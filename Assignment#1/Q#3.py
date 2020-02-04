#Append
studentData = ["Ali Raza", 22, 91.24, "Computer Science", 5, "University of Agriculture"]
studentData.append('20 February 2019')
studentData.append(8)
print("Output1: ",studentData)
#Insert
studentData.insert(1,"Zohaib Niazi")
studentData.insert(4,25000)
print("Output2: ",studentData)
#Update Method
'''
studentData.Update("Ali")
print("Output3: ",studentData)
'''
#Remove Method
studentData.remove("Computer Science")
studentData.remove(91.24)
print("Output4: ",studentData)

len=len(studentData)
len-=1
studentData.pop(len)
print("Output5: ",studentData)


studentData.pop(3)
print("Output6: ",studentData)


