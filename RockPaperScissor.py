import random
random_choice=random.randint(1,3)
user_input1=input("user_input is: ")
user_input=user_input1.capitalize()
if(random_choice==1):
    print("Random_input: Rock")
elif(random_choice==2):
    print("Random_input: Paper")
elif(random_choice==3):
    print("Random_input: Scissor")

if(random_choice==1 and user_input=="Rock" or random_choice==2 and user_input=="Paper" or random_choice==3 and user_input=="Scissor"):
    print("Result: Draw")
elif(random_choice==1 and user_input=="Paper" or random_choice==2 and user_input=="Scissor" or random_choice==3 and user_input=="Rock"):
    print("Result: User wins")
elif(random_choice==2 and user_input=="rock" or random_choice==1 and user_input=="Scissor" or random_choice==1 and user_input=="Scissor" or random_choice==3 and user_input=="Paper"):
    print("Result: Computer wins")
else:
    print("error")