##Filename: yeesh_p02_q05.py
##Name: Yee Shen Hao
##Description: Write a program that prompts the user to enter the month and year, and displays the
##number of days in the month. 

import calendar

# User input
month = int(input("Enter a month (in digits):"))
year  = int(input("Enter a year:"))

month_range =str(calendar.monthrange(year,month))

month_10 = month_range[-3]
month_1  = month_range[-2]


#output
print("Number of days in", calendar.month_name[month], year, "is", month_10 + month_1)

end = input("Press ENTER to exit")
