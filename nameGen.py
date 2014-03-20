#!/usr/bin/env python3

from random import choice
import cgitb
import sys
import time
cgitb.enable()


print("Content-Type: text/html;charset=utf-8")
print("")

print("""<style type="text/css"><!--/*--><![CDATA[/*><!--*/ 
    h1 { color: #9999ff; background-color: #000000 fontsize:2em;}
    body { color: #ffffff; background-color: #000000; }
    a:link { color: #0000CC; }
    p, address {margin-left: 2em;}
    span {font-size: smaller;}
    prime {color: #ff8888; background-color: #000000;}
    twin {color: #ff99ff; background-color: #000000;}
    circle {color: #ff9999; background-color: #000000;}
    ol {
    font-family:monospace;
    font-size:16;
      columns: 5;
     -gecko-colums: 5;
     -webkit-columns: 5;
     -mox-columns: 5;
        }
/*]]>*/--></style>""")

print
print("<body>")


'''Beginnings'''
con=["B","C","Ch","D","F","G","Gl","H","J","K","Kh","L","M", "N", "P","R","S","Sh","St","Sl","T","Th","V","W","Z","Zh"]
vo=['Al','An','Am','As','Ap','El','En','Em','Ev','Ez','Il','In','Im','I','Iz','Iv','Ih','Ix','Ol','On','Ov','Ox','Yn', 'Yl','Ul','Un', 'Um','']
vo2=["A","E","I","O","U","Y","AA","Ie","Ei","Ae","Ou"]
'''middles'''
midsoft=["ani","ana","eni","eno","ila","ira","ini","ota","a","e","i","o","u"]
midhard=["k","kh",'c','ch','t','v','d','fah','gor','shor','b','bin','f','fin','din','shin','fron','fon','don','quin','shen','zin','zon','xin','tor','khon']

'''endings'''
ends=["s","m","z","t","n","r",'']
softEnds=['a','e','i','o','u','y','as','es','is','os','us']
def nameGen(len=1,start=con,mid=midsoft,ending=ends):
	name=[]
	name.append(choice(start))
	for i in range(0,len):
		name.append(choice(mid))
		if mid==midhard:name.append(choice(vo2))
	name.append(choice(ending))
	return("".join(name).title())



li=[]
x=300
for i in range(1,x):
	li.append(nameGen(choice([1])))

	
	

li=list(set(li))
li.sort()
li.sort(key=len)
columns=5
print('<ol>')
for i in li:
	if li.index(i)%columns!=0:print(', ')
	if li.index(i)%columns==0:print('</br>')
	print(i)


print("</body>")
