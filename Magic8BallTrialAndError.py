#imported modules in this case we only imported the "random" module using import random
import random

#Declared the variables:
Name = "Joseph"
Question = "Will There Be Free Doritos In The Office Today?"
answer = ""

#Created a call to a random integer in a function and assigned the random_number variable to it
random_number = random.randint(1, 9)
#Next line was a test to see if it prints off the random number and if the variable works using the print(random_number) line here.

#Then I set up my If/Else/Elif statement
if random_number == 1:
  answer = "Yes - definitely"
elif random_number == 2:
  answer = "It is decidedly so"
elif random_number == 3:
  answer = "Without a doubt"
elif random_number == 4:
  answer = "Reply hazy, try again"
elif random_number == 5:
  answer = "Ask again later"
elif random_number == 6:
  answer = "Better not tell you now"
elif random_number == 7:
  answer = "My sources say no"
elif random_number == 8:
  answer = "outlook not so good"
elif random_number == 9:
  answer = "very doubtful"
else: 
  answer == "Error"

#Trying it out and put it into action
if Name == "":
  print(Question)
elif Question == "":
  print("You need to ask a question to the magic 8-ball otherwise the magic is lost")
else:
  print(Name,"asks:",Question)
  print("8-Ball's answer:",answer)


# I tested my final if/else statement by putting empty strings into the Name and Question variable's output and got my if/else statement to function well. 
# The only thing i struggled with was the syntax of my if else statement adapting to powershell structure and often forgetting when to put == vs = 
# I also struggled a bit with putting in  my def when asked to Declare a variable called random_number, and assign it to the function call: random.randint(1, 9)
# This was because I kept trying to overcomplicate it. Simpler was better, and I misread it as writing a def statment like def(call) = random = random.randint(1, 9), which definitely didn't work.