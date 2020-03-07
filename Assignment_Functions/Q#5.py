def showDetails(*args,**kwargs):
    sum = 0
    max=0
    min=100
    max_key=None
    min_key=None
    print("Class Marks: ")
    for key, val in kwargs.items():
        if val<min:
            min=val
            min_key=key
        if val>max:
            max=val
            max_key=key
        print(key, ":", val)
        sum = sum + val
    percentage = (sum / 400) * 100

    print("\n\nDate ", args[2])
    print("Hello " + args[0])
    print("Course " + args[1])
    print("Total Obtained Marks: ", sum)
    print("You got Minimum Marks in ", min_key, " with Marks= ", min)
    print("You got Maximum Marks in ", max_key, " with Marks= ", max)
    print("Percentage: ", percentage)
    permit=args[3]
    if percentage>=70:
        permit=True
        print("Your are promoted to Next Class: ",permit)
    else:
        permit=False
        print("Your are not promoted to Next Class: ", args[3])


name=input("Enter your Name: ")
course=input("Enter your Class: ")
marks={}
marks["Math"]=int(input("Enter your Maths Marks "))
marks["Physics"]=int(input("Enter your Physics Marks "))
marks["Bio"]=int(input("Enter your Biology Marks "))
marks["Computer"]=int(input("Enter your Computer Marks "))
date=input("Enter Date ")
nextClass=False
showDetails(name,course,date,nextClass,**marks)
