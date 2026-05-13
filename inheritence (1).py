class A :
    def displayA(this):
        print("this is class A display function")
class B(A):
    def displayB(this):
        print("This is class  B display function")
objB=B()
objB.displayA()
objB.displayB()
