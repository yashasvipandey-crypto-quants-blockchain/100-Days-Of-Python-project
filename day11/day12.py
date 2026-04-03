import random
x=random.randint(1,100)
def easy():
    print("you have 10 attempts to guess the number ")
   
    for i in range(1,11):
        print(f"you have {11-i} attempts remaining")
        y=int(input("make a guess: "))
        if x==y:
            print(f"you got it ! the answer is {x}")
            break
        else :
            if y<x:
                print("Too low")
            elif y>x:
                print("Too high")
    print(f"Game Over! The correct number was {x}")   
def hard():
     print("you have 5 attempts to guess the number ")
     for i in range(1,6):
        print(f"you have {6-i} attempts remaining")
        y=int(input("make a guess: "))
        if x==y:
            print(f"you got it ! the answer is {x}")
            break
        else :
            if y<x:
                print("Too low")
            elif y>x:
                print("Too high")
     print(f"Game Over! The correct number was {x}")
print("welcome to the number gussing game ")
print( "i am thinking of a number between 1 and 100")
diff=input("choose a difficulity easy or hard: ").lower()
if diff=='easy':
    easy()
else :
    hard()
