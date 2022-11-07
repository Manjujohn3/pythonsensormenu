while True:
    print("select an option from menu")
    print("1 add ")
    print("2 view all")
    print("3 search by date")
    print("4 Exit")

    choice = int(input("Enter an option: "))

    if(choice==1):
        print("add selected")
    elif(choice==2):
        print("view selected")
    elif(choice==3):
        print("search selected")
        
    elif(choice==4):
        break