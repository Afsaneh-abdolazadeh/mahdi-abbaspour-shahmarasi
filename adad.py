#a=input("Enter tool:")
#a=int(a)
#b=input("Enter arz:")
#b=int(b)
#masahat=(a*b)
#mohit=(a+b)*2
#print("Masahat:",masahat)
#print("mohit:",mohit)


'''tool=input("Enter tool:")
tool=int(tool)
arz=input("Enter araz:")
arz=int(arz)
shoa_Dayereh=(tool)/2
mohasebe_Dayereh=(shoa_Dayereh*shoa_Dayereh)*3.14
print("mohasebe_Dayereh:",mohasebe_Dayereh)'''

'''a=input("Enter a:")
a=int(a)
if(a>0):
    print('Mosbat')
else:
    print('Manfi')'''

'''a=input("Enter a:")
a=int(a)
if(a%2==0):
    print('zoj')
else:
    print('fard')'''


''' for i in range (100,999,2):
    print(i) '''

'''m=input("Enter m:")
m=int(m)
s=0
for i in range(m):
    a=input('Enter a:')
    a=int(a)
    s=s+a
print(s)
print(s/m)'''

m=input("Enter m:")
m=int(m)
s=0
max=-9999999999999
min=9999999999999
for i in range(m):
    a=input('Enter a:')
    a=int(a)
    if a>max:
        max=a
    if a<min:
        min=a
s=max+min
print(s,max,min,s/2)





