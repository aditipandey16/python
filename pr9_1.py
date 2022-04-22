f=open("poem.txt","r")
t=f.read()
if "Twinkle" in t:
    print("True")
else:
    print("False")
f.close()