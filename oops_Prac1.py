


# class Laptop:

#     def __init__(self, name, processor):
#         self.name = name
#         self.processor = processor


#     def printoutput(self):
#         print("My laptop name is : ", self.name, "and the processor is : ", self.processor) 

# laptop1 = Laptop("HP", "RYZEN5")
# laptop2 = Laptop("ASUS", "i7")

# laptop1.printoutput()
# laptop2.printoutput()
# print(laptop1)
# print(laptop2) 



# class Person:
#     def __init__(self,name,rollno):
#         self.name = name
#         self.rollno = rollno

#     def printOutput(self):
#         print("My name is :",self.name,"and roll no is :", self.rollno)


# person1=Person("Mehroj","55")
# person2=Person("Ram","33")

# person1.printOutput()
# person2.printOutput()


class Person:

    def _init_(self,name,rollNo):
        self.name = name
        self.rollNo = rollNo

    def printOutput(self):
        print("My name is :",self.name,"and roll no is :",self.rollNo)

person1 = Person("Ram","33")
person2 = Person("Mehroj","55")

person1.printOutput()
person2.printOutput()