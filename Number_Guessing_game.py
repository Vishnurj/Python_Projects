import random


def random_number():
    score = 0
    guessed_number = random.randint(1,100)
    
    print("Welcome to Guessing game..! Try to Guess the number between (1  to 100)")
    
    while True:
      
       number = None
       try:
          number = int(input("Enter the Guess :"))
       except ValueError:
          print("Invalid Input..! Enter the number  ")
          continue
      
       if number is not None:
          if  guessed_number == number:
            print("Congrulations Buddy..You Guess is right like as always")
            score = score + 10
            print(f"The Current Score is :{score}")
            play_again = input("Do you want to play game again (y/n):").lower()
          
            if play_again == "n":
             print(f"Thanks for playing  and your final score is : {score}..See you again ")
             break
            else:
              guessed_number = random.randint(1, 100)
              print("Hurry..Let's play one more round")
          elif number < guessed_number:
           print("oooopss..Try some Big number")
              
          else:
            print("oooopss..Try some Small number")
     
      
  
random_number()