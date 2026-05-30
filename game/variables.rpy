#region Persistent Variables
#playthrough flags
default persistent.true_reset_visible = False
default persistent.completed_playthroughs = 0
default persistent.first_playthrough = True

#story path and ending flags
default persistent.got_the_guy = False #roll the guy by random chance
default persistent.girlfriend_flag = True #have gabriel ask you if your game is more important than your girlfriend
default found_gf_flag = False #nonpersisted flag that merely exists to prevent the player from acquiring the flag before finishing a route.
default persistent.ed_appears = False 
default persistent.seen_ed = False #set to true adter the player meets ed for the first time

default persistent.impostor_seen = False #encounter impostor ed for the first time.
default persistent.gabriel_complete = False #reach either end of a gabriel route
default persistent.ed_complete = False #reach the end of the ed route
default persistent.niecy_complete = False #reach the normal ending



#endregion

#region Gameplay Variables
#Gacha pull mechanics

init 0 python:
    impostor_name = ""
    if persistent.seen_ed:
        impostor_name = "Ed?"
    else:
        impostor_name = "Ed"

    repeat_requests = 0
    since_last_repeat = 0 #increments every line.
    repeat_active = True

    class Guy:
        def __init__(self, name, image, rarity, is_the_guy=False):
            self.name = name
            self.image = image #where image is the name of the file provided as a string
            if rarity >= 0 and rarity < 5:
                self.rarity = rarity
            else:
                self.rarity = 1
                #rarity auto set to uncommon if I make a mistake
            self.is_the_guy = is_the_guy

    def count_repeat(event, interact=True, **kwargs):
        if event is "end":
            global since_last_repeat
            since_last_repeat +=1

    class Spontaneous:
        def __init__(self, label, priority, group, jump=False, lines_until=0):
            self.label = label #string
            self.priority = priority #int
            self.group = group #string
            self.jump = jump #where jump is true and call is false
            self.lines_until = lines_until #int
    
    class SpontaneousHandler:
        def __init__(self):
            self.current_spontaneous = None
            
        def add_spontaneous(self, spontaneous):
            self.current_spontaneous = spontaneous #we'll see if we can pull the data from just the object
            
            
        def update_spontaneous(self, event, interact=True, **kwargs):
            if event is "end":
                if self.current_spontaneous == None:
                    #return early because there's nothing to update
                    return
                    
                else:
                    self.current_spontaneous.lines_until -= 1
                    if self.current_spontaneous.lines_until <=0:
                        match self.current_spontaneous.jump:
                            case True:
                                label = self.current_spontaneous.label
                                self.current_spontaneous = None
                                renpy.jump(label)
                            case False:
                                label = self.current_spontaneous.label
                                self.current_spontaneous = None
                                renpy.call(label)
                    else:
                        return

            else:
                return

    greenout_time = 0
            

define greenout = Spontaneous("weed", 0, "weed", jump=True, lines_until=5)
define spontaneous_handler = SpontaneousHandler()
define config.all_character_callbacks = [count_repeat, spontaneous_handler.update_spontaneous]

    


#make a bunch of test guys
define test_guy_0 = Guy("theguy1", "ph_mint_heart.png", 0)
define test_guy_1 = Guy("theguy2", "ph_brown_heart.png", 1)
define test_guy_2 = Guy("theguy3", "ph_purple_heart.png", 2)
define test_guy_3 = Guy("theguy4", "ph_mitski.png", 3)
define test_guy_4 = Guy("theguy5", "ph_baba.png", 4)
define test_the_guy = Guy("he's The GUY", "ph_the_guy.png",4, is_the_guy = True)
define all_guys = {test_guy_0, test_guy_1, test_guy_2, test_guy_3, test_the_guy}


init 1 python:
    class Gacha:
        total_rolls = 0
        pity_threshold = 25
        def __init__(self, set_of_all_guys):
            self.__total_rolls = 0
            self.__pity_count = 0
            self.__pity_active = False
            self.__commons = []
            self.__uncommons = []
            self.__rares = []
            self.__super_rares = []
            self.__ultra_rares = []
            for guy in set_of_all_guys:
                match guy.rarity:
                    case 0:
                        self.__commons.append(guy)
                    case 1:
                        self.__uncommons.append(guy)
                    case 2:
                        self.__rares.append(guy)
                    case 3:
                        self.__super_rares.append(guy)
                    case 4:
                        self.__ultra_rares.append(guy)
                    case _:
                        pass
                        
                pass
            #the last value in the pool are the weights
            self.__normal_pool = [self.__commons, self.__uncommons, self.__rares, self.__super_rares, self.__ultra_rares, [55,92,97,99,100]]
            self.__first_pool = [self.__commons, self.__uncommons, self.__rares, self.__super_rares, [55,90,97,100]] #the first pull will never get the guy
            self.__pity_pool = [self.__rares, self.__super_rares, self.__ultra_rares, [0,0,100]]
            self.__is_first_roll = True
        
        def __gacha_rand(self, pool):
            #population is everything except the last index
            #cumulative weights is the last index
            #weighted selection of a pool of guys
            active_pool = renpy.random.choices(pool[:-1], cum_weights=pool[-1])

            #unweighted choice of a guy of that rarity. should be a type guy
            return renpy.random.choice(active_pool)


        def pull_guy(self):
            global current_guy
            if self.__is_first_roll == True:
                this_guy = self.__gacha_rand(self.__first_pool) #first pull randomizer
                self.__is_first_roll = False #turns off first pull flag
                self.__total_rolls += 1 #keeps track of all rolls
                self.__pity_count += 1 #keeping track of the pity roll counter
                if self.__pity_count >= self.pity_threshold:
                    self.__pity_active = True #if the pity counter reaches the threshold, the pity roll will be active for the next roll
                #this_guy.image added to gallery (list of guys)
                current_guy = this_guy[0]
                return this_guy[0]
            elif self.__pity_active:
                this_guy = self.__gacha_rand(self.__pity_pool) #pity randomizer
                self.__pity_count = 0 #resets count and turns off pity roll
                self.__pity_active = False
                self.__total_rolls += 1 #keeps track of all rolls
                self.__pity_count += 1 #keeping track of the pity roll counter
                if self.__pity_count >= self.pity_threshold:
                    self.__pity_active = True #if the pity counter reaches the threshold, the pity roll will be active for the next roll         
                current_guy = this_guy[0]     
                return this_guy[0]
            else:
                this_guy = self.__gacha_rand(self.__normal_pool) #regular randomizer
                self.__total_rolls += 1 #keeps track of all rolls
                self.__pity_count += 1 #keeping track of the pity roll counter
                if self.__pity_count >= self.pity_threshold:
                    self.__pity_active = True #if the pity counter reaches the threshold, the pity roll will be active for the next roll
                current_guy = this_guy[0]
                return this_guy[0]


            #the object that comes out of pull guy should be a Guy object
        
        #Getters
        def get_pity_count(self):
            return self.__pity_count

        def get_pity_active(self):
            return self.__pity_active

        def get_total_rolls(self):
            return self.__total_rolls

        def get_is_first_roll(self):
            return self.__is_first_roll


default gacha_puller = Gacha(all_guys)
default roll_obj = Gacha.pull_guy
default can_pull = True
default guy_end = False

default current_guy = test_guy_0

default gems = 115
define pull_cost = 7

default list_of_pulls = []

init 2 python:
    class PullGuy(Action):
        def __call__(self):
            global gacha_puller
            global current_guy
            global list_of_pulls
            current_guy = gacha_puller.pull_guy()
            unassuming_local_guy = current_guy
            list_of_pulls.append(unassuming_local_guy)
            return current_guy

        pass


#timer and money mechanics


init python:
    import decimal as d
    money_spent = d.Decimal('0.00')
    #define all decimal objects here.
    gem_price_1 = d.Decimal('0.99')
    gem_price_2 = d.Decimal('4.99')
    gem_price_3 = d.Decimal('19.99')
    gem_price_4 = d.Decimal('29.99')
    gem_price_5 = d.Decimal('49.99')
    gem_price_6 = d.Decimal('99.99')
    time_price_1 = d.Decimal('1.49')
    time_price_2 = d.Decimal('5.49')
    time_price_3 = d.Decimal('9.49')
    time_price_4 = d.Decimal('16.49')
    time_price_5 = d.Decimal('27.49')
    

    def update_money(amount):
        #since we only need to add money, it won't be too complex.
        #it accepts one argument.
        global money_spent
        money_spent += amount

    import datetime as dt
    timer_started = False
    max_time = dt.timedelta(hours=3)
    time_elapsed = 0
    current_time = max_time
    
    def decrement_timer():
        global time_elapsed
        global current_time
        if current_time.seconds <= 0:
            current_time = max_time
            time_elapsed = 0
            return
        time_elapsed += 1
        current_time = dt.timedelta(seconds=max_time.seconds-time_elapsed)

    def buy_time(amount_in_seconds, price):
        global time_elapsed
        global current_time
        global gems
        total_passed_time = time_elapsed + amount_in_seconds
        time_check = max_time.seconds - total_passed_time
        update_money(price)
        if time_check < 0:
            current_time = max_time
            time_elapsed = 0
            gems += 50
            return
        else:
            time_elapsed += amount_in_seconds
            current_time = dt.timedelta(seconds=max_time.seconds-time_elapsed)


    
    


#phone interrupt mechanic

#endregion

#story variables/inventory
default story_index = 0 #where in the story the player is
default gabriel_present = False #true if gabriel is on screen

default niecy_irritation = 0 #counts the number of times you've irritated her

default has_gummy = False

#region Images and Transforms


image bg black = Solid("#000")
image bg white = Solid("#fff")
image bg green = Solid("#486316")
image bg room cassiopeia = Image("bg_cas_room.png")

image cg white = Solid("#fff")
image cg green = Solid("#486316")
image cg covers 0 = Image("cg_covers_0.png")
image cg covers 1 = Image("cg_covers_1.png")
image cg covers 2 = Image("cg_covers_2.png")
image cg covers 3 = Image("cg_covers_3.png")
image cg covers 4 = Image("cg_covers_4.png")
#image cg ceiling
#image cg warning
#image cg thatsit
#chase sequence cg might be more elaborate

#cutins
#note: to show multiple cutins at once, use the "as" statement to dyanmically assign a new tag to the second cutin
transform handpos:
    pos (800, 700)
    pause 1.0
    pos (150, 50)

image cutin gummy1 = Image("ci_ed_appears.png")
layeredimage cutin gummy2:
    always:
        "ci_gummy_background"
    attribute gummy:
        image:
            "ci_gummy_gummy"
        pos (300, 380)
  
    group hand:
        attribute fist:
            image:
                "ci_gummy_hand_fist"
                pos (0, 0)
                
                
            
                
            
        attribute splay:
            image:
                "ci_gummy_hand_splay"
                pos (150, 50)
        

image cutinraw = LayeredImageProxy("cutin gummy2")
image maskedcutin = AlphaMask("cutinraw", "ci_gummy_mask.png")
        

        
    
    


#gabriel's talk sprites
#pose 1
image gabriel neutral = Image("ch_gabriel_neutral.png")
image gabriel smug = Image("ch_gabriel_smug.png")
image gabriel concern = Image("ch_gabriel_concern.png")
image gabriel annoyed = Image("ch_gabriel_annoyed.png")
image gabriel unimpressed = Image("ch_gabriel_unimpressed.png")
#pose 2
image gabriel groggy = Image("ch_gabriel_groggy.png")
image gabriel rage = Image("ch_gabriel_rage.png")

#niecy's talk sprites
#pose 1
image niecy neutral = Image("ch_niecy_neutral.png")
image niecy smile open = Image("ch_niecy_smile_open.png")
image niecy smile close = Image("ch_niecy_smile_close.png")
image niecy smile speed = Image("ch_niecy_smile_speed.png")
image niecy concern = Image ("ch_niecy_concern.png")
image niecy confuse = Image("ch_niecy_confuse.png")
image niecy coy = Image("ch_niecy_coy.png")
image niecy unimpressed = Image("ch_niecy_unimpressed.png")

#pose 2
image niecy angry = Image("ch_niecy_angry.png")
image niecy relief = Image("ch_niecy_relief.png")
image niecy uhoh = Image("ch_niecy_uhoh.png")

#endregion

#region Audio




#endregion

#region Characters

define c = Character("Cassiopeia")
define n = Character("Niecy", image="niecy")
define g = Character("Gabriel", image="gabriel")
define e = Character("Ed")
define i = Character("impostor_name", dynamic=True)


#impostor name is Ed unless the game has been cleared


#endregion

