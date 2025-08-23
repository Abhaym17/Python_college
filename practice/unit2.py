try:
    file = open("1.txt","a")
    print("file is exists")
    try :
        file.write("Abhay")
    except:
        print("file was not writable")
    finally :
        file.close()
except FileNotFoundError:
    print("Something was wrong")



