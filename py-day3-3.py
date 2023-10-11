'''#write a program to check the whether student is pass or fail
sno,sname,group,s1,s2,s3
pass constraint,marks should greater than or equal to 40,
if the condition is true,then print pass otherwise print fail
s1>=40
s2>=40
s3>=40'''
sno=int(input("Enter student no:"))
sname=input("Enter student name:")
s1=int(input("Enter sub1 marks:"))
s2=int(input("Enter sub2 marks:"))
s3=int(input("Enter sub3 marks:"))
if(s1>=40 and s2>=40 and s3>=40):
    print("Pass")
else:
    print("Fail")

