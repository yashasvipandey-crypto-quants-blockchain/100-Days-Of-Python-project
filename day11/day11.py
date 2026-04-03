# blackjack capstone project
import random

cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
x=input("do you want to play y or n: ")
if x=="y":
    print( "\n"*20 )
    your_card=[]
    your_card.append(random.choice(cards))
    your_card.append(random.choice(cards))
    y=sum(your_card)
    print(f"your card{your_card},sum={y}")
    dealer_card=[]
    dealer_card.append(random.choice(cards))
    z=sum(dealer_card)
    print(f"dealer card{dealer_card},sum={z}")
    dealer_card.append(random.choice(cards))
    is_game_over = False
    while is_game_over==False:



            

    
else: 
    print("bye")

    
