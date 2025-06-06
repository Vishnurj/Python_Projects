print('--contact book---')

contact_book = {}

def contact_menu():
       while True:
           print("\n select option")
           print("1.Add Contact")
           print("2.View Contacts")
           print("3.Delete Contact")
           print("4.Exit")
   
           try:
               option = int(input("Enter your option"))
           except ValueError:
               print("Invalid option try again")
               return
   
           if option == 1:
               add_contact()
           elif option == 2:
               view_contact()
           elif option == 3:
               delete_contact()
           elif option == 4:
               print("Contact Book closed")
               break
           else:
               print("Invalid option ,Try again")
   
def add_contact():
       name = input("Enter the name")
       number = int(input("Enter the phone number"))
       contact_book[name] = number
       print(f"Contact '{name}' is added successfully")
   
def view_contact():
       if not contact_book:
           print("Contacts Not found")
       else:
           for name, number in contact_book.items():
               print(f"{name}:{number}")
   
def delete_contact():
       name = input("Enter the name :")
       if name in contact_book:
           print(name)
           del contact_book[name]
           print(f"Contact '{name}' is deleted successfully")
       else:
           print(f"{name} not found to delete")

contact_menu()

