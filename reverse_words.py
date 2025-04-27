class Reverse:
    def __init__(self, s):
        self.s = s
        
    def reverse(self):
        rev = ''
        for i in (self.s):
            rev = i + rev
        print(rev)
    

a = Reverse("Laxman")
a.reverse()