from PIL import Image
im=Image.open("leaf.png")
print(im.format,im.size,im.mode)
image=im.convert("RGB")
message=input("enter the message you wish to hide:")
string=""
for i in message:
    string+=format(ord(i), '08b')
newstring=""
newstring=string+"11111111"
print(newstring)

r,g,b=image.split()
r_list=list(r.get_flattened_data())
g_list=list(g.get_flattened_data())
b_list=list(b.get_flattened_data())
print(r_list)#
print(g_list)#
print(b_list)#
new_r_list=[]
new_g_list=[]
new_b_list=[]
for i in r_list:
    new_r_list.append(i&254)
for i in g_list:
    new_g_list.append(i&254)
for i in b_list:
    new_b_list.append(i&254)
print(new_r_list)#
print(new_g_list)#
print(new_b_list)#
final_r_list=[]
final_g_list=[]
final_b_list=[]
for i in range(len(new_r_list)):
    if i<len(newstring):
        final_r_list.append(new_r_list[i]+int(newstring[i]))
    else:
        final_r_list.append(new_r_list[i])
for i in range(len(new_g_list)):
    if i<len(newstring):
        final_g_list.append(new_g_list[i]+int(newstring[i]))
    else:
        final_g_list.append(new_g_list[i])                                                                          
for i in range(len(new_b_list)):
    if i<len(newstring):
        final_b_list.append(new_b_list[i]+int(newstring[i]))
    else:
        final_b_list.append(new_b_list[i])
print(final_r_list)#
print(final_g_list)#
print(final_b_list)#
r.putdata(final_r_list)
g.putdata(final_g_list)
b.putdata(final_b_list)
new_im=Image.merge("RGB",(r,g,b))
new_im.save("secret.png") 
print("message hidden successfully")

