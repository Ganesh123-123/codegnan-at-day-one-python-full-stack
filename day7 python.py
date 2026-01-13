# get number of students in the class
n=int(input("enter number of students in the class:"))
present_count=0
absent_count=0
rool=1# initilization
while  rollno <=n:# condition
    for rollno in range(1,n+1):
        print("enter", rollno,"is present or absent and select followinf option 1 or 2 \n 1. present \n 2. absent:")
status=input()

    #check statu
if status=='1':
    present_count +=1# increment
    rollno+
    elif status== '2':
        absent_count+=1
else:
            print("please select either 1 or 2 options")
            print("tptel student in the class:",n)
            print("number of students present:",present_count)
            print("number of students absent:",absent_count)
            percentage=(present_count/n)*100
            print("attendence report:", percentage)
