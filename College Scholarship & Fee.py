marks = int(input("Enter your marks: "))
if marks >100 and marks<=0:
    print("Invalid marks")
gareebi_pass = input("Do you have a gareebi pass? yes or no: ").lower()
if marks<=50:
    print("Try harder next time")
elif gareebi_pass == "yes" and marks>=90:
        print("Congratulations! You have been awarded a Full Scholarship")
elif gareebi_pass == "no" and marks>50 and marks<90 and marks%2==0:
                print("You qualify for a Partial Scholarship")
else:
                    print("You qualify for a base-level tuition grant.")

