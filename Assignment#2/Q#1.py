import datetime
employee={}
employeesData=[]
degree={}
values=int(input("How many records you want to Store: "))
for i in range(values):
    employee["Name"] = input("Enter your Name: ")
    employee["Age"] = int(input("Enter your Age: "))
    employee["Work"] = input("Your Working Department: ")
    employee["Skills"] = input("Your Skills: ").split(",")
    print("Enter your Degree Details: ")
    degree["Title"]=input("Enter Degree Title: ")
    degree["Major"] = input("Enter Major: ")
    date=input("Enter Completion Date: ")
    degree["Completion Date"] =date
    employee["Degree"]=degree
    salary = input("Enter your Salary: ")
    employee["Salary"] = salary
    employeesData.append(employee)
    print("-"*50)
print(employeesData)