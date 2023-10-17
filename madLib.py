# madLib game

#! Taking user inputs 
name = input("Enter name: ") 
school = input("What school did you go to? ")
food = input("On a scale of 1-10 how much do you like food? ")
sport = input("What sport do you play? ")
ability = input("Were you any good? ")

#! Converting food to integer
food = int(food)

#* Creating the Story
awesome_story = f"There once was a boy named {name}. He went to {school} during his school years. When it comes to how much he likes food on a scale of 1-10 he says {food}. He played {sport} and answered {ability} when it came to describing how good he was."

#?Printing the story 
print(awesome_story)

