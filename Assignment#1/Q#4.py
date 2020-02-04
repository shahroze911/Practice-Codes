employeeData = [["Ali", 35000, "Software Engineer"],
				["Talha", 55000, "Product Manager"],
				["Nasir", 79000, "Computer Engineer"],
				["Khalid", 44000, "DBA"]]
print("Employee Names")
for sal in employeeData:
    if sal[1]>50000:
        print(sal[0])
print("\n")
salSum=0
for sal in employeeData:
    salSum+=sal[1]
print("Salary Sums of all Employees: ",salSum)

for data in employeeData:
    if data[0]=="Nasir":
        data[1]=90000
        data[2]="Product Manager"
    if data[0]=="Khalid":
        data[1]=50000
print("\nUpdated List:")
print(employeeData)



