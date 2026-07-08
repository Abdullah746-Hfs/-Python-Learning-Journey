username = str(input("Enter your username: ")).lower()
password = str(input("Enter your password: ")).lower()
match username:
    case "admin":
     if password =="123":
       print("Welcome admin")
     else:
        print("Incorrect password")
    case "admin123":
     if password == "12345":
          print("Welcome admin123")
     else:
          print("Incorrect password")
    case "admin12345":
     if password == "admin1234":
             print("Welcome 12345!")
     else:
             print("Incorrect password")
    case _:
     print("Incorrect credentials")




  