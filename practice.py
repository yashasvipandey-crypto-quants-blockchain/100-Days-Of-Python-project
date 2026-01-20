import random
# import pracice

# random_integer=random.randint(1,10)
# print(random_integer)
# print(pracice.xsos)
# random_number=random.random()*10
# print(random_number)
# random_float=random.uniform(1,10)
# print(random_float)
# rand_int=random.randint(0,1)
# print(rand_int)


# if rand_int=="0":
#     print("heads")
# else:
#     print("tails")
# states=["hello","hi","yo","gg"]
# print(states[0])
# states.extend(["guy","new","you"])
# print(states)

# friends = ["Alice", "Bob", "Charlie", "David", "Emanuel"]
# friends_r=random.randint(0,4)
# print(friends_r)
# print(friends[friends_r])
# print(random.choice(friends))

# fruits = ["Strawberries", "Nectarines", "Apples", "Grapes", "Peaches", "Cherries", "Pears"]
# vegetables = ["Spinach", "Kale", "Tomatoes", "Celery", "Potatoes"]
# num=len(fruits)
# print(num)
# dirty_dozen = [fruits, vegetables]
# print(dirty_dozen[1][1])

# fruits =["apple","peach","pear"]
# for fruits in fruits:
#     print(fruits)   
#     print(fruits+"pie")
# student_score=[150,450,200,800,623,456,]
# total=sum(student_score)
# print(total)
# sum=0
# for score in student_score:
#     sum+=score
#     print(sum)
# max_score=0
# for score in student_score:
#     if score>max_score:
#         max_score=score
# print(max_score)
#range
# for number in range(0,10,2):
#     print(number)
# total=0
# for number in range(1,100):
#    total+=number
# print(total)
for number in range(1,101):
    if number%15==0:
        print("FizzBuzz")
    elif number%3==0:
        print("Fizz")
    elif number%5==0:
        print("Buzz")
    else:
        print(number)
