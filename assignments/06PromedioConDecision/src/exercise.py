print("Input numbers to calculate average: ")
    
sum_ = 0
count = 0
number = 0

while number >= 0:
    number = float(input())
    if number >= 0:
        sum_ = sum_ + number
        count = count +1
    else:
        break
        
print("The average is: ", (sum_/count))
