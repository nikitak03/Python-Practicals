import mysql.connector
import tabulate
from datetime import date

def displayAll():    
    cur.execute("select * from students")
    res=cur.fetchall()
    print(tabulate.tabulate(res,headers=["PRN", "FIRST_NAME", "MIDDLE_NAME", "LAST_NAME", "ADDRESS", "MOBILE", "EMAIL", "DOB"]))
def dispNameAge():
    cur.execute(" select FIRST_NAME, MIDDLE_NAME ,LAST_NAME, DOB from students")
    res=cur.fetchall()
    todays_date= date.today()
    nameAge=[]
    for i in res:
        name=i[0]+' '+i[1]+' '+i[2]
        age=todays_date-i[-1]
        days=age.days//365
        nameAge.append((name,days))
    print(tabulate.tabulate(nameAge,headers=["Name","Age"]))
def addData():
    prn=input("Enter Prn:")
    FN= input("FIRST_NAME:").upper()
    MN=input("MIDDLE_NAME:").upper()
    LN=input("LAST_NAME:").upper()
    addrs=input("ADDRESS:").upper()
    MOB=input("MOBILE NO.:")
    EMAIL=input("EMAIL:").lower()
    DOB=input("DOB:")
    cur.execute("insert into students values('{}','{}','{}','{}','{}','{}','{}','{}')".format(prn,FN,MN,LN,addrs,MOB,EMAIL,DOB))
    mycon.commit()
   # res=cur.fetchall()
    print("Record Added Sucessfully")
def deldata():
    prn=input("Enter Prn: ")
    cur.execute("Delete from students where prn='{}'".format(prn))
    mycon.commit()
    #res=cur.fetchall()
    print("Record Deleted successfully")

def updatephoneemail():
    prn = input("Enter the PRN whose record is to be deleted: ")
    MOB = input("Enter new MOBILE: ")
    EMAIL = input("Enter new EMAIL: ")
    cur.execute("UPDATE students SET MOBILE='{}',EMAIL='{}' WHERE PRN='{}'".format(MOB, EMAIL, prn))
    mycon.commit()
    print("Database updated Successfully")

def addCGPA(flag):
    if flag:
        query = "ALTER TABLE STUDENTS ADD COLUMN CGPA FLOAT"
        cur.execute(query)
        mycon.commit()
        print("\n CGPA field added successfully...\n")
        cur.execute("SELECT PRN FROM STUDENTS")
        x = cur.fetchall()
        for i in x:
            prn = i[0]
            print("Enter the CGPA of PRN ", prn, end=': ')
            cgpa = float(input())
            query = "UPDATE students SET CGPA='{}' WHERE PRN='{}'".format(cgpa, prn)
            cur.execute(query)
            mycon.commit()
        return False
    else:
        print("The field CGPA already exists.")
        return True


def functions():
    print('''
            1. Display the database
            2. Display name and age of all students
            3. Add record 
            4. Delete a record
            5. Update email and Phone number
            6. Add column CGPA
            Enter any other key to exit
    ''')

if __name__ == "__main__":
    print("Welcome to DBATU Second year Computer Engineering Department")
    print("--" * 30)
    mycon = mysql.connector.connect(host="localhost", user="root", password="Nikit@", database="comp_sy")
    cur = mycon.cursor()
    global flag
    flag = False
    try:
        cur.execute("ALTER TABLE STUDENTS DROP COLUMN CGPA")
    except:
        pass
    flag = True
    if mycon.is_connected():
        functions()
        while True:
            opt = input("Select your choice(h for help): ")
            if opt == '1':
                displayAll()
            elif opt == '2':
                dispNameAge()
            elif opt == '3':
                addData()
            elif opt == '4':
                delRecord()
            elif opt == '5':
                updatePhoneEmail()
            elif opt == '6':
                flag = addCGPA(flag)
            elif opt in 'hH':
                functions()
            else:
                break
    else:
        print("Unable to connect to MySQL") 


    
    









#mycon= mysql.connector.connect(host="localhost" ,user="root", password="Nikit@", database="comp_sy")
#cur=mycon.cursor()
#dispNameAge()
#addData()
#displayAll()
#deldata()
#updatephoneemail()
#addCGPA(flag)
