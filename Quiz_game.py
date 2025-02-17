def play_game():
   score = 0
   Name = input("Enter the Name :")
   print("Hey ",Name,"Welcome to the Game...!")
   should_we_play = input("Are you ready to play Guessing game :").lower()

   if should_we_play == "yes" or should_we_play == "y":
    print("Hurry..let's play")
    
   
    while True:
     Direction = input("Now it's time to go to Top of the mountain ..choose (Right/Left) :").lower()
     if Direction == "left":
           print("Sorry your choice is wrong ..you won't reach the top of the mountain ..you lost the game..play again")
           break
     elif Direction == "right":
        print("Congrulations you reached top of the mountain.. Level 1 cleared ")
        score = score + 10
        print("you earned score is :",score)
       
        
        print("Now it's time to cross river..?will you swim in water  or cross it via bridge ")
        choice = input("choose swim or bridge and Type it : ").lower()
        
        if choice == "swim":
          print("Sorry.. You are eaten by alligator,you died,play again")
          break
        elif choice == "bridge":
          print("Congrulations you crossed the river.. Level 2 cleared ")
          score = score + 10
          print("you earned score is :",score)
        else:
          print("Sorry it's invalid choice..game ended..play again")
          break
        
        print("Now its time move into forest..Are you ready")
        choice = input("You see a wolf. Fight or run ? : ").lower()
        if choice == "fight":
         print("Congrulations You defeated the wolf level 3 cleared and  proceed to the next level")
         score = score + 10
         print("you earned score is :",score)
        elif choice == "run":
         print("You tripped and got injured. Game over.")
         
     
  

    
    
     should_we_play = input("Do you want to play again? (yes/no): ").lower()
     if  should_we_play not in ["YES", "yes"]:
      print(f"Thanks for playing! Your final score is: {score}")
      break
  

    

    
    
play_game()