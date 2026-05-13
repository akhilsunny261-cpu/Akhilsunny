def average(l):
    sum=0
    for i in range(len(l)):
        sum+=l[i]
    return(sum/len(l))

l=list(map(int,input("enter elements").split()))
print(average(l))

