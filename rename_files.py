import os
import string

maketrans = ''.maketrans
to_remove = "0123456789"
table = maketrans("", "", to_remove)

def rename_files():
    file_list = os.listdir(r"C:\Users\Chris\Downloads\prank")
    saved_path = os.getcwd()
    print("Current Working Directory is "+saved_path)
    os.chdir(r"C:\Users\Chris\Downloads\prank")

    for file_name in file_list:
        os.rename(file_name, file_name.translate(table))
    os.chdir(saved_path)

rename_files()
