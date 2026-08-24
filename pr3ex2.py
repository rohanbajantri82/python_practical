#placement eligibility

score = float(input("Enter graduation score (%):"))
backlogs = int(input("Enter number of backlogs:"))

if score >= 70 and backlogs == 0:
    print("candidate is eligible for placement.")

else:
    print("candidate is not eligible for placement.")

    if score < 70 and backlogs ==0:
        print("Reason:graduation score is below 70%.")

    else:
        print("Reason:candidate has active backlogs.")
