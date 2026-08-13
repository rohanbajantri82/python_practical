name = input("Enter student's name: ")

marks1 = float(input("Enter marks for Subject 1: "))
marks2 = float(input("Enter marks for Subject 2: "))
marks3 = float(input("Enter marks for Subject 3: "))

total = marks1 + marks2 + marks3
average = round(total *100 /300)

print("\n===== Final Scorecard =====")
print(f"Student Name : {name}")
print(f"Subject 1    : {marks1}")
print(f"Subject 2    : {marks2}")
print(f"Subject 3    : {marks3}")
print(f"Total Marks  : {total}")
print(f"Average Marks: {average}")
print("===========================")














