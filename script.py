import os
import shutil
print("Hello there !, let give a look to the tool menu")
print("lib = library managemnet\ncalc = calculator\nlol = largest of list\nsol = smallest of list\nrev = reverse the input")
tool = str(input("Select tool : "))

if tool == "lib":
    print("1 = create/write file\n2 = create/append file\n3 = open/read file\n4 = copy file content\n5 = delete a file\n6 = entry on file list")
    func = int(input("Select function :"))
    if func == 1 or func == 2:
        name = str(input("Enter name of the file: "))
        content = str(input("Write your content : "))
        if func == 1:
            with open("files/" + name + ".txt", "w") as file:
                file.write(content)
        elif func == 2:
            with open("files/" + name + ".txt", "a") as file:
                file.write(content)
    elif func == 3:
        name = str(input("Enter name of the file: "))
        if not os.path.exists("files/" + name + ".txt"):
            print("File not found")
        else:
            with open("files/" + name + ".txt", "r") as file:
                for line in file:
                    print(line.strip())
    elif func == 4:
        old_name = str(input("Enter name of the old file: "))
        new_name = str(input("Enter name of the new file: "))
        with open("files/" + new_name + ".txt", "w") as file:
            file.write("")
            f1 = open("files/" + old_name + ".txt", "r")
            f2 = open("files/" + new_name + ".txt", "w")
            for line in f1:
                f2.write(line)
    elif func == 5:
        delname = str(input("Enter name of the file: "))
        if os.path.isfile("files/" + delname + ".txt"):
            os.remove("files/" + delname + ".txt")
        else:
            # If it fails, inform the user.
            print("Error: %s file not found" % ("files/" + delname + ".txt"))
    elif func == 6:
        fileArr = []
        nData = str(input("Enter Name of File : "))
        fileArr.append(nData)
        fileList = fileArr
        print(fileArr)
elif tool == "calc":
    num1 = int(input("Enter first number : "))
    num2 = int(input("Enter second number : "))
    print("1 = sum\n2 = minus\n3 = multiply\n4 = devide\n5 = remainder\n6 = power of")
    inp = int(input("Select operation :"))
    opCode = ""
    ans = 0
    if inp == 1:
        ans = num1 + num2
        opCode = "sum"
    elif inp == 2:
        ans = num1 - num2
        opCode = "minus"
    elif inp == 3:
        ans = num1 * num2
        opCode = "multiply"

    elif inp == 4:
        ans = num1 / num2
        opCode = "devide"
    elif inp == 5:
        ans = num1 % num2
        opCode = "modulus"
    elif inp == 6:
        ans = num1 ** num2
        opCode = "power of"

    print(opCode + " = ", ans, end="")
elif tool == "lol":
    lstl = []
    print("Enter 10 Values : ")
    for arr in range(0, 10):
        lData = int(input("Enter Numbers in list : "))
        lstl.append(lData)
        print(lstl)
        print((10 - len(lstl)), "are left to insert")
        largest = max(lstl)
    print("largest element is = ", largest)
elif tool == "sol":
    lstl = []
    print("Enter 10 Values : ")
    for arr in range(0, 10):
        lData = int(input("Enter Numbers in list : "))
        lstl.append(lData)
        print(lstl)
        print((10 - len(lstl)), "are left to insert")
        largest = min(lstl)
    print("largest element is = ", largest)
elif tool == "rev":
    print("1 = Number\n2 = String")
    revCheck = int(input("Select Option: "))
    if revCheck == 1:
        rArr = []
        for i in range(0, 5) :
            rev = int(input("Enter the number to reverse : "))
            rArr.append(rev)
            print(rArr)
        arrRev = list(reversed(rArr))
        print(arrRev)
