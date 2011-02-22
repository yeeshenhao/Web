#Filename: yeesh_p02_q02.py
#Author: Yee Shen Hao
#Description:
##Write a program that reads three edges for a triangle and determines whether the input is
##valid. The input is valid if the sum of any two edges is greater than the third edge. The
##program will compute the perimeter of the triangle if the input is valid. Otherwise, display
##that the input is invalid. 2 sample sessions are as follows:

# User input:
print("This is to calculate perimeter of a triangle (in metres.)")
side1 = float(input("Enter side 1: "))
side2 = float(input("Enter side 2: "))
side3 = float(input("Enter side 3: "))

perimeter = side1+side2+side3

# Check if triangle is valid, print results
if side1+side2>side3 and side3+side2>side1 and side1+side3>side2:
    print("Perimeter = ", str(perimeter), " m.")
else:
    print("Invalid triangle.")

end = input("Press ENTER to exit")
