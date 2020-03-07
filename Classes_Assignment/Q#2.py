class String:
    def __init__(self,str):
        self.s1=str
    def get_String(self):
        get_s=self.s1
        return get_s
    def print_String(self):
        print_s=self.get_String()
        print(print_s.upper())
        #print(type(print_s))
s=input("Enter any String ")
ss=String(s)
ss.get_String()
ss.print_String()


