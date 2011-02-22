## Filename: yeesh_p02_q03.py
## Name: Yee Shen Hao
## Description: Write a program that prompts the user to enter a score between 0 and 100 inclusive. The
##grading system is as follows: is valid or not.

# prompt for input
score = float(input("Enter score (%): "))

if score > 69 and score < 101:
    print("Your grade is A.")

elif score > 59 and score < 70:
    print("Your grade is B.")

elif score > 54 and score < 60:
    print("Your grade is C.")

elif score > 49 and score < 55:
    print("Your grade is D.")
    
elif score > 44 and score < 50:
    print("Your grade is E.")
    
elif score > 34 and score < 45:
    print("Your grade is S.")
    
elif score >= 0 and score < 35:
    print("Your grade is U.")
    
else:
    print("Invalid Score")

end = input("Press ENTER to exit")
