while True:
    try:
        print("Options: ")
        print("1. Addition")
        print("2. Subtraction")
        print("3. Multiply")
        print("4. Divide")
    
        print(end="")
        userInpt = input("Selection option or type 'exit' or 'EXIT to quit program: ")

        userInpt = int(userInpt)
        if userInpt == 1:
            print("Add")
            add()
        elif userInpt == 2:
            print("Subtract")
            subtract()
        elif userInpt == 3:
            print("Multiply")
            multiply()
        elif userInpt == 4:
            print("Divide")
            divide()
        elif userInpt > 4:
            print("Enter a valid number")
    except:
        if userInpt == "exit" or userInpt == "EXIT":
            print("Exiting program...")
            break
