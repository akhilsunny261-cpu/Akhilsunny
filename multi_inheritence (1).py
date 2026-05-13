class A :
    def displayA(this):
        print("This is class A display function")
class B(A):
    def displayB(this):
        print("This is class B display function")
class C(B):
    def displayC(this):
        print("This is class C display function")
objC=C()
objC.displayA()
objC.displayB()
objC.displayC()
