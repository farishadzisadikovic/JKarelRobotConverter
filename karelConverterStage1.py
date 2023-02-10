"""
Faris Hadzisadikovic
2/6/2023

JKarelRobot Converter Stage 1:

This program will be able to convert a Karel world file 
to a Jarel file, and vice versa. As of right now, it will 
be working on a command line as the previous C++ version.
It will be able to identify wether it is a Karel or Jarel world file, 
but also it will be taking directories of Karel and Jarel world files.

Karel and Jarel Project Stage 2:

After a successful conversion from C++ to Python, we will have a program 
that works on a same basis as the previous version in C++. In this stage 
we will start the process of creating a GUI Desktop application.

Mars Hill University Honor Code

We, the students of Mars Hill University pledge ourselves 
to uphold integrity, honesty, and academic responsibility 
in and out of the classroom.

Mars Hill University Honor Pledge

On my honor, I have neither given nor received any academic aid 
or information that would violate the Honor Code of Mars Hill University
"""

import binascii
import sys
import os

hexdata = []
path = sys.argv[1]

for path in sys.argv:
    with open(path, 'rb') as f:
        hexdata = f.read().hex()
def isJarel():
    print("This is a Jarel world file.\n")

def isKarel():
    print("This is a Karel world file.\n")

def notKarelOrJarel():
    print("This is not a Karel world file nor a Jarel world file.\n")
    
print(hexdata, "\n")

"""
This will print out the 8 bytes that we can compare to see
if it is a Karel or a Jarel world file
"""
byteValue = hexdata[-64:-48]
print(byteValue, "\n")

#This part might be going into the writing part
if byteValue == "0e32ee4672937cf8":
    isJarel()
    convertedStr = hexdata[0:len(hexdata)-64] + "c07500c54fec2e52" + hexdata[-48]
    print(convertedStr + "\n")
    print("This is now a Karel world file.\n")
elif byteValue == "c07500c54fec2e52":
    isKarel()
    convertedStr = hexdata[0:len(hexdata)-64] + "0e32ee4672937cf8" + hexdata[-48]
    print(convertedStr + "\n")
    print("This is now a Jarel world file.\n")
else:
    notKarelOrJarel()
    



