import qrcode
from PIL import Image
import cv2 as cv

#l'information qu'on stock dans le qrcode
img = qrcode.make("https://github.com/Froste0")
#on stock le qrcode sous forme d'image
img.save("qrcode.png") 


#on déchifre le code qrcode
path = ("qrcode.png")   
img = cv.imread(path)  
det = cv.QRCodeDetector()
valeur, point, qr = det.detectAndDecode(img)
print (valeur)