mail=input()
li=[]
for i in mail:
    if i == '@':
        break
    else:
      li.append(i)
x=len(li)
exp =bool(len(mail) != x)
if x <= 5 and exp:
    for i in li:
        print('*',end="")
    print(mail[x:])

elif len(li) > 5 and exp:
    print("***"+mail[3:])

elif len(mail) == len(li):
    print("invalid input")
