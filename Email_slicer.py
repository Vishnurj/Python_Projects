def email_silcer(email):
 
    if "@" not in email:
     print("Invalid email ")
     return
 
    username,domain = email.split("@")
    print(f"UserName : {username}\nDomain : {domain}")

email =input("Enter the mail id :")
email_silcer(email)
  