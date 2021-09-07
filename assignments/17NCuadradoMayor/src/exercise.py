def Square():
    return()

number = int(input("Input number: "))
i = int()

j = 1

while i <= number:
    j = j + 1
    i = j**2
    
    if i > number:
        print("Result: ", j)
