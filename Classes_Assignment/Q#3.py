
class reverse:
    def __init__(self,str):
        self.string=str
    def rev(self):
        getS=self.string
        return ' '.join(reversed(getS.split()))
input=input("Enter any String")
rev1=reverse(input)
print(rev1.rev())