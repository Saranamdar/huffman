from tkinter import messagebox
from gui import show_screen
from handle_files import write_file, open_file, modify_cmp_content
from huffmanAlgorithm import encoding , decoding

if __name__ == "__main__":
    # create and show the screen
    input_file, output_directory = show_screen()
    dialog_message = 'error'
    # extract content
    content = open_file(input_file)
    # create txt from cmp if input file is encoded
    if input_file[-3:] == 'cmp':
        binary_content,char_n_dict = modify_cmp_content(content)
        # encoding
        decoded_content = decoding(binary_content,char_n_dict)
        # create and save txt file
        write_file(decoded_content,output_directory,'decoded_content.txt')
        # change dialog_message
        dialog_message = 'decode cmp to txt'
    # create cmp from text if input file is decoded
    elif input_file[-3:] == 'txt':
        # encoding
        encoded_content = encoding(content)
        # create and save cmp file
        write_file(encoded_content,output_directory,'encoded_content.cmp')

        dialog_message = 'encode txt to cmp'

    # show dialog message
    messagebox.showinfo(title='Huffman algorithm', message=dialog_message)
