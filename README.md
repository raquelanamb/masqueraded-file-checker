# masqueraded-file-checker
This program checks if the file extension matches the hex file signature for each file within a given folder.

To use:
1. Run the program file_signatures.py.
2. A window should appear allowing you to choose a folder from your computer. Choose the folder containing the files that you would like to check for masquerading.
3. The program will print the paths of the files which may potentially be masqueraded baased on a mismatch between actual extension and expected file signature.
4. The program will take into account the fact that some file extensions, such as a .txt, do not always have an associated file signature.
5. After printing out the file paths of all potentially masqueraded files from the selected folder, the program will print the total number of potentially masqueraded fles.

Please note that although the Python dictionary within the program contains a large number of common and rare file types, it is not an entirely comprehensive list. If the program encounters an unincluded file extension, it will output that file's path along with a message saying that this file extension was not found.
