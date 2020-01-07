import pymysql

db=pymysql.connect(host="localhost",user="root",password="",database="careall")
cursor=db.cursor()

class elder:

    def confirm_request(self,k):
        sql="SELECT Request_id FROM elder_details Where Id"+"="+k+";"
        cursor.execute(sql)
        row=list(cursor.fetchone())
        sq='SELECT Id,Name,Address,Contact FROM youth_details Where Id = "'+str(row[0])+'";'
        cursor.execute(sq)
        row1 = list(cursor.fetchone())
        print(row1)
        i=input("Press C to confirm or Press R to reject = ")
        if i=="C" or i=="c":
            sql1='UPDATE elder_details SET Request_id'+'="'+str(0)+'", Taken_care_by'+'="'+str(row[0])+ '" WHERE Id'+ '="'+ k+'";'
            cursor.execute(sql1)
            sql2='UPDATE youth_details SET Number_undertaken_elders = Number_undertaken_elders+1 Where Id '+'="'+str(row[0])+'";'
            cursor.execute(sql2)
            sql3=sql="INSERT INTO taking_care(youth_id,old_id_1) VALUES (%s, %s)"
            val=(str(row[0]),k)
            cursor.execute(sql3,val)
            db.commit()
            print("Confirmed")
        elif i=="R" or i=="r":
            sql4='UPDATE elder_details SET Request_id'+'="'+str(0)+ '" WHERE Id'+ '="'+ k+'";'
            cursor.execute(sql4)
            db.commit()
            print("Rejected")

    def login(self,n):
        sql="SELECT * FROM elder_details Where Id = "+n+";" 
        cursor.execute(sql)
        row = list(cursor.fetchone())
        print(row)
        i=input("1. To Confirm pending request \n 2. To give review \n")
        if i==1 :
            ed.confirm_request(n)
        elif i==2 :
            j=input("Enter the id of youth")
            rr.elder_review_and_rating(j)
        else:
            print("Please enter a valid response")
        
    def signup(self,i,j,l,k):
        sql="INSERT INTO elder_details(Name,Age,Fund_raised,Contact) VALUES (%s, %s,%s,%s)"
        val=(str(i),j,l,k)
        cursor.execute(sql,val)
        db.commit()
        sq="SELECT Id FROM elder_details Where Contact"+"="+str(k)+";"
        cursor.execute(sq) 
        i=list(cursor.fetchone())
        print("Signup successfull, your Login Id is ",i)

class young:
    def send_request(self,k):
        sql="SELECT * FROM elder_details Where Taken_care_by=0;"
        cursor.execute(sql)
        row = list(cursor.fetchall())
        print("Following is the list of registered Elders")
        for i in row:
            print(i)
        j=input("Enter Id of the elder to want to take care of = " )
        sq='UPDATE elder_details SET Request_id'+'="'+k+ '" WHERE Id'+ '="'+ j+'";'
        cursor.execute(sq)
        db.commit()




    def login(self,n):
        sql="SELECT * FROM youth_details Where Id = "+n+";" 
        cursor.execute(sql)
        row = list(cursor.fetchone())
        print(row)
        i=input("1. To send request to elders \n 2. To give review \n")
        if i==1 :
            yg.send_request(n)
        elif i==2 :
            j=input("Enter the id of elder")
            rr.young_review_and_rating(j)
        else:
            print("Please enter a valid response")

        
    def signup(self,i,j,l,k):
        sql="INSERT INTO youth_details(Name,Age,Address,Contact) VALUES (%s, %s,%s,%s)"
        val=(str(i),j,l,k)
        cursor.execute(sql,val)
        db.commit()
        sq="SELECT Id FROM youth_details Where Contact"+"="+str(k)+";"
        cursor.execute(sq) 
        i=list(cursor.fetchone())
        print("Signup successfull, your Login Id is ",i)
    
class review_and_rating:

    def young_review_and_rating(self,k):
        i,j=input("Enter Reviews = "),input("Enter Rating = ")
        sql='UPDATE elder_details SET Reviews'+'="'+str(i)+'", Ratings'+'="'+str(j)+ '" WHERE Id'+ '="'+ k+'";'
        cursor.execute(sql)
    def elder_review_and_rating(self,k):
        i,j=input("Enter Reviews = "),input("Enter Rating = ")
        sql='UPDATE youth_details SET Reviews'+'="'+str(i)+'", Ratings'+'="'+str(j)+ '" WHERE Id'+ '="'+ k+'";'
        cursor.execute(sql)

ed=elder()
yg=young()
rr=review_and_rating()
a=input("Please enter weather you are elder or young= ")
if a=="Elder" or a=="elder" or a=="ELDER":
    b=input("Login or Signup = ")
    if b=="login" or b=="Login" or b=="LOGIN":
        old_id=input("Enter your id i.e. 1,2...15 = ")
        ed.login(old_id)# call login funtion of class old fetch details of old from old table
    elif b=="Signup" or b=="signup" or b=="SIGNUP":
        name,age,fund_raised,contact=input("Enter name= "),int(input("Enter age where age>50 = ")),int(input("Fund raised per month in RS.= ")),int(input("Enter mobile number = "))
        ed.signup(name,age,fund_raised,contact)#call signup funtion of class old and inset details in old table
    else:
        print("Please enter a valid response")
elif a=="Young" or a=="young" or a=="YOUNG":
    b=input("Login or Signup = ")
    if b=="login" or b=="Login" or b=="LOGIN":
        young_id=input("Enter your id i.e. 1,2...15 = ")
        yg.login(young_id)# call login funtion of class young fetch details of young from young table
    elif b=="Signup" or b=="signup" or b=="SIGNUP":
        name,age,address,contact=input("Enter name = "),int(input("Enter age where 25>age<40 = ")),input("Enter your complete address = "),int(input("Enter mobile number = "))
        yg.signup(name,age,address,contact)#call signup funtion of class old youngand inset details in old table
else:
    print("Invalid Response")

