def secretcode(msg):
    lists=[]
    for i in msg:
        lists.append(format(ord(i), '08b'))
    return lists
msg=input("enter the message you wish to hide:")
ans=secretcode(msg)
print(ans)
secretcode(msg)