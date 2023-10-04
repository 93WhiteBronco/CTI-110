# CWM-110
# P4LAB2 - Output range with increment of 5
# name redacted
# 10/4/2023
# This program takes two integers as inputs, then prints the range inbetween them in increments of five

input_int_1 = int(input())
input_int_2 = int(input())

if input_int_1 <= input_int_2:
    print(input_int_1, end=' ')
    for i in range(input_int_1 + 5, input_int_2 + 5, 5):
        if i <= input_int_2:
            print(i, end=' ')
            
    print()
else:
    print("Second integer can't be less than the first.")
