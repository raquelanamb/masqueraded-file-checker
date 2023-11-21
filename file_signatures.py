"""
Created on 11/3/23
@author: raquelana
"""

import os
import tkinter as t
from tkinter import filedialog


def main():
    # call method to check for masqueraded files in a given folder:
    list_masqueraded_files()


# determines if a single file is masqueraded:
def list_masqueraded_files():
    # counter counts masqueraded files:
    counter = 0
    # create a tkinter window:
    root_directory = t.Tk()
    # withdraw the tkinter window:
    root_directory.withdraw()
    # use tkinter file dialog box to have user select folder:
    folder_path = filedialog.askdirectory()
    # check if something actually selected:
    if folder_path is not None:
        print("The following file(s) may be masqueraded:")
        print()
        # iterate over all directories and files within the folder making
        # tuples containing (root, directories, files) throughout the hierarchy:
        for root, dirs, files in os.walk(folder_path):
            # iterate over each file in each directory traversed:
            for file in files:
                # get full file path by joining root directory path & file name:
                file_path = os.path.join(root, file)
                # call method to check if masqueraded:
                if is_file_masqueraded(file_path):
                    # if so, print path
                        print(file_path)
                        print()
                        counter += 1
        # print out a message to user if no masqueraded files were found:
        if counter == 0:
            print("No masqueraded files were found.")
        # print out a message telling user how many masqueraded files found:
        else:
            print(counter, "potentially masqueraded files were found.")
    # print out a message if the user did not actually select a file:
    else:
        print("You did not select a file.")


def is_file_masqueraded(file_path):
    # split file path into tuple with (base name, extension), and store the
    # extension (the element at index 1) as file_extension:
    file_extension = os.path.splitext(file_path)[1]
    # check if the file extension is one of the few with no file signature
    # associated:
    if file_extension in ['.csv', '.txt', '.log', '.ini', '.dat', '.cfg']:
        # tell user that file extension has no associated signature (this means
        # the file could still potentially have a different file signature
        # belonging to a different file type):
        print("(" + file_extension + " files have no hex signature necessarily "
                                     "associated with them)")
        return True
    # check if the file extension is in dictionary of matching file signatures:
    elif file_extension in file_sigs:
        # open the file in "read binary mode":
        with open(file_path, 'rb') as file:
            # read first 30 bytes of file:
            file_start = file.read(30)
            # look at each file sig associated with the extension in the dict:
            for sig in file_sigs[file_extension]:
                # check if the actual file signature and the expected file
                # signature(s) are equal:
                if sig in file_start:
                    # if not, the file is masqueraded:
                    return False
    # masqueraded if went through all expected sigs & none matched actual sig:
    return True


# dict containing file extensions as keys & respective Hex signatures as values:
file_sigs = {'.wk1': [bytes.fromhex('0000020006040600080000000000')],
             '.wk3': [bytes.fromhex('00001A000010040000000000')],
             '.wk4': [bytes.fromhex('00001A000210040000000000')],
             '.wk5': [bytes.fromhex('00001A000210040000000000')],
             '.123': [bytes.fromhex('00001A00051004')],
             '.qxd': [bytes.fromhex('00004949585052'),
                      bytes.fromhex('00004D4D585052')],
             '.psafe3': [bytes.fromhex('50575333')],
             '.pcap': [bytes.fromhex('D4C3B2A1'), bytes.fromhex('A1B2C3D4'),
                       bytes.fromhex('4D3CB2A1'), bytes.fromhex('A1B23C4D')],
             '.pcapng': [bytes.fromhex('0A0D0D0A')],
             '.rpm': [bytes.fromhex('EDABEEDB')],
             '.sqlitedb': [bytes.fromhex('53514C69746520666F726D6174203300')],
             '.sqlite': [bytes.fromhex('53514C69746520666F726D6174203300')],
             '.db': [bytes.fromhex('53514C69746520666F726D6174203300')],
             '.bin': [bytes.fromhex('53503031')],
             '.wad': [bytes.fromhex('49574144')],
             '.icns': [bytes.fromhex('69636e73')],
             '.3gp': [bytes.fromhex('667479703367')],
             '.3g2': [bytes.fromhex('667479703367')],
             '.heic': [bytes.fromhex('66747970686569'),
                       bytes.fromhex('667479706d')],
             '.avi': [bytes.fromhex('52494646')],
             '.DS_Store': [bytes.fromhex('504B0304')],
             '.z': [bytes.fromhex('1F9D'), bytes.fromhex('1FA0')],
             '.lzh': [bytes.fromhex('2D686C302D'), bytes.fromhex('2D686C352D')],
             '.bac': [bytes.fromhex('4241434B4D494B454449534B')],
             '.idx': [bytes.fromhex('494E4458')],
             '.plist': [bytes.fromhex('62706C697374')],
             '.bz2': [bytes.fromhex('425A68')],
             '.gif': [bytes.fromhex('474946383761'),
                      bytes.fromhex('474946383961')],
             '.tif': [bytes.fromhex('49492A00'), bytes.fromhex('4D4D002A')],
             '.tiff': [bytes.fromhex('49492A00'), bytes.fromhex('4D4D002A')],
             '.cr2': [bytes.fromhex('49492A00100000004352')],
             '.cin': [bytes.fromhex('802A5FD7')],
             '.nui': [bytes.fromhex('4E555255494D47'), bytes.fromhex(
                 '4E55525550414C')],
             '.nup': [bytes.fromhex('4E555255494D47'), bytes.fromhex(
                 '4E55525550414C')],
             '.dpx': [bytes.fromhex('53445058'), bytes.fromhex('58 50 44 53')],
             '.exr': [bytes.fromhex('762F3101')],
             '.bpg': [bytes.fromhex('425047FB')],
             '.jpg': [bytes.fromhex('FFD8FFE0'), bytes.fromhex('FFD8FFE1'),
                      bytes.fromhex('FFD8FFEE'), bytes.fromhex('FFD8FFDB')],
             '.jpeg': [bytes.fromhex('FFD8FFE0'), bytes.fromhex('FFD8FFE1'),
                       bytes.fromhex('FFD8FFEE'), bytes.fromhex('FFD8FFDB')],
             '.jp2': [bytes.fromhex('0000000C6A5020200D0A870A'),
                      bytes.fromhex('FF4FFF51')],
             '.j2k': [bytes.fromhex('0000000C6A5020200D0A870A'),
                      bytes.fromhex('FF4FFF51')],
             '.jpf': [bytes.fromhex('0000000C6A5020200D0A870A'),
                      bytes.fromhex('FF4FFF51')],
             '.jpm': [bytes.fromhex('0000000C6A5020200D0A870A'),
                      bytes.fromhex('FF4FFF51')],
             '.jpg2': [bytes.fromhex('0000000C6A5020200D0A870A'),
                       bytes.fromhex('FF4FFF51')],
             '.j2c': [bytes.fromhex('0000000C6A5020200D0A870A'),
                      bytes.fromhex('FF4FFF51')],
             '.jpc': [bytes.fromhex('0000000C6A5020200D0A870A'),
                      bytes.fromhex('FF4FFF51')],
             '.jpx': [bytes.fromhex('0000000C6A5020200D0A870A'),
                      bytes.fromhex('FF4FFF51')],
             '.mj2': [bytes.fromhex('0000000C6A5020200D0A870A'),
                      bytes.fromhex('FF4FFF51')],
             '.qoi': [bytes.fromhex('716f6966')],
             '.lz': [bytes.fromhex('4C5A4950')],
             '.cpio': [bytes.fromhex('303730373037')],
             '.exe': [bytes.fromhex('4D5A'), bytes.fromhex('5A4D')],
             '.dll': [bytes.fromhex('4D5A')],
             '.mui': [bytes.fromhex('4D5A')],
             '.sys': [bytes.fromhex('4D5A')],
             '.scr': [bytes.fromhex('4D5A')],
             '.cpl': [bytes.fromhex('4D5A')],
             '.ocx': [bytes.fromhex('4D5A')],
             '.ax': [bytes.fromhex('4D5A')],
             '.iec': [bytes.fromhex('4D5A')],
             '.ime': [bytes.fromhex('4D5A')],
             '.rs': [bytes.fromhex('4D5A')],
             '.tsp': [bytes.fromhex('4D5A')],
             '.fon': [bytes.fromhex('4D5A')],
             '.efi': [bytes.fromhex('4D5A')],
             '.zip': [bytes.fromhex('504B0304'), bytes.fromhex('504B0506'),
                      bytes.fromhex('504B0708')],
             '.aar': [bytes.fromhex('504B0304'), bytes.fromhex('504B0506'),
                      bytes.fromhex('504B0708')],
             '.apk': [bytes.fromhex('504B0304'), bytes.fromhex('504B0506'),
                      bytes.fromhex('504B0708')],
             '.docx': [bytes.fromhex('504B0304'), bytes.fromhex('504B0506'),
                       bytes.fromhex('504B0708')],
             '.epub': [bytes.fromhex('504B0304'), bytes.fromhex('504B0506'),
                       bytes.fromhex('504B0708')],
             '.ipa': [bytes.fromhex('504B0304'), bytes.fromhex('504B0506'),
                      bytes.fromhex('504B0708')],
             '.jar': [bytes.fromhex('504B0304'), bytes.fromhex('504B0506'),
                      bytes.fromhex('504B0708')],
             '.kmz': [bytes.fromhex('504B0304'), bytes.fromhex('504B0506'),
                      bytes.fromhex('504B0708')],
             '.maff': [bytes.fromhex('504B0304'), bytes.fromhex('504B0506'),
                       bytes.fromhex('504B0708')],
             '.msix': [bytes.fromhex('504B0304'), bytes.fromhex('504B0506'),
                       bytes.fromhex('504B0708')],
             '.odp': [bytes.fromhex('504B0304'), bytes.fromhex('504B0506'),
                      bytes.fromhex('504B0708')],
             '.ods': [bytes.fromhex('504B0304'), bytes.fromhex('504B0506'),
                      bytes.fromhex('504B0708')],
             '.odt': [bytes.fromhex('504B0304'), bytes.fromhex('504B0506'),
                      bytes.fromhex('504B0708')],
             '.pk3': [bytes.fromhex('504B0304'), bytes.fromhex('504B0506'),
                      bytes.fromhex('504B0708')],
             '.pk4': [bytes.fromhex('504B0304'), bytes.fromhex('504B0506'),
                      bytes.fromhex('504B0708')],
             '.pptx': [bytes.fromhex('504B0304'), bytes.fromhex('504B0506'),
                       bytes.fromhex('504B0708')],
             '.usdz': [bytes.fromhex('504B0304'), bytes.fromhex('504B0506'),
                       bytes.fromhex('504B0708')],
             '.vsdx': [bytes.fromhex('504B0304'), bytes.fromhex('504B0506'),
                       bytes.fromhex('504B0708')],
             '.xlsx': [bytes.fromhex('504B0304'), bytes.fromhex('504B0506'),
                       bytes.fromhex('504B0708')],
             '.xpi': [bytes.fromhex('504B0304'), bytes.fromhex('504B0506'),
                      bytes.fromhex('504B0708')],
             '.rar': [bytes.fromhex('526172211A0700'),
                      bytes.fromhex('526172211A070100')],
             '.png': [bytes.fromhex('89504E470D0A1A0A')],
             '.class': [bytes.fromhex('CAFEBABE')],
             '.ps': [bytes.fromhex('25215053')],
             '.eps': [bytes.fromhex(
                 '252150532D41646F62652D332E3020455053462D332E30'),
                 bytes.fromhex(
                     '252150532D41646F62652D332E3120455053462D332E30')],
             '.epsf': [bytes.fromhex(
                 '252150532D41646F62652D332E3020455053462D332E30'),
                 bytes.fromhex(
                     '252150532D41646F62652D332E3120455053462D332E30')],
             '.chm': [bytes.fromhex('495453460300000060000000')],
             '.pdf': [bytes.fromhex('255044462D')],
             '.asf': [bytes.fromhex('3026B2758E66CF11A6D900AA0062CE6C')],
             '.wma': [bytes.fromhex('3026B2758E66CF11A6D900AA0062CE6C')],
             '.wmv': [bytes.fromhex('3026B2758E66CF11A6D900AA0062CE6C')],
             '.psd': [bytes.fromhex('38425053')],
             '.mp3': [bytes.fromhex('FFFB'), bytes.fromhex('FFF3'),
                      bytes.fromhex('FFF2'), bytes.fromhex('494433')],
             '.bmp': [bytes.fromhex('424D')],
             '.dib': [bytes.fromhex('424D')],
             '.iso': [bytes.fromhex('4344303031')],
             '.cdi': [bytes.fromhex('4344303031')],
             '.mgw': [bytes.fromhex('6D61696E2E6273')],
             '.nes': [bytes.fromhex('4E4553')],
             '.doc': [bytes.fromhex('D0CF11E0A1B11AE1'),
                      bytes.fromhex('0D444F43')],
             '.xls': [bytes.fromhex('D0CF11E0A1B11AE1')],
             '.ppt': [bytes.fromhex('D0CF11E0A1B11AE1')],
             '.msi': [bytes.fromhex('D0CF11E0A1B11AE1')],
             '.msg': [bytes.fromhex('D0CF11E0A1B11AE1')],
             '.dex': [bytes.fromhex('6465780A30333500')],
             'vmdk': [bytes.fromhex('4B444D'),
                      bytes.fromhex('23204469736B2044657363726970746F')],
             '.crx': [bytes.fromhex('43723234')],
             '.cwk': [bytes.fromhex(
                 '05070000424F424F0507000000000000000000000001'),
                 bytes.fromhex('0607E100424F424F0607E10000000000000000000001')],
             '.toast': [bytes.fromhex('455202000000'),
                        bytes.fromhex('8B455202000000')],
             '.dmg': [bytes.fromhex('6B6F6C79')],
             '.xar': [bytes.fromhex('78617221')],
             '.gz': [bytes.fromhex('1F8B')],
             '.xz': [bytes.fromhex('FD377A585A00')],
             '.cab': [bytes.fromhex('4D534346')],
             '.flif': [bytes.fromhex('464C4946')],
             '.webm': [bytes.fromhex('1A45DFA3')],
             '.rtf': [bytes.fromhex('7B5C72746631')],
             '.mpg': [bytes.fromhex('47'), bytes.fromhex('000001BA'),
                      bytes.fromhex('000001B3')],
             '.mpeg': [bytes.fromhex('47'), bytes.fromhex('000001BA'),
                       bytes.fromhex('000001B3')],
             '.mp4': [bytes.fromhex('00000020667479706D703432'), bytes.fromhex(
                 '0000001866747970336770'), bytes.fromhex('66747970'),
                      bytes.fromhex('69736F6D'),
                      bytes.fromhex('667479704D534E56')],
             '.eml': [bytes.fromhex('52656365697665643A')],
             '.dss': [bytes.fromhex('02647373'), bytes.fromhex('03647373')],
             '.indd': [bytes.fromhex('0606EDF5D81D46E5BD31EFE7FE74B71D')],
             '.dsp': [bytes.fromhex(
                 '23204D6963726F736F667420446576656C6F7065722053747564696F')],
             '.xml': [bytes.fromhex('3C3F786D6C20'),
                      bytes.fromhex('3C003F0078006D006C0020'),
                      bytes.fromhex('003C003F0078006D006C0020'),
                      bytes.fromhex(
                          '3C0000003F000000780000006D0000006C00000020000000'),
                      bytes.fromhex(
                          '0000003C0000003F000000780000006D0000006C00000020'),
                      bytes.fromhex('4C6FA7949340')],
             '.MOV': [bytes.fromhex('00000014667479706D70343200000000'),
                      bytes.fromhex('6D6F6F76'), bytes.fromhex('66726565'),
                      bytes.fromhex('6674797071742020')],
             '.mov': [bytes.fromhex('00000014667479706D70343200000000'),
                      bytes.fromhex('6D6F6F76'), bytes.fromhex('66726565'),
                      bytes.fromhex('6674797071742020')]
             }

if __name__ == '__main__':
    main()
