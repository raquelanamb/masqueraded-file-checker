# masqueraded-file-checker
This program checks if the file extension matches the hex file signature for each file within a given folder.

The program works by checking for each file in a given folder whether the extension of the file matches with the expected hex file signature(s) within a Python dictionary that contains the file extensions as keys and the lists of possible file signatures as values.

To use:
1. Open the Python file file_signatures.py in your IDE (I used PyCharm) and run it (without any parameters).
2. A window should appear allowing you to choose a folder from your computer. Choose the folder containing the files that you would like to check for masquerading.
3. The program will print the paths of the files which may potentially be masqueraded based on a mismatch between actual extension and expected file signature.
4. The program will take into account the fact that some file extensions, such as a .txt, do not always have an associated file signature.
5. After printing out the file paths of all potentially masqueraded files from the selected folder, the program will print the total number of potentially masqueraded fles.

Please note that although the dictionary within the program contains a large number of common and rare file types, it is not an entirely comprehensive list. If the program encounters an unincluded file extension, it will output that file's path along with a message saying that this file extension was not found.
