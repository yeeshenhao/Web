## Filename: yeesh_p02_q06.py
## Name: Yee Shen Hao
## Description: Write a program that sorts three integers. The integers are entered from standard input and
##stored in variables num1, num2, and num3, respectively. The program sorts the numbers
##so that num1 > num2 > num3. The result is displayed as a sorted list in descending order


# User input
num1 = int(input("Enter 1st integer:"))
num2 = int(input("Enter 2nd integer:"))
num3 = int(input("Enter 3rd integer:"))

#Create list
sort = [num1,num2,num3]

#Print
print("In descending order:", sorted(sort, reverse=True))
 
end = input("Press ENTER to exit")
