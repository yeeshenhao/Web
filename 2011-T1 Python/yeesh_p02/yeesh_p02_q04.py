##Filename: yeesh_p02_q04.py
##Name: Yee Shen Hao
##Description: Write a program that prompts the user to enter a year and determines whether it is a leap
##year. A year is a leap year if it is divisible by 4 but not 100, or is divisible by 400. A sample
##session:

# Prompt user to input the year
year = int(input("Enter year (AD):"))

# Check if input is leap year:
if year > 0 and ((year%4 == 0 and year%100 != 0) or year%400 == 0) :
    print(year, "is leap year.")
elif year <= 0 :
    print("Please enter a valid year (AD).")
else:
    print(year, "is not leap year.")

end = input("Press ENTER to exit")
