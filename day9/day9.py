logo = '''
                         ___________
                         \         /
                          )_______(
                          |"""""""|_.-._,.---------.,_.-._
                          |       | | |               | | ''-.
                          |       |_| |_             _| |_..-'
                          |_______| '-' `'---------'` '-'
                          )"""""""(
                         /_________\\
                       .-------------.
                      /_______________\\
'''

bid ={}
def find_highest (bid):
    winner =""
    highest=0
    for bidder in bid :
        bid_amount=bid[bidder]
        if bid_amount> highest:
            highest=bid_amount
            winner=bidder
    print(f"the winner is {winner} with bid of {highest}")
x=True
while x:
  name=input("what is your name?: ")
  biding=int(input ("what is your bid?: "))
  bid[name]=biding 
  x=input("are there any bidders left yes or no: \n").lower() 
  if x=="no":
      find_highest (bid)
      break
      
 




