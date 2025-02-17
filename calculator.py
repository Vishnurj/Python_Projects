import time

print("Welcome to simple calculator")
def countdown():
  print("Your calculator starts in few seconds....")
  for i in range(1,4):
    print(i)
    time.sleep(2)
    
    
def add(x,y):
    return x + y
  
def sub(x,y):
    return x - y
  
def mul(x,y):
    return x * y
  
def div(x,y):
    if y != 0:
      return x / y
    else:
      print("Error.. division by zero")
  
def pow(x,y):
    return x ** y
  
def calculate():
  
    countdown()
    print("Hey..Let's start calculating..")
    print("\nselect operation :")
    print("1.Add")
    print("2.Subtract")
    print("3.Multiply")
    print("4.Divide")
    print("5.Power")
    print("6.Quit")
    
    while True:
      
      choice = input("Enter your choice(1/2/3/4/5/6):")
      
      if choice == '6':
        print("Thank you")
            
      x = float(input("Enter the number1:"))
      y = float(input("Enter the number2:"))
      
      if choice == "1":
        print(f"The result is : {add(x,y)} ")
      elif choice == "2":
        print(f"The result is : {sub(x,y)} ")
      elif choice == "3":
        print(f"The result is : {mul(x,y)} ")
      elif choice == "4":
        print(f"The result is : {div(x,y)} ")
      elif choice == '5':
        print(f"The result is : {pow(x,y)} ")
      else:
        print("Invalid Input")
        
if __name__ == "__main__":
    calculate()
    