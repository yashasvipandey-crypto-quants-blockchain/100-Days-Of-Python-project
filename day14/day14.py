# higher lower game
import random
import data
import art

game_should_continue = True

compare_A = random.choice(data.data)
compare_B = random.choice(data.data)

count = 0

def a():
    print(compare_A["name"], "is a", compare_A["description"], "from", compare_A["country"])

def b():
    print(compare_B["name"], "is a", compare_B["description"], "from", compare_B["country"])

def checker(y):
    if compare_A["follower_count"] > compare_B["follower_count"]:
        ans = 'A'
    else:
        ans = 'B'

    if ans == y:
        return True
    else:
        return False


while game_should_continue == True:

    print(art.logo)

    # avoid same A and B
    while compare_A == compare_B:
        compare_B = random.choice(data.data)

    a()
    print(art.vs)
    b()

    print(f"score {count}")
    x = input("type 'A' or 'B': ").upper()

    # input validation
    if x != 'A' and x != 'B':
        print("Invalid input! Game over.")
        print(f"final score {count}")
        game_should_continue = False

    else:
        result = checker(x)

        if result == True:
            count += 1
            compare_A = compare_B
            compare_B = random.choice(data.data)

        else:
            print(f"gameover with score {count}")
            game_should_continue = False