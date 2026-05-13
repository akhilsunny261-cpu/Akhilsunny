fp = open("abc.txt","r")
content=fp.read()
print(content)


fp=open("abc.txt","w")
fp.write("sansh")
fp.close()


fp=open("abc.txt","a")
fp.write("this is file demonstartion in sansh")
fp.close()


fp=open("abc.txt","r")
print(fp.readlines())
fp.close()
