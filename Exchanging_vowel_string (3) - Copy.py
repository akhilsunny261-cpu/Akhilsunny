#a,b,c = map(int,input('Enter 3 numbers').split())
#print(a*b*c)
#s1 = 'python programming'
#s2 = 'python'
#if s2 in s1:
#   print('found')
#else:
#    print('not found')
s =input('Enter string: ')
i = 0
j = len(s)-1
s1 = 'aeiouAEIOU'
l = list(s)
for i in range(len(s)):
    while s[i] not in s1 and i<j:
        i+=1
    while s[j] not in s1:
        j-=1
    l[i],l[j] = l[j],l[i]
    t = str(l)
print(t)