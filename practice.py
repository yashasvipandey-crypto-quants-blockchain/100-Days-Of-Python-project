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
# for number in range(1,101):
#     if number%15==0:
#         print("FizzBuzz")
#     elif number%3==0:
#         print("Fizz")
#     elif number%5==0:
#         print("Buzz")
#     else:
#         print(number)



# word_list =["aadvark","baboon","camel"]
# x=random.choice(word_list)

# word_len=len(x)

# holderplace=""

# for under in range(word_len):

#     holderplace += "_"

# print(holderplace) 
# game_over=False 
# correct=[]
# display="_"*len(X)
# while not game_over:
#     y=str(input("guess the letter: ")).lower()
    
#     for word in x:
    
#         if word==y:
#             display += word
#             correct.append(word)
#         elif word in correct:
#             display+=word
    
#         else:
#             display +="_"

#     print(correct)
    
#     if "_" not in display:
#         game_over=True
#         print("you win")

# def greet():
#     print("hello")
#     print("how do you do")

# greet()
# def greet(name,location ):
#     print (f"hello {name}")
#     print(f"what is like to be {location}")
    
# # greet("muk","saharanpur")
# greet(location="sarahanpur",name="muk")

# programming_dictionary = {"Bug": "An error in a program that prevents the program from running as expected.", "Function": "A piece of code that you can easily call over and over again."}
# # print(programming_dictionary["Bug"])


# programming_dictionary["loop"]="hellow yr"
# # print(programming_dictionary["loop"])
# # for thing in programming_dictionary:
# #     print (thing)
# #     print(programming_dictionary[thing])
# capitals ={
#     "france":"paris",
#     "germany":"berlin"
# }
# travel={
#     "france":["paris","lille"],
#     "germany":["berline","stuttgart"]
# }
# print(travel["france"][1])
# nested_list = ["A", "B", ["C", "D"]]
# print(nested_list[2])
# travel_log = {
#   "France": {
#     "cities_visited": ["Paris", "Lille", "Dijon"], 
#     "total_visits": 12
#    },
#   "Germany": {
#     "cities_visited": ["Berlin", "Hamburg", "Stuttgart"], 
#     "total_visits": 5
#    },
# }
# print(travel_log["France"]["cities_visited"][1])
