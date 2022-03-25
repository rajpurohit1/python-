import qrcode
import image

qr = qrcode.QRCode (
    version = 15,
    box_size = 5,
    border = 5,
    
    
)
 

data = "https://www.youtube.com/watch?v=-3am_5jMzJ4"

qr.add_data(data)
qr.make(fit = True)
img = qr.make_image(fill = 'black',back_color = 'yellow')
img.save('test.png')