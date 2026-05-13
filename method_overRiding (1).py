'''OVER RIDING :- '''
class A:
    def display(self):
        print("this is class A")
class B(A):
   def display(self):
        print("this is class B")
objB=B()
objB.display()