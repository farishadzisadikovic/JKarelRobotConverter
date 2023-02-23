"""
Faris Hadzisadikovic
2/17/2023

JKarelRobot Converter:

This program is a GUI application written in Python using the Tkinter library. 
It provides a graphical user interface to convert files between Jarel World files 
and Karel World files. 

The GUI has a label to show the selected file or directory, and four buttons:
1. Select File(s) - opens a file dialog for selecting one or more files.
2. Select Folder(s) - opens a folder dialog for selecting one or more folders.
3. Remove Selected - removes the selected files or folders from the list.
4. Convert - performs the file conversion on the selected files and folders.

The selected files and folders are displayed in a listbox. The listbox has a scrollbar, 
which is displayed on the right-hand side. When the Convert button is pressed, 
the program reads in each file, checks if it is a Jarel World file or a Karel World file, 
and converts it to the other format. The converted file is saved with the same 
filename but with a different extension. After the conversion, a message box is displayed to 
inform the user that the conversion was successful.


Mars Hill University Honor Code

We, the students of Mars Hill University pledge ourselves 
to uphold integrity, honesty, and academic responsibility 
in and out of the classroom.

Mars Hill University Honor Pledge

On my honor, I have neither given nor received any academic aid 
or information that would violate the Honor Code of Mars Hill University
"""

import binascii
import os
import tkinter as tk
from tkinter import filedialog
from tkinter import messagebox
from PIL import Image, ImageTk

class App:
    def __init__(self, master):
        self.master = master
        self.master.title("JKarelRobot - Converter")
        self.master.geometry("700x400")
        self.master.minsize(700, 400)
        self.master.config(bg="#3b5998")
          
        # Create a label to display the logo image    
        self.image = Image.open("/Users/faris_hadzisadikovic/Desktop/seniorProject/JKarelRobotConverter/desktopIcon.jpeg")  
        
        # Resizing the image
        width, height = self.image.size
        newWidth = 150
        newHeight = int(height * newWidth / width)
        self.image = self.image.resize((newWidth, newHeight))
        
        self.photo = ImageTk.PhotoImage(self.image)
        self.imageLabel = tk.Label(self.master, image=self.photo)
        self.imageLabel.pack(side="top", padx=5, pady=10)

        # Create a frame to hold the buttons
        self.buttonFrame = tk.Frame(self.master, bg="#3b5998")
        self.buttonFrame.pack(side="bottom", padx=20, pady=10, fill="x")

        # Create a button to select files
        self.selectFileButton = tk.Button(self.buttonFrame, text="Select File(s)", font=("Facebook", 12), bg="white", width=6, command=self.selectFiles)
        self.selectFileButton.pack(side="left", padx=5, pady=5, ipadx=20, ipady=5)

        # Create a button to select folders
        self.selectFolderButton = tk.Button(self.buttonFrame, text="Select Folder(s)", font=("Facebook", 12), bg="white", width=6, command=self.selectFolders)
        self.selectFolderButton.pack(side="left", padx=5, pady=5, ipadx=20, ipady=5)
        
        # Create a button to remove selected files and folders
        self.removeButton = tk.Button(self.buttonFrame, text="Remove Selected", font=("Facebook", 12), bg="white", width=6, command=self.removeSelected)
        self.removeButton.pack(side="left", padx=5, pady=5, ipadx=20, ipady=5)
        
        # Create a button to clear the listbox
        self.clearButton = tk.Button(self.buttonFrame, text="Clear", font=("Facebook", 12), bg="white", width=6, command=self.clearListbox)
        self.clearButton.pack(side="left", padx=5, pady=5, ipadx=20, ipady=5)
        
        # Create a button to start the conversion
        self.convertButton = tk.Button(self.buttonFrame, text="Convert", font=("Facebook", 12), bg="white", width=6, command=self.convert)
        self.convertButton.pack(side="right", padx=5, pady=5, ipadx=20, ipady=5)
        
        # Create a listbox to display the selected files
        self.fileListbox = tk.Listbox(self.master, font=("Facebook", 12))
        self.fileListbox.pack(pady=20,padx=20, fill = "both", expand=True)
        
        # Create a scrollbar for the listbox
        self.scrollbar = tk.Scrollbar(self.fileListbox, orient="vertical")
        self.scrollbar.pack(side="right", fill="y")
        self.fileListbox.config(yscrollcommand=self.scrollbar.set)
        self.scrollbar.config(command=self.fileListbox.yview)

        self.paths = []

    def selectFiles(self):
        paths = filedialog.askopenfilenames(initialdir="/", title="Select file(s)", filetypes=[("All Files", "*.*")])
        self.paths.extend(paths)
        self.updateFileListbox()

    def selectFolders(self):
        folderPath = filedialog.askdirectory(initialdir="/", title="Select folder(s)")
        self.paths.append(folderPath)
        self.updateFileListbox()

    def updateFileListbox(self):
        self.fileListbox.delete(0, tk.END)
        for path in self.paths:
            self.fileListbox.insert(tk.END, path)
            
    def removeSelected(self):
        selection = self.fileListbox.curselection()
        if selection:
            index = selection[0]
            self.fileListbox.delete(index)
            self.paths.pop(index)
            
    def clearListbox(self):
        self.paths.clear()
        self.fileListbox.delete(0, tk.END)

    def convert(self):
        if not self.paths:
            return

        # clear the listbox
        self.fileListbox.delete(0, tk.END)
        
        files_to_convert = []

        for path in self.paths:
            if os.path.isdir(path):
                for dirpath, dirnames, filenames in os.walk(path):
                    for filename in filenames:
                        filePath = os.path.join(dirpath, filename)
                        filesToConvert.append(filePath)
            elif os.path.isfile(path):
                filesToConvert.append(path)
            else:
                print("Invalid file or directory")

        for filePath in filesToConvert:
            self.convertFile(filePath)
        
    def convertFile(self, filePath):
        with open(filePath, 'rb') as f:
            hexdata = f.read().hex()
            binStr = binascii.unhexlify(hexdata)
            byteValue = hexdata[-64:-48]
            base = os.path.splitext(filePath)[0]

            if byteValue == "c07500c54fec2e52":
                convertedString = hexdata[0:len(hexdata)-64] + "0e32ee4672937cf8" + hexdata[-48:]
                os.rename(filePath, base + '.kw')
            elif byteValue == "0e32ee4672937cf8":
                convertedString = hexdata[0:len(hexdata)-64] + "c07500c54fec2e52" + hexdata[-48:]
                os.rename(file_Path, base + '.jw')
            else:
                # print(f"{file_path} is not a Karel world file nor a Jarel world file.")
                return

            convert = binascii.unhexlify(convertedString)

            if byteValue == "c07500c54fec2e52":
                with open(base + ".jw", 'wb') as f:
                    f.write(convert)
            elif byteValue == "0e32ee4672937cf8":
                with open(base + ".kw", 'wb') as f:
                    f.write(convert)
            
            # Show a warning message box
            messagebox.showinfo("Conversion Successful", f"{os.path.basename(filePath)} has been converted successfully!")


root = tk.Tk()
app = App(root)
root.mainloop()