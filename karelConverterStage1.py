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
sys.argv = sys.argv[1:] 
counter = 0

if len(sys.argv) == 0:
      sys.exit("You need to put a file or directory.")

for path in sys.argv:
    #if os.path.isdir(path) or os.path.isfile(path):
    with open(path, 'rb') as f:
        hexdata = f.read().hex() #this will read all the hexdata
        
        binStr = binascii.unhexlify(hexdata)
        
        fileLocation = sys.argv[counter]
        
        #print(fileLocation, "\n") #this prints out the name of the argument that is being looked at at the time
        #print(binStr, "\n")
            
        """
        This will print out the 8 bytes that we can compare to see
        if it is a Karel or a Jarel world file
        """
        byteValue = hexdata[-64:-48]
        #print(byteValue, "\n")
        #print(binascii.unhexlify(byteValue), "\n")
        
        base = os.path.splitext(fileLocation)[0]
        #print(base)
        
        if byteValue == "c07500c54fec2e52": #check if it is a Karel world file
            #print("This is a Karel world file.\n")
            convertedString = hexdata[0:len(hexdata)-64] + "0e32ee4672937cf8" + hexdata[-48:]
            #print(binascii.unhexlify(convertedString), "\n")
            #print(convertedStr + "\n")
            #print("This is now a Jarel world file.\n")
            os.rename(fileLocation, base + '.kw')
            
        elif byteValue == "0e32ee4672937cf8": #check if it is a Jarel world file
            #this is the part where it starts writing a new file with the converted string
            #print("This is a Jarel world file.\n")
            convertedString = hexdata[0:len(hexdata)-64] + "c07500c54fec2e52" + hexdata[-48:]
            #print(binascii.unhexlify(convertedString), "\n")
            #print(convertedStr + "\n")
            #print("This is now a Karel world file.\n")
            os.rename(fileLocation, base + '.jw')
        else:
            print("This is not a Karel world file nor a Jarel world file.\n")
            
        convert = binascii.unhexlify(convertedString)
        
        """
        If it is a Karel world file make the new converted file with the extension '.jw'
        """
        if byteValue == "c07500c54fec2e52": 
            with open(base + ".jw", 'wb') as f:
                f.write(convert)
        elif byteValue == "0e32ee4672937cf8":
            with open(base + ".kw", 'wb') as f:
                f.write(convert)
                
        counter += 1 #incrementation of fileName which means it is looking at eveery argument at the command line