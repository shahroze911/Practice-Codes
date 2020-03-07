def checkValue(check,lst=[]):
    for i in lst:
        if(i==check):
            return ("Match Found")
        else:
            return ("Match not Found")

testString=input("Enter String to Find in List: ")
data = ["python", "r", "java", "pascal", "c", "javascript", "assembley", "html", "c++"]
print(checkValue(testString,data))
