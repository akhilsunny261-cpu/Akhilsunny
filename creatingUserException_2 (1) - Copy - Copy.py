class VoteElegibilityError(Exception):
    def __init__(self,age,msg="Age should be >=18"):
        self.age=age
        self.msg=msg
        super().__init__(self.msg)
def set_age(age):
    if(age<=18):
        raise VoteElegibilityError(age)
    else:
        print("Elegibility for Vote")
try:
    set_age(20)
except VoteElegibilityError as e:
    print(e)