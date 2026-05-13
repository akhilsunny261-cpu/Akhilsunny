fp=open("abc.txt","w")
fp.write("python programming")
fp.close()
fp=open("abc.txt","r")
print(fp.read())
fp.close()
fp=open("abc.txt","a")

fp.write("python is easy to learn")
fp.close()

fb=open("abc.txt","r")
print(fb.read())
fb.close()