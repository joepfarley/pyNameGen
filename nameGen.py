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
        }
/*]]>*/--></style>""")

print
print("<body>")


syls=[
["B","C","Ch","D","F","G","Gl","H","J","K","Kh","L","M", "N", "P","R","S","Sh","St","Sl","T","Th","V","W","Z","Zh"],
['Al','An','Am','As','Ap','El','En','Em','Ev','Ez','Il','In','Im','I','Iz','Iv','Ih','Ix','Ol','On','Ov','Ox','Yn', 'Yl','Ul','Un', 'Um',''],
["A","E","I","O","U","Y","AA","Ie","Ei","Ae","Ou"],
["ani","ana","eni","eno","ila","ira","ini","ota","a","e","i","o","u"],
["k","kh",'c','ch','t','v','d','fah','gor','shor','b','bin','f','fin','din','shin','fron','fon','don','quin','shen','zin','zon','xin','tor','khon'],
["s","m","z","t","n","r",''],
['a','e','i','o','u','y','as','es','is','os','us']
]

def nameGen(length,start,mid,mid2,ending):
	name=[]
	result=""
	while len(result)<3:
	  name.append(choice(start))
	  for i in range(0,length):
		  if i%2==0:name.append(choice(mid))
		  else:name.append(choice(mid2))
	  name.append(choice(ending))
	  result=("".join(name).title())
	return(result)



li=[]
num=int(sys.argv[1])
length=int(sys.argv[2])
start=int(sys.argv[3])
mid=int(sys.argv[4])
mid2=int(sys.argv[5])
end=int(sys.argv[6])



for i in range(0,num):
	li.append(nameGen(length,syls[start],syls[mid],syls[mid2],syls[end]))



	
	

li=list(set(li))
li.sort()
li.sort(key=len)
columns=5
print('<ul>')
for i in li:
	print("<li>{0:^0}</li>".format(i))


print("</ui></body>")
