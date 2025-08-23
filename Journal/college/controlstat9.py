#write a programm to control statement in a python

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print("Using 'break' statement:")
for num in numbers:
    if num == 6:
        break  
    print(num)
print("\nUsing 'continue' statement:")
for num in numbers:
    if num % 2 == 0:
        continue 
    print(num)
print("\nUsing 'pass' statement:")
for num in numbers:
    if num == 5:
        pass  
    print(num)

    