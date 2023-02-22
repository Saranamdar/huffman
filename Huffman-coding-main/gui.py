from tkinter import Tk,filedialog,Label,Button
# ---------------------------- CONSTANTS ------------------------------- #
BLACK = "#000000"
RED = "#D80018"
GREEN = "#008402"
FONT_NAME = "Courier"
FILE_TYPES = (('All files','.*'),('text files','*.txt'))
INPUT_FILE = ''
OUTPUT_DIRECTORY = ''


def show_screen():
    # create the window
    window = Tk()
    window.title("Huffman Ciding")
    window.minsize(width=300, height=200)
    # select input file
    input_file_button = Button(text="choose input file", highlightthickness=2, command=input_file)
    input_file_button.grid(column=1,row=1,padx=100, pady=10)
    # select output directory
    output_file_button = Button(text="choose output directory", highlightthickness=2, command=output_directory)
    output_file_button.grid(column=1,row=3,padx=100, pady=10)
    # close the window and strat process
    close_screen = Button(text='start process',highlightcolor=GREEN,highlightthickness=4,command= window.destroy)
    close_screen.grid(column=1,row=5,padx=100, pady=10)
    #----------------------
    window.mainloop()
    return INPUT_FILE,OUTPUT_DIRECTORY


def input_file():
    global INPUT_FILE
    INPUT_FILE = filedialog.askopenfilename(title='choose a file', initialdir='/', filetypes=FILE_TYPES)
    # show the input file name
    title_label = Label(text=INPUT_FILE, fg=GREEN, bg=BLACK, font=(FONT_NAME, 10))
    title_label.grid(column=1, row=2)


def output_directory():
    global OUTPUT_DIRECTORY
    OUTPUT_DIRECTORY = filedialog.askdirectory(title='choose a directory')
    # show the output directory
    title_label = Label(text=OUTPUT_DIRECTORY, fg=RED, bg=BLACK, font=(FONT_NAME, 10))
    title_label.grid(column=1, row=4)

