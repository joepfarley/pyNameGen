#Name generator. 

from random import choice


'''Beginnings'''
con=["B","C","Ch","D","F","G","Gl","H","J","K","Kh","L","M", "N", "P","R","S","Sh","St","Sl","T","Th","V","W","Z","Zh"]
vo=['Al','An','Am','As','Ap','El','En','Em','Ev','Ez','Il','In','Im','I','Iz','Iv','Ih','Ix','Ol','On','Ov','Ox','Yn', 'Yl','Ul','Un', 'Um','']
vo2=["A","E","I","O","U","Y","AA","Ie","Ei","Ae","Ou"]
'''middles'''
midsoft=["ani","ana","eni","eno","ila","ira","ini","ota","a","e","i","o","u"]
midhard=["k","kh",'c','ch','t','v','d','fah','gor','shor','b','bin','f','fin','din','shin','fron','fon','don','quin','shen','zin','zon','xin','tor','khon']

'''endings'''
end=["s","m","z","t","n","r",'']
softEnd=[]
def nameGen(len=1,start=con,mid=midsoft):
	name=[]
	name.append(choice(start))
	for i in range(0,len):
		name.append(choice(mid))
		if mid==midhard:name.append(choice(vo2))
	name.append(choice(end))
	return("".join(name).title())



li=[]
x=300
for i in range(1,x):
	li.append(nameGen(choice([1])))

	
	
names=open("names.txt",'a')
li=list(set(li))
li.sort()
print(len(li))
for i in li:
	if li.index(i)%5!=0:names.write(', ')
	if li.index(i)%5==0:names.write('\n')
	names.write(i)
