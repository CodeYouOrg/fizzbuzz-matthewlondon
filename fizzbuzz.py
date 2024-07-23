# Fizz buzz (often spelled FizzBuzz in this context) has been used as an interview screening device for computer programmers. 
# Writing a program to output the first 100 FizzBuzz numbers is a relatively trivial problem requiring little more than a loop and conditional statements. 
# However, its value in coding interviews is to analyze fundamental coding habits that may be indicative of overall coding ingenuity.

# From FizzBuzz on wikipedia.org.

# In this exercise we will implement the classic programming challenge FizzBuzz. 
# This is the Week 2 Bonus Exercise from the openSAP Learn Python course.
# If you have already solved it as part of the Learn Python course you can re-use your code here.

# Write a Python program that prints the numbers from 1 to 100. 
# If the number is dividable by 3 print Fizz. 
# If the number is dividable by 5 print Buzz instead of the number. 
# If the number is dividable by 3 and 5 print FizzBuzz instead of the number.

# Below is the output of the program for the first 15 numbers:

# 1
# 2
# Fizz
# 4
# Buzz
# Fizz
# 7
# 8
# Fizz
# Buzz
# 11
# Fizz
# 13
# 14
# FizzBuzz

# Check if remainder (modulus operator) 3 and 5 is 0, if so, number is divisible by both and print "FizzBuzz"
# follow up with individual check (3 (Fizz) then 5 (Buzz))
# Otherwise print the value of i, indivisible by 3&5, 3, or 5.

def fizzbuzz():
    for i in range(1, 101):
        if (i % 3 == 0 and i % 5 == 0):
            print("FizzBuzz")
        elif (i % 3 == 0):
            print("Fizz")
        elif (i % 5 == 0):
            print("Buzz")
        else:
            print(i)
def main():
    fizzbuzz()
main()