class Student:
    def __init__(self):
       self.avg = 0
       self.temp = 0 
       self.name = ""
       self.roll_no = 0 
       self.marks = []
    
    def get_data(self):
        self.name = input("Enter  student name:")
        self.roll_no = input("Enter roll number:")
        for i in range(1,6):
            x = int(input("Enter the marks:"))
            self.marks.append(x)
    
    def total_marks(self):
        self.temp = 0 
        for i in self.marks:
            self.temp += i
        return self.temp
    
    def avg_marks(self):
        self.avg = self.total_marks()/5
        return self.avg
    
    def grade(self):

        if self.avg_marks()>=90:
            return ("Grade A")
        elif self.avg_marks()>=75 and self.avg_marks()<90:
            return ("Grade B")
        elif self.avg_marks()>=60 and self.avg_marks()<75:
            return ("Grade C")
        elif self.avg_marks()<60:
            return ("Grade D")
    
    def display(self):
        print(f"Name is {self.name}\nRoll Numebr is {self.roll_no}\nTotal is {self.total_marks()}\nGrade is {self.grade()}")


student1 = Student()
student1.get_data()
print(student1.avg_marks())
student1.display()