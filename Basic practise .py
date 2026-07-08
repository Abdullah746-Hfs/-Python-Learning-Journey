# Type conversion

# num = int(input("Enter a number"))
# print(num+5)
 

# num = (input("Enter a number"))
# print(int(num)+5)
 
# age = int(input("Enter your age: "))
# name = str(input("Enter your name: ")).lower()
# city = str(input("Enter your city name: ")).lower()
# print("Your age is:", age, " || Your age data type is: ", type(age))
# print("Your name is: ", name, " || And the data type of your name is: ",type(name))

# if age>=18:
#     print("You are eligible to drive ")
# elif age<18:
#     print("Go study")
# else:
#     print("Invalid")

# age = int(input("Please enter your age: "))
# if age > 18:
#      print("You can legally drive a car")
#      allow = "Yes"
# elif age != 18:
#      allow = "No"
#      print("You are not eligible to drive")
# else:
#      print("Invalid please try again")

# print("Your age is:" + " " + str(age))
# if age >= 18:
#    print("yes you can drive")
# else:
#      print("You cannot drive")


# num = int(input("Enter a number: "))
# if num>10: 
#     print("Your number is greater than 10")
# elif num<5:
#     print("Your number is less than 5")
# elif num%2==0:
#     print("Your number is even")
# elif num%3==0:
#     print("Your number is an odd number")
    
# else:
#     print("Your number is between 5 and 10")
# num2 = int(input("Enter a number: "))    
# if num==num2:
#     print("Both numbers are equal")

# age = int(input("Please enter your age: "))
# if age>=18:
#     print("You are an adult")

# num = int(input("Enter a number: "))
# if num>0:
#     print("Your number is postive")
# else:
#     print("Your number is negative")
# score = int(input("Enter your score: "))
# if score>70:
#     print("You passed")
# else:
#     print("You failed")
# age = int(input("Enter your age: "))
# if age<10:
#     print("You are a child")
# elif age>+10 and age<18:
#     print("You are a teen")
# else:
#     print("You are an adult")

# num2 = int(input("Enter a number: "))
# if num2%3==0:
#     print("Your number is divisible by 3")
# else:
#     print("Your number is not divisible by 3")
# num3 = int(input("Enter a number: "))
# if num3%2==0:
#     print("Your number is even")
# elif num3%3==0:
#     print("Your number  is odd")
# elif num3==0:
#     print("Your number is zero")
# else:
#     print("Invalid input")

          

choice = input("Are you a member, 'Yes' or 'No'?").lower()
if choice == "yes":
    print("You are a member")
    if choice == "yes":
        amount = int(input("Tell your purchase amount: "))
        if amount>= 50:
           print("You get a 20% discount")
           new_amount =  amount  - amount*0.2
        if amount<50:
                print("Yoou get a 10% discount")
                new_amount = amount - amount*0.1
                if choice == "no":
                     print("You are not a member")
print("Your final amount to pay is: ", new_amount)

        
           