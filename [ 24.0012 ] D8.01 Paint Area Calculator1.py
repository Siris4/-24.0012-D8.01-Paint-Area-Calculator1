#Write your code below this line 👇
import math

def paint_calc(height, width, cover):
    area = height * width
    m = (math.ceil(area / cover / 2) * 2)
    print(f"You'll need {m} cans of paint.")


#Below rounds UP to the nearest whole 2 number:
# rounded_num = math.ceil(num / 2) * 2

# paint_calc(test_h, test_w, coverage)


#Write your code above this line 👆
# Define a function called paint_calc() so that the code below works.

# 🚨 Don't change the code below 👇
test_h = int(input("Height of wall: "))
test_w = int(input("Width of wall: "))
coverage = 5
paint_calc(height=test_h, width=test_w, cover=coverage)