age = int(input("Enter age:"))

income = float(input("Enter annual family  income:"))

caste = input("enter your caste (SC/ST/NT/OBC/OPEN):")

if age < 25 and income < 300000 and caste in ["SC" "ST" "NT" "OBC"]:
    print("you are eligible for scholorship:")

else:
    print("you are not eligible for scholorship:")