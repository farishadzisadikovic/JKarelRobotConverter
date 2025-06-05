# JKarelRobotConverter
This program is a GUI application written in Python using the Tkinter library. 
It provides a graphical user interface to convert files between Jarel World files 
and Karel World files, and vice versa. 

The GUI has a label to show the selected file or directory, and four buttons:
1. Select File(s) - opens a file dialog for selecting one or more files.
2. Select Folder(s) - opens a folder dialog for selecting one or more folders.
3. Remove Selected - removes the selected files or folders from the list.
4. Clear - clearing the listbox
5. Convert - performs the file conversion on the selected files and folders.

The selected files and folders are displayed in a listbox. The listbox has a scrollbar, 
which is displayed on the right-hand side. When the Convert button is pressed, 
the program reads in each file, checks if it is a Jarel World file or a Karel World file, 
and converts it to the other format. The converted file is saved with the same 
filename but with a different extension. After the conversion, a message box is displayed to 
inform the user that the conversion was successful.

This program is currently compatible only with macOS. To properly install and access 
the application, please follow the instructions below:

# Installation:
3. After navigating to the "JKarelRobot Converter" folder run this command to create a standalone executable: pyinstaller --onefile --windowed converterGUI.py
4. Once this has been created, the application will be located in the 'dist' directory. Everything else that has been created could be erased except the application.
5. The application is now successfully installed and can be accessed from the "Applications" folder.

## Installation

To run this project locally:

1. **Clone the repository**:
   ```bash
   git clone https://github.com/farishadzisadikovic/JKarelRobotConverter.git
   ```
2. **Navigate to the project directory**:
   ```bash
   cd 
   ```
3. **Install dependencies**:
   ```bash
   npm install
   ```
4. **Start the development server**:
   ```bash
   npm run preview
   ```

## Technologies Used
