rows = int(input("Input the # of rows wanted: "))

i = 1
while(i <= rows):
    j = 1
    if(i % 2 != 0):          
        print('#', end = ' ')
    else:
        print('%', end = ' ')
    j = j + 1
    i = i + 1
    print()
