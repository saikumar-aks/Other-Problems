mail=input()
li=[]
li1=[]
for i in mail:
    if i == '@':
        break
    else:
      li.append(i)
x=len(li)
if x <= 5 and len(mail) != x:
    for i in li:
        print('*',end="")
    print(mail[x:])
    
elif len(li) > 5 and len(mail) != len(li):
    print("***"+mail[3:])

elif len(mail) == len(li):
    print("invalid input")
