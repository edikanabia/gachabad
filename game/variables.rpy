#region Constants
#define pity_threshold = 100




#endregion

#region Gameplay Variables
#Gacha pull mechanics
default is_first_roll = True
default number_of_rolls = 0
default number_of_pity = 0
default money_spent = 0.00
default is_pity_roll = False

#timer mechanics

#repeat that mechanic
default repeat_count = 0
default since_last_repeat = 0 #increments every line.
default repeat_active = True

#phone interrupt mechanic
default story_index = 0 #where in the story the player is
default gabriel_present = False #true if gabriel is on screen
default will_bother_niecy = False #true if an action will bother niecy at a particular moment
default niecy_tolerance = 0 #counts the number of times you've irritated her
#endregion



#region Images and Transforms


image bg black = Solid("#000")
image bg white = Solid("#fff")



#image cg ceiling
#image cg warning
#image cg thatsit
#chase sequence cg might be more elaborate

#endregion

#region Audio




#endregion

#region Characters

define c = Character("Cassiopeia")
define n = Character("Niecy")
define g = Character("Gabriel")
define e = Character("Ed")



#endregion

