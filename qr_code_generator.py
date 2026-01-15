# Write a program to generate a QR code based on user input, such as text or a 
# URL. The QR code should be saved as an image file that can be scanned with a 
# smartphone. 
# Optional Enhancements 
# • Add options for the user to choose the color of the QR code. This will allow 
# users to generate QR codes that match their style or branding. 
# • Implement a feature that lets the user generate multiple QR codes at once by 
# providing a list of URLs or texts. Each QR code should be saved with a unique 
# filename.


# import qrcode

# count=int(input("How many QR code you want to generate ? : "))
# name=input("Enter your filename (No .png required) ")
# for i in range(count):
#     data=input("Data for generating qr code : ")
#     img=qrcode.make(data)
#     img.save(f"{name}{i}.png") 




import qrcode

count=int(input("How many QR code you want to generate ? : "))
name=input("Enter your filename (No .png required) ")

fill=input(("Enter qr color (default black)" )).strip()  or "black"   #strip remove the extra space if given in input e.g " red"=invalid color but strip convert it to "red" and make it valid
back=input(("Enter background color (default white) ")).strip() or "white"

for i in range(count):
    data=input("Data for generating qr code : ")
    
    qr=qrcode.QRCode() #it creates a structure/object which lets us control qrcode more which is not let by qrcode.make()
    qr.add_data(data)   #add data to qr code
    
    img=qr.make_image(fill_color=fill,back_color=back)
    qr.make(fit=True)
    
    img.save(f"{name}{i}.png") 
