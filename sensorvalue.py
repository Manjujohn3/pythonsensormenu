
import mysql.connector

mydb= mysql.connector.connect(host = 'localhost' , user = 'root' , password = '' , database = 'homeautomationdb')
mycursor = mydb.cursor()
while True:
    print("select an option from menu")
    print("1 add ")
    print("2 view all")
    print("3 search by date")
    print("4 Exit")

    choice = int(input("Enter an option: "))

    if(choice==1):
        print("add selected")
        temperature = input("enter the temperature")
        humidity = input("enter the humidity")
        moisture = input("enter the moisture")
        sql = 'INSERT INTO `sensorvalue`(`temperature`, `humidity`, `moisture`, `date`) VALUES (%s,%s,%s,now())'
        data = (temperature,humidity,moisture)
        mycursor.execute(sql , data)
        mydb.commit()
        print("value inserted succesfully") 

    elif(choice==2):
        print("view selected")
    elif(choice==3):
        print("search selected")
        
    elif(choice==4):
        break