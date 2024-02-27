import qrcode
from tkinter import *
from tkinter import messagebox

#I actually don't know much about the qrcode module stuff, I should check out the documentation
def generate():
    #Create the QRCode object of the size specified by the user
    qr = qrcode.QRCode(version = size.get(), #version parameter controls the size from 1 to 40
                       box_size = 10, #The box_size parameter controls how many pixels each “box” of the QR code is.
                       border = 5) #The border parameter controls how many boxes thick the border should be

    qr.add_data(url_text.get()) #Adding the data to be encoded to the QR Code
    qr.make(fit=True) #Makes the entire QR COde space utilized

    img = qr.make_image() #Generates the QR Code
    directory_location = location.get() + "\\" + name.get() #Location where to put saved file

    img.save(f"{directory_location}.png") #Saves the QR Code

    messagebox.showinfo("QR Code Generator","QR COde is saved.")

#Main Code
window = Tk()
window.title("QR Code Generator")
window.geometry("700x700")

#Create the content of the Window, this part is rather lengthy
header_frame = Frame(window, bd=5)
header_frame.place(relx=0.15,rely=0.05,relwidth=0.7,relheight=0.1)
header_label = Label(header_frame, text="Generate QR Code", font=('Times',20,'bold'))
header_label.place(relx=0,rely=0, relwidth=1, relheight=1)

#Taking the input of the text or URL to get QR Code
url_frame = Frame(window)
url_frame.place(relx=0.1,rely=0.15,relwidth=0.7,relheight=0.3)

url_label = Label(url_frame, text="Enter the text/URL:  ",font=('Courier',13,'bold'))
url_label.place(relx=0.05, rely=0.2, relheight=0.08)

url_text = Entry(url_frame, font=("Century 12"))
url_text.place(relx=0.05,rely=0.4, relwidth=1, relheight=0.2)

#Getting input of the location to save QR Code
location_frame = Frame(window)
location_frame.place(relx=0.1,rely=0.35,relwidth=0.7,relheight=0.3)

location_label = Label(location_frame,text="Enter the location to save the QR Code: ",font=('Courier',13,'bold'))
location_label.place(relx=0.05,rely=0.2, relheight=0.08)

location = Entry(location_frame,font=('Century 12'))
location.place(relx=0.05,rely=0.4, relwidth=1, relheight=0.2)

#Getting input of the QR Code image name
name_frame = Frame(window)
name_frame.place(relx=0.1,rely=0.55,relwidth=0.7,relheight=0.3)

name_label = Label(name_frame,text="Enter the name of the QR Code: ",font=('Courier',13,'bold'))
name_label.place(relx=0.05,rely=0.2, relheight=0.08)

name = Entry(name_frame,font=('Century 12'))
name.place(relx=0.05,rely=0.4, relwidth=1, relheight=0.2)

#Getting the input of the size of the QR Code
size_frame = Frame(window)
size_frame.place(relx=0.1,rely=0.75,relwidth=0.7,relheight=0.2)

size_label = Label(size_frame,text="Enter the size from 1 to 40 with 1 being 21x21: ",font=('Courier',13,'bold'))
size_label.place(relx=0.05,rely=0.2, relheight=0.08)

size = Entry(size_frame,font=('Century 12'))
size.place(relx=0.05,rely=0.4, relwidth=0.5, relheight=0.2)

#Button to generate and save the QR Code
button = Button(window, text='Generate Code',font=('Courier',15,'normal'),command=generate)
button.place(relx=0.35,rely=0.9, relwidth=0.25, relheight=0.05)

#Runs the window till it is closed manually
window.mainloop()