# madLib game
from home_page import get_integer_input1

def main():
    #! Taking user inputs 
    name = input("Enter name: ") 
    school = input("What school did you go to? ")
    food = get_integer_input1("On a scale of 1-10 how much do you like food? ")
    sport = input("What sport do you play? ")
    ability = input("Were you any good? ")
    print()

    #! Converting food to integer
    food = int(food)

    #* Creating the Story
    awesome_story = f"""
There once was a boy named {name}. 
He went to {school} during his school years. 
When it comes to how much he likes food on a scale of 1-10 he says {food}. 
He played {sport} and answered {ability} when it came to describing how good he was."""

    #?Printing the story 
    print(awesome_story)

if __name__ == "__main__":
    main()