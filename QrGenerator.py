import qrcode

text = input("Enter your text or URL: ")
filename = input("Enter your file type: ")

def generateqr(text,filename):

    #convert text to qr code
        image_qr= qrcode.make(text)
    #save to image
        image_qr.save(filename)

generateqr(text,filename)