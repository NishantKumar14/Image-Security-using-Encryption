from tkinter import *
from tkinter import filedialog

root = Tk()  # Creating tkinter dialog box
root.title('My App')  # Name the Dialog box title
root.geometry("400x260")  # Size of Dialog box
root.configure(bg='#D9D9D6')  # Background color of Dialog box


# Taking file for encrypting and decrypting from the local source
def encrypt_image():
    # Opening file in jpg, jpeg or png format
    file1 = filedialog.askopenfile(mode='r', filetypes=[('jpg', '*.jpg'), ('jpeg', '*.jpeg'), ('png', '*.png')])
    if file1 is not None:
        # print(file1) # -> For checking
        file_name = file1.name
        # print(file_name) # -> For checking
        key = entry1.get(1.0, END)
        print(file_name, key)

        specific_file = open(file_name, 'rb')  # Selecting file which we have to encrypt and decrypt
        image = specific_file.read()  # Reading selected file
        specific_file.close()

        image = bytearray(image)
        # XOR
        for index, value in enumerate(image):
            image[index] = value ^ int(key)
        file = open(file_name, 'wb')
        file.write(image)
        file.close()


'''In the button giving name with color and border. At same time defining the encrypt_image by the command option,  
which sets the function or method to be called when the button is clicked'''

b1 = Button(root, border=5, text="Encrypt/Decrypt", width=13, bg='#f5f5f5', fg='black', command=encrypt_image)
b1.place(x=145, y=60)

entry1 = Text(root, height=1, width=15)
entry1.place(x=135, y=95)

root.mainloop()
