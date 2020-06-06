import pytesseract
import cv2 as cv


pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'


def scan():
    input_img = cv.imread('test.jpg',1)
  
    result=pytesseract.image_to_string(input_img)
        
    text=""
    for i in result:
        if (ord(i)>=48 and ord(i)<=57) or (ord(i)>=65 and ord(i)<=90) or (ord(i)>=97 and ord(i)<=122):
            text+=i
            print(i,end='')
    return text
    


#scan()

