import mysql.connector
mydb=mysql.connector.connect(host="localhost",user="root",passwd="ROOT",database="HOSPITAL")
mycursor=mydb.cursor()


#function for adding new record to employee
def newrecemp():
    choice='y'
    while choice=='y':
        empid=input("Enter employee ID:")
        lname=input("Enter last name:")
        fname=input("Enter first name:")
        title=input("Enter title:")
        titofcourt=input("Enter title of courtesy(Mr.,Ms.,Mrs.,Dr.):")
        bdate=input("Enter birth date(YYYY-MM-DD):")
        hdate=input("Enter hire date(YYYY-MM-DD):")
        address=input("Enter address:")
        mycursor.execute("INSERT INTO EMPLOYEE(EmployeeID,LastName,FirstName,Title,TitleOfCourtesy,BirthDate,HireDate,Address) VALUES(%s,%s,%s,%s,%s,%s,%s,%s)",(empid,lname,fname,title,titofcourt,bdate,hdate,address))
        choice=input("Do you wish to add another record(y/n)?:")
    mydb.commit()


#function for updating record to employee
def updateemp():
    print("1.EmpID     2.LastName     3.FirstName     4.Title     5.TitleOfCourtesy     6.BirthDate     7.HireDate     8.Address")
    choice='y'
    while choice=='y':
        ch=input("Which field do you wish to update?:")
        empid=int(input("Enter empID of record to be updated:"))
        if ch=='1':
            new=input("Enter new value:")
            query="UPDATE EMPLOYEE SET EmployeeID=%s WHERE EmployeeID=%s"
            data=(new,empid)
            mycursor.execute(query,data)
        if ch=='2':
            new=input("Enter new value:")
            query="UPDATE EMPLOYEE SET LastName=%s WHERE EmployeeID=%s"
            data=(new,empid)
            mycursor.execute(query,data)
        if ch=='3':
            new=input("Enter new value:")
            query="UPDATE EMPLOYEE SET FirstName=%s WHERE EmployeeID=%s"
            data=(new,empid)
            mycursor.execute(query,data)
        if ch=='4':
            new=input("Enter new value:")
            query="UPDATE EMPLOYEE SET Title=%s WHERE EmployeeID=%s"
            data=(new,empid)
            mycursor.execute(query,data)
        if ch=='5':
            new=input("Enter new value:")
            query="UPDATE EMPLOYEE SET TitleOfCourtesy=%s WHERE EmployeeID=%s"
            data=(new,empid)
        if ch=='6':
            new=input("Enter new value:")
            query="UPDATE EMPLOYEE SET BirthDate=%s WHERE EmployeeID=%s"
            data=(new,empid)
            mycursor.execute(query,data)
        if ch=='7':
            new=input("Enter new value:")
            query="UPDATE EMPLOYEE SET HireDate=%s WHERE EmployeeID=%s"
            data=(new,empid)
            mycursor.execute(query,data)
        if ch=='8':
            new=input("Enter new value:")
            query="UPDATE EMPLOYEE SET Address=%s WHERE EmployeeID=%s"
            data=(new,empid)
            mycursor.execute(query,data)
        mydb.commit()
        choice=input("Do you wish to update another record(y/n)?:")


#function for searching record in employee
def searchemp():
    choice='y'
    while choice=='y':
        empID=int(input("Enter employeeID of record to be searched:"))
        query="SELECT * FROM EMPLOYEE WHERE EmployeeID=%s"
        data=(empID,)
        mycursor.execute(query,data)
        cont=mycursor.fetchall()
        x=cont[0]
        empid,lname,fname,tit,titoco,bdate,hdate,address=x
        newh=str(hdate)
        newb=str(bdate)
        print("{:<17} {:<17}".format("EmpID",empid))
        print("{:<17} {:<17}".format("LastName",lname))
        print("{:<17} {:<17}".format("FirstName",fname))
        print("{:<17} {:<17}".format("Title",tit))
        print("{:<17} {:<17}".format("TitleofCourtesy",titoco))
        print("{:<17} {:<17}".format("BirthDate",newb))
        print("{:<17} {:<17}".format("HireDate",newh))
        print("{:<17} {:<17}".format("Address",address))
        choice=input("Do you wish to search another record(y/n)?:")


#function for deleting record in employee
def deleteemp():
    choice='y'
    while choice=='y':
        empID=int(input("Enter employeeID of record to be deleted:"))
        mycursor.execute("DELETE FROM EMPLOYEE WHERE EmployeeID=%s",(empID,))
        mydb.commit()
        choice=input("Do you wish to delete another record(y/n)?:")

def createtablepatient():
    mycursor.execute("CREATE TABLE patient(admisno int(35),name varchar(50),age int(3),date varchar(15),phno int,bg varchar(5))")


#function for adding new patients
def add_patient():
    name_of_new_patient = input("[+]ENTER THE NAME OF THE PATIENT:")
    age_of_patient = input("[+]ENTER THE AGE OF PATIENT:")
    dob_of_patient = input("[+]ENTER THE DATE OF BIRTH OF PATIENT(YYYY-MM-DD):")
    phno = input("[+]ENTER THE PHONE NUMBER :")
    bg = input("[+]ENTER THE BLOOD GROUP OF THE PATIENT:")
    admission_no=input("[+]ENTER THE ADMISSION NUMBER:")
    mycursor.execute("INSERT INTO patient(admisno,name,age,date,phno,bg) VALUES(%s,%s,%s,%s,%s,%s)",(admission_no,name_of_new_patient,age_of_patient,dob_of_patient,phno,bg))
    mydb.commit()
    print("SUCCESSFULLY ADDED NEW PATIENT.")

#funtion to search for a patient's details
def search_patient_details():
    admission_number = int(input("ENTER THE ADMISSION NUMBER:"))
    try:
        mycursor.execute("SELECT * FROM PATIENT WHERE admisno=%s",(admission_number,))
        result =mycursor.fetchone()
        admno,name,age,date,phno,bg=result
        print("{:<17} {:<17}".format("AdmNo",admno))
        print("{:<17} {:<17}".format("Name",name))
        print("{:<17} {:<17}".format("Age",age))
        print("{:<17} {:<17}".format("Date",date))
        print("{:<17} {:<17}".format("Phoneno",phno))
        print("{:<17} {:<17}".format("BloodG",bg))
    except:
        print("SORRY WE WERE UNABLE TO FIND THE PATIENT😔")

#function to delete a patient's details
def delete_patient_details():
    admission_num = int(input("PLEASE ENTER THE ADMISSION NUMBER:"))
    try:
        mycursor.execute("DELETE FROM patient WHERE admisno=%s",(admission_num,))
        mydb.commit()
        print("RECORD HAS BEEN DELETED SUCCESSFULLY")
    except:
        print("SORRY WE WERE UNABLE TO FIND THE PATIENT😔")

#function to update phone number, date of birth, name, year of admission
def update_patient_details():
    print("1.PHONE NUMBER 2.DATE OF BIRTH 3.NAME OF PATIENT 4.AGE 5.BLOOD GROUP")
    update_choice = int(input("[+]ENTER THE FIELD TO BE UPDATED:"))
    admission_num = input("[+]PLEASE ENTER THE ADMISSION NUMBER:")
    if update_choice == 1:
        new= input("[o]ENTER THE NEW VALUE:")
        mycursor.execute("UPDATE patient SET phno=%s WHERE admisno=%s",(new,admission_num))
    elif update_choice == 2:
        new= input("[o]ENTER THE NEW VALUE:")
        mycursor.execute("UPDATE patient SET date=%s WHERE admisno=%s",(new,admission_num))
    elif update_choice == 3:
        new= input("[o]ENTER THE NEW VALUE:")
        mycursor.execute("UPDATE patient SET name=%s WHERE admisno=%s",(new,admission_num))
    elif update_choice == 4:
        new= input("[o]ENTER THE NEW VALUE:")
        mycursor.execute("UPDATE patient SET age=%s WHERE admisno=%s",(new,admission_num))
    elif update_choice == 5:
        new= input("[o]ENTER THE NEW VALUE:")
        mycursor.execute("UPDATE patient SET bg=%s WHERE admisno=%s",(new,admission_num))
    else:
        print("[-]SORRY FIELD NOT FOUND")
    mydb.commit()





def mainmenu():
    user=input("Enter username:")
    passwd=input("Enter password:")
    check='n'
    if user=='admin':
        while check=='n':
            if passwd=='password':
                check='y'
                choice=int(input("Do you wish to access 1.Employee details OR 2.Patient details ?:"))
                #choosing option of employee details
                if choice==1:
                    cho='n'
                    print("EMPLOYEE MENU")
                    while cho!='y':
                        print("1.Add record     2.Update record     3.Search record     4.Delete record")
                        ch=int(input("Enter a choice:"))
                        if ch==1:
                            newrecemp()
                        if ch==2:
                            updateemp()
                        if ch==3:
                            searchemp()
                        if ch==4:
                            deleteemp()
                        cho=input("Do you wish to exit main menu(y/n)?:")
                #choosing option of patient details
                elif choice==2:
                    cho='n'
                    print("PATIENT MENU")
                    while cho!='y':
                        print("1.Add record     2.Update record     3.Search record     4.Delete record")
                        ch=int(input("Enter a choice:"))
                        if ch==1:
                            add_patient()
                        if ch==2:
                            update_patient_details()
                        if ch==3:
                            search_patient_details()
                        if ch==4:
                            delete_patient_details()
                        cho=input("Do you wish to exit main menu(y/n)?:")
            else:
                print("PASSWORD IS INCORRECT! TRY AGAIN!")
                passwd=input("Enter password:")
                

mainmenu()




        

    



            
    
