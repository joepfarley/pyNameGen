#!/usr/bin/env python3

    # web based python script to generate names
    # Copyright (C) 2014  Joseph Farley

    # This program is free software: you can redistribute it and/or modify
    # it under the terms of the GNU General Public License as published by
    # the Free Software Foundation, either version 3 of the License, or
    # (at your option) any later version.

    # This program is distributed in the hope that it will be useful,
    # but WITHOUT ANY WARRANTY; without even the implied warranty of
    # MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
    # GNU General Public License for more details.

    # You should have received a copy of the GNU General Public License
    # along with this program.  If not, see https://www.gnu.org/licenses/gpl.html




from random import choice,sample
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

print("""
<!-- 
    web based python script to generate names
    Copyright (C) 2014  Joseph Farley

    This program is free software: you can redistribute it and/or modify
    it under the terms of the GNU General Public License as published by
    the Free Software Foundation, either version 3 of the License, or
    (at your option) any later version.

    This program is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
    GNU General Public License for more details.

    You should have received a copy of the GNU General Public License
    along with this program.  If not, see https://www.gnu.org/licenses/gpl.html
    
    You can find the source at 
    https://github.com/joepfarley/pyNameGen
--> 

""")


syls1=[
["b","d","g", "p","v","w","z"],
['f','h','l','m','n','r','s','sh','th','w'],
['c','ch','j','k','kh','q','t','x'],
["a","e","i","o","u","y"],
['al','an','am','as','ap','el','en','em','ev','ez','il','in','im','iz','iv','ih','ix','ol','on','ov','ox','yn', 'yl','ul','un', 'um'],
['as','ash','es','esh','is','ish','os','osh','us','ush'],
['ana','ane','ani','ano','anu','ena','ene','ani','eno','enu','ina','ine','ini','ino','inu','ona','one','oni','ono','onu','una','une','uni','uno','unu'],
['ata','ate','ati','ato','atu','eta','ete','ati','eto','etu','ita','ite','iti','ito','itu','ota','ote','oti','oto','otu','uta','ute','uti','uto','utu'],
['ara','are','ari','aro','aru','era','ere','ari','ero','eru','ira','ire','iri','iro','iru','ora','ore','ori','oro','oru','ura','ure','uri','uro','uru'],
['as','es','is','os','us'],
['ly','ley','la','li','te','ti','ny','ney','na','ni'],
['lu','lo','to','tu','no','nu','tho','thu'],
[' ','\'','-',' ',' ','\'','-',' ',' ','\'','-',' '],
[' ','\'',' ','\'',' ','\'',' ','\'',' ','\'',' ','\''],
['cho','chu','cha','che','chi','zho','zhu','zha','zhe','zhi','sho','shu','sha','she','shi','tho','thu','tha','the','thi','pha','phe','phi','pho','phu'],
['at','et','it','ot','ut','ack','eck','ick','ock','uck','ach','ech','ich','och','uch','ak','ik','ek','ik','uk','ac','ic','ec','oc','uk'],
['ha','he','hi','ho','hu','hy','wa','wo','we','wi','wu','ba','be','bi','bo','bu','va','ve','vi','vo','vu','za','ze','zi','zo','zu','la','le','li','lo','lu'],
['1','2','3','4','5','6','7','8','9','0'],
['first', 'second', 'third', 'fourth', 'prime']
]
syls2=[
syls1[6]+syls1[7]+syls1[8],
syls1[1]+syls1[0]+syls1[2]
]
syls=syls1+syls2
def nameGen(*args):
    args=args[0]
    name=[]
    result=""
    for i in args:
        try:
            time.sleep(.0005)
            name.append(choice(syls[int(i)-1]))
        except ValueError:
            name.append(i)
        
    result=("".join(name).title())
    return(result)

def frontEnd():
    print("""
    <title>Name Generator</title>
    <h1>Name generator</h1>
    <p>
    To use this name generator reference the lest below and place the number in the text box for the type of syllable you want to use. The first number refers to the number of names that will be generated. Please keep the number to 300 or lower. You may place your own string into any box or simply leave the box blank if you don't want to use it. 
    </p>
    <form>
    <ul>
    <li>Number of names:<input type="text" id="num" size="3" value="15"></li>
    <li>Syllable one:<input type="text" id="syl1" size="3"value="6"></li>
    <li>Syllable two:<input type="text" id="syl2" size="3"value="7"></li>
    <li>Syllable three:<input type="text" id="syl3" size="3"value=" "></li>
    <li>Syllable four:<input type="text" id="syl4" size="3"value="16"></li>
    <li>Syllable five:<input type="text" id="syl5" size="3"value="14"></li>
    <li>Syllable six:<input type="text" id="syl6" size="3"value=""></li>
    </br><a href='javascript:var num = document.getElementById("num").value;var syl1 = document.getElementById("syl1").value;var syl2 = document.getElementById("syl2").value;var syl3 = document.getElementById("syl3").value;var syl4 = document.getElementById("syl4").value;var syl5 = document.getElementById("syl5").value;var syl6 = document.getElementById("syl6").value;location = ( "?" + num + "+" + syl1 + "+" + syl2 + "+" + syl3 + "+" + syl4 + "+" + syl5 + "+" + syl6);'> Generate List </a>
    </ul>
    </form><ol>
    <h2> Syllable List </h2>
    """)
    
    for i in syls:
        print("<li>")
        for i2 in sample(i,5):
            print("{0:^0} ".format(i2))
        print("</li>")
    print("</ol>")
        
def helper():
    print("""
    <title>Advanced help</title>
    <h1>Advanced Help</h1>
    <p>
    Right now this application uses interger arguments to define the name types. 
    The URL should look something like example.com/name.py?A+B+C+D+E+F
    Where each letter is an integer. Anything other than an integer will cause an error.
    </p></br>
    <ul>
    <li>A) indicates the number of names generated. please limit number to a value no greater than 300.</li>
    <li> All numbers after A are arbitrary numbers starting at 1. Each number is an index key to a list of lists. Each list is a set of letter combinations. </li>
    <li><a href='/cgi/name.py?frontEnd'> Front End </a></li>
    </ul>
    <h2>Syllable Lists</h2>
    <ol>
    """)

    for i in syls:
        print("<li>")
        for i2 in i:
            print("{0:^0} ".format(i2))
        print("</li>")
    
    print("""
    <p><ul>
    Click on the links below for various examples.
    <li><a href='/cgi/name.py?15+6+7'>Example 1 </a> </li>
    <li><a href='/cgi/name.py?15+2+8+10'>Example 2</a> </li>
    <li><a href='/cgi/name.py?15+3+4+14+3'>Example 3</a> </li>   
    <li><a href='/cgi/name.py?15+8+14+14'>Example 4</a> </li>
    <li><a href='/cgi/name.py?15+16+14+12+14+3'>Example 5</a> </li>
    <li><a href='/cgi/name.py?15+6+6+10+%20+14+14'>Example 6</a> </li>
    <li><a href='/cgi/name.py?15+10+9'>Example 7</a> </li>
    </ul></p>
    """)

try:
    if sys.argv[1] == 'help':
        helper()
except:pass

li=[]

try:
    num=int(sys.argv[1])
except IndexError:pass
except ValueError:frontEnd()

try:
    if num>300:
        print("<sub>Don't make more names than 300. Limiting to 300 names.</sub>")
        num=300
    for i in range(0,num):
        li.append(nameGen(sys.argv[2:]))
except ValueError:pass
except NameError:pass
except IndexError:frontEnd()

li=list(set(li))
li.sort()

print('<ul>')
for i in li:
    if i==li[0]:print("<title>{0:^0}</title>".format(choice(li)))
    print("<li>{0:^0}</li>".format(i))

print("""</br><sub>
<a href="javascript:location.reload(true);"> Reload list </a></br>
<a href='/cgi/name.py?frontEnd'> Home </a></br>
<a href='/cgi/name.py?help'> Advanced </a> </br>
</sub>""")
print("</ui></body>")
