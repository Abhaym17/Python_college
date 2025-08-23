#Write a Python program to work with the read and write operations on a file.
#The program should have the following functionalities:
#1. Read the content of the file
#2. Write the content to the file
#3. Append the content to the file
#4. Delete the content of the file
#5. Delete the file
import os
import shutil
#Function to read the content of the file

def read_file(number):
    match number :
        case 1:
            file_name = open("demo.txt","r") # Open the file in read mode
            context = file_name.read()
            print(context)
            file_name.close()
        case 2:
            file_name = open("demo.txt","w") # its remove old data
            get = input()
            context = file_name.write(get)
            print("Data enter succesfully")
            file_name.close()
        case 3:
            file_name = open("demo.txt","a") # Open the file in append mode
            get1 = input()
            context = file_name.write(get1)
            print("Data append succesfully")
            file_name.close()
        case 4:
            with open("demo.txt", "w") as file:
                pass 
print("1 for read \n2 for write \n3 for append \n4 for delete")
number = int(input("Enter your choice: "))
read_file(number)