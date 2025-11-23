Student Management Python code
#import random

print("Welcome to student management:)\n")

class Student:
    def __init__(self, name, roll_no, m1, m2):
        self.name = name
        self.roll_no = roll_no
        self.m1 = m1
        self.m2 = m2
        
    def show(self):
      
        print("Name:", self.name)
        print("Roll:", self.roll_no)
        print("Subject1:", self.m1)
        print("Subject2:", self.m2)
        print("Total:", self.m1+self.m2)
        print("-------------")

box = [Student("Al",1,80,23), Student("Bo",2,51,54)]

def menu():
    print("\nEnter your number")
    print("1... New student")
    print("2... See all")
    print("3... Search")
    print("4... Delete")
    print("5... Change info")
    print("6... Quit")

while True:
    menu()
    c=input("Your pick: ")
    if c=='1':
        print("Enter name for new student")
        name = input("Enter your name: ")
        roll_no = int(input("Enter your roll number: "))
        exist = False
        for s in box:
            if s.roll_no==roll_no:
                print("Roll no already exists,Try diff roll no number")
                exist = True
        if exist: continue
        m1 = int(input("Sub1 marks: "))
        m2 = int(input("Sub2 marks: "))
        box.append(Student(name,roll_no,m1,m2))
        print("Student name of",name,"is added")
    elif c=='2':
        if not box: print("No record of student found, First Add someone :")
        for s in box: s.show()
    elif c=='3':
        f = int(input("Roll to search: "))
        hit = False
        for s in box:
            if s.roll_no==f:
                print("Student Record Exists:")
                s.show()
                hit = True
        if not hit: print("Student Roll no does not exist")
    elif c=='4':
        g = int(input("Roll to delete: "))
        before = len(box)
        box = [s for s in box if s.roll_no != g]
        if len(box) < before:
            print("Student record deleted")
        else:
            print("Student record didn't exist")
    elif c=='5':
        h = int(input("Roll to edit: "))
        done = False
        for s in box:
            if s.roll_no==h:
                print("Previous Student record ")
                s.show()
                na = input("New name (or Enter to keep): ")
                if na: s.naam = na
                u = input("New marks for sub1? (or Enter): ")
                v = input("New marks for sub2? (or Enter): ")
                if u: s.m1 = int(u)
                if v: s.m2 = int(v)
                print("New Student Record:")
                s.show()
                done = True
        if not done:
            print("Student Roll no doesn't exist")
    elif c=='6':
        print("THANK YOU")
        break
    else:
        print("Try again")

