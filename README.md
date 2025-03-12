# Masqueraded File Checker

## Overview
The **Masqueraded File Checker** is a Python-based tool that detects files whose **extensions do not match their expected hex file signatures**. This can help identify **potentially masqueraded files**, which may be used to disguise malicious content or mislead users about a file’s true format.

The program works by analyzing each file in a selected folder and comparing its **actual binary signature** against a **predefined dictionary of expected signatures** for known file types.

---

## Features
- **Automatic File Scanning**: Checks every file within a selected folder for extension mismatches.
- **Signature-Based Analysis**: Uses a comprehensive dictionary of **hex signatures** for common file formats.
- **Batch Processing**: Analyzes multiple files simultaneously.
- **GUI-Based Folder Selection**: Uses Tkinter’s file dialog to allow easy folder selection.
- **Detailed Reporting**:
  - Displays all **potentially masqueraded files** with their file paths.
  - Identifies file types **without standard signatures**.
  - Outputs a **summary count** of suspicious files found.

---

## Installation
### 1. Clone the Repository
```bash
git clone https://github.com/raquelanamb/masqueraded-file-checker.git
cd masqueraded-file-checker
```

### 2. Install Dependencies
This script relies on Python's Tkinter library, which is included in most standard installations. If missing, install it manually:

Linux:
```
sudo apt install python3-tk
```

Windows/macOS:
Tkinter is pre-installed with Python, so no additional installation is required.


## Usage

1. Open the file_signatures.py script in your IDE (e.g., PyCharm) or run it from the terminal:
```
python file_signatures.py
```
2. A file selection window will appear. Choose the folder containing the files you want to check.
3. The program will analyze the files and display:
   - A list of files that may be masqueraded based on extension/signature mismatches.
   - A message noting files without standard signatures.
   - A final count of potentially suspicious files.


## Example Output

The following file(s) may be masqueraded:

/Users/Raquel/Documents/suspicious.exe
(The file extension ".exe" does not match the expected hex signature.)

/Users/Raquel/Documents/note.txt
(.txt files have no hex signature necessarily associated with them.)

2 potentially masqueraded files were found.



### If no masqueraded files are found:

No masqueraded files were found.



### If no folder is selected:

You did not select a file.
