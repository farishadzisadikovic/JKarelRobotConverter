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

sys.argv = sys.argv[1:]
if len(sys.argv) == 0:
    sys.exit("You need to put a file or directory.")

for path in sys.argv:
    if os.path.isdir(path):
        for dirpath, dirnames, filenames in os.walk(path):
            for filename in filenames:
                file_path = os.path.join(dirpath, filename)
                with open(file_path, 'rb') as f:
                    hexdata = f.read().hex() #this will read all the hexdata
                    
                    binStr = binascii.unhexlify(hexdata)
                    
                    """
                    This will get the 8 bytes that we can compare to see
                    if it is a Karel or a Jarel world file
                    """
                    byteValue = hexdata[-64:-48]
                    base = os.path.splitext(file_path)[0] #this will give you the base of the file name. Ex: karel1.kw , base will be: karel1

                    if byteValue == "c07500c54fec2e52": #check if it is a Karel world file
                        convertedString = hexdata[0:len(hexdata)-64] + "0e32ee4672937cf8" + hexdata[-48:]
                        os.rename(file_path, base + '.kw')
                    elif byteValue == "0e32ee4672937cf8": #check if it is a Jarel world file
                        convertedString = hexdata[0:len(hexdata)-64] + "c07500c54fec2e52" + hexdata[-48:]
                        os.rename(file_path, base + '.jw')
                    else:
                        #print("This is not a Karel world file nor a Jarel world file.\n")
                        continue

                    convert = binascii.unhexlify(convertedString)
                    
                    """
                    If it is a Karel world file make the new converted file with the extension '.jw'
                    If it is a Jarel world file make the new converted file with the extension '.kw'
                    """
                    if byteValue == "c07500c54fec2e52":
                        with open(base + ".jw", 'wb') as f:
                            f.write(convert)
                    elif byteValue == "0e32ee4672937cf8":
                        with open(base + ".kw", 'wb') as f:
                            f.write(convert)

    elif os.path.isfile(path):
        with open(path, 'rb') as f:
            hexdata = f.read().hex()
            
            binStr = binascii.unhexlify(hexdata)
            
            """
            This will get the 8 bytes that we can compare to see
            if it is a Karel or a Jarel world file
            """
            byteValue = hexdata[-64:-48]
            base = os.path.splitext(path)[0] #this will give you the base of the file name. Ex: karel1.kw , base will be: karel1

            if byteValue == "c07500c54fec2e52":
                convertedString = hexdata[0:len(hexdata)-64] + "0e32ee4672937cf8" + hexdata[-48:]
                os.rename(path, base + '.kw')
            elif byteValue == "0e32ee4672937cf8":
                convertedString = hexdata[0:len(hexdata)-64] + "c07500c54fec2e52" + hexdata[-48:]
                os.rename(path, base + '.jw')
            else:
                print(f"{path} is not a Karel world file nor a Jarel world file.")
                continue

            convert = binascii.unhexlify(convertedString)
            
            """
            If it is a Karel world file make the new converted file with the extension '.jw'
            If it is a Jarel world file make the new converted file with the extension '.kw'
            """
            if byteValue == "c07500c54fec2e52":
                with open(base + ".jw", 'wb') as f:
                    f.write(convert)
            elif byteValue == "0e32ee4672937cf8":
                with open(base + ".kw", 'wb') as f:
                    f.write(convert)

