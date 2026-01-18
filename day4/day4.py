import random
rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''



#less efficient code




# user_input=int(input("what do you want to choose ? type 0 for rock ,1 for paper, 2 for scissor."))
# if user_input >= 3 or user_input < 0:
#     print("You typed an invalid number, you lose!")
# else:
#     if user_input==0:
#      print(rock)
#     elif  user_input==1:
#      print(paper)
#     elif  user_input==2:
#      print(scissors)
#     com_random=random.randint(0,2)
#     if com_random==0:
#      print(rock)
#     elif com_random==1:
#      print(paper)
#     elif  com_random==2:
#      print(scissors)

# #to decide who win 

# if user_input == 0 and com_random == 2:
#         print("You win!")
# elif com_random == 0 and user_input == 2:
#         print("You lose")
# elif com_random > user_input:
#         print("You lose")
# elif user_input > com_random:
#         print("You win!")
# elif com_random == user_input:
#         print("It's a draw")



#more efficient code


game_images = [rock, paper, scissors]
user_input=int(input("what do you want to choose ? type 0 for rock ,1 for paper, 2 for scissor."))
if user_input >= 3 or user_input < 0:
    print("You typed an invalid number, you lose!") 
else:
    print(game_images[user_input])
    computer_choice = random.randint(0, 2)
    print("Computer chose:")
    print(game_images[computer_choice]) 
    if user_input == 0 and computer_choice == 2:
        print("You win!")
    elif computer_choice == 0 and user_input == 2:
        print("You lose")
    elif computer_choice > user_input:
        print("You lose")
    elif user_input > computer_choice:
        print("You win!")
    elif computer_choice == user_input:
        print("It's a draw")