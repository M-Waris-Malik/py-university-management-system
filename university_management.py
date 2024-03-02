def addStudent():
    stdRollNo=input("Enter RollNo of Student: ")
    stdName= input("Enter Name of Student: ")
    stdSubject=input("Enter Subject of Student: ")
    record={"RollNo":stdRollNo, "Name":stdName, "Subject":stdSubject}
    university.append(record)
    print("Student Added Successfuly!")
    print("-----------------------------")
    
def search():
     rollNo=input("Enter RollNo for Search: ") 
     isFound=False
     for i in university:  
         if rollNo==i["RollNo"]:
             isFound=True
             print("----------------------")
             print("Name of Student: ",i["Name"])
             print("Subject of Student: ",i["Subject"])
             print("------------------------")
             break
     if isFound==False:
         print()
         print("Student Not Found!")  
         print() 
         
def update():
    rollNo=input("Enter RollNo for Update: ") 
    isFound=False
    for i in university:  
         if rollNo==i["RollNo"]:
             isFound=True
             newSub=input("Enter Subject to Replace: ")
             i["Subject"]=newSub
             print("Subject Updated Successfuly!")
             print("New Subject: ",i["Subject"])
             print("------------------------")
             break
    if isFound==False:
         print()
         print("Student Not Found!")  
         print()  
         
def removeStudent():
    rollNo=input("Enter RollNo for Remove: ") 
    isFound=False
    for i in university:  
         if rollNo==i["RollNo"]:
             isFound=True
             university.remove(i)
             print("Student Removed!")
             print("------------------------")
             break
    if isFound==False:
         print()
         print("Student Not Found!")  
         print()                   
    
university=[]
while True:
    print("1.Add Student")
    print("2.Search Student")
    print("3.Update Record")
    print("4.Remove Student")
    print("0.Close")
    value=int(input("Enter Choice: "))
    print()
    
    if value==1:
        print()
        addStudent()
        print()
    
    elif value==2:
        print()
        search()
        print()
        
    elif value==3:
        print()
        update()
        print()
        
    elif value==4:
        print()
        removeStudent()
        print() 
        
    elif value==0:
        print()
        print("Good Bye!")
        print()
        break
    
    else:
        print()
        print("Invalid Input!")  
        print()     