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
    h2 { color: #9999ff; background-color: #000000 fontsize:1.8em;}
    body { color: #ffffff; background-color: #000000; }
    a:link { color: #CC00CC; }
    p, address {margin-left: 2em;}
    span {font-size: smaller;}
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
["s","m","z","t","n","r"],
['a','e','i','o','u','y','as','es','is','os','us'],
[' ','\'','-',' '],
[' ','\''],
[' '],
['cho','chu','cha','che','chi','zho','zhu','zha','zhe','zhi','sho','shu','sha','she','shi','tho','thu','tha','the','thi','pha','phe','phi','pho','phu'],
['at','et','it','ot','ut','ack','eck','ick','ock','uck','ach','ech','ich','och','uch','ak','ik','ek','ik','uk','ac','ic','ec','oc','uk'],
['ha','he','hi','ho','hu','hy','wa','wo','we','wi','wu','ba','be','bi','bo','bu','va','ve','vi','vo','vu','za','ze','zi','zo','zu','la','le','li','lo','lu']
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

	
def helper():
	print("""
	<h1>Help</h1>
	<p>
	Right now this application uses interger arguments to define the name types. 
	The URL should look something like example.com/name.py?A+B+C+D+E+F
	Where each letter is an integer. Anything other than an integer will cause an error.
	</p></br>
	<ul>
	<li>A) indicates the number of names generated. please limit number to a value no greater than 300.</li>
	<li>B) indicates the number of letter units. A larger number indicates a longer word but isn't directly related to syllables. Generally 4 is the largest you'll need to use.</li>
	<li> The next four are arbitrary numbers starting at 1. Each number is an index key to a list of lists. Each list is a set of letter combinations. </li>
	<li>C) This represents the first letter combintaion selected. </li>
	<li>D) This is always the second letter combination and every even set thereafter</li>
	<li>E) This is always the third letter combination and every even odd thereafter </li>
	<li>F) This represents the last letter combination</li>
	</ul>
	<h2> lists</h2>
	<ol>
	""")

	for i in syls:
		print("<li>{0:^0}</li>".format(i))
	
	print("""
	<p><ul>
	Click on the links below for various examples. Take the cultural references with a grain of salt, since this is randomly generated and I'm no expert on lingustics. 
	<li><a href='/cgi/name.py?15+1+1+4+5+4'>Asian</a> </li>
	<li><a href='/cgi/name.py?15+1+1+4+5+7'>Greek (short)</a> </li>
	<li><a href='/cgi/name.py?15+2+1+4+5+7'>Greek (medium)</a> </li>
	<li><a href='/cgi/name.py?15+3+1+4+5+7'>Greek (long)</a> </li>
	<li><a href='/cgi/name.py?15+4+1+4+5+7'>Greek (super long)</a> </li>
	<li><a href='/cgi/name.py?15+2+1+3+5+6'>Harsh</a> </li>
	<li><a href='/cgi/name.py?15+3+1+3+5+6'>Harsh (long)</a> </li>
	<li><a href='/cgi/name.py?15+1+4+5+4+7'>Flowing start with vowels</a> </li>
	<li><a href='/cgi/name.py?15+1+3+11+5+11'>Japanese </a> </li>
	<li><a href='/cgi/name.py?15+3+11+11+8+2'>Aztec</a> </li>
	<li><a href='/cgi/name.py?15+3+4+11+8+2'>Orc Tribal</a> </li>
	</ul></p>
	""")
	

if sys.argv[1] == 'help':
	helper()

li=[]
try:
	num=int(sys.argv[1])
	length=int(sys.argv[2])
	start=int(sys.argv[3])-1
	mid=int(sys.argv[4])-1
	mid2=int(sys.argv[5])-1
	end=int(sys.argv[6])-1
except:pass


	
try:
	if num>300:
	    print("<sub>Don't make more names than 300. Limiting to 300 names.</sub>")
	    num=300
	if length>16:
	    print("<sub>Don't make more names longer than 16. Limiting length to 16.</sub>")
	    length=13
	for i in range(0,num):
		li.append(nameGen(length,syls[start],syls[mid],syls[mid2],syls[end]))
except ValueError:pass
except NameError:pass
except IndexError:helper()





li=list(set(li))
li.sort()
columns=5


print('<ul>')
for i in li:
	print("<li>{0:^0}</li>".format(i))

print("""</br><sub>Click here for some <a href='/cgi/name.py?help'> help. </a></sub> """)
print("</ui></body>")
