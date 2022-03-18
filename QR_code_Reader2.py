# Import Library
import cv2
import webbrowser
from tkinter import Tk
from tkinter.filedialog import askopenfilename

# we don't want a full GUI, so keep the root window from appearing
Tk().withdraw()

# show an "Open" dialog box and return the path to the selected file
filename = askopenfilename()

# read the QRCODE image
image = cv2.imread(filename)

# initialize the cv2 QRCode detector
detector = cv2.QRCodeDetector()

# detect and decode
data, vertices_array, binary_qrcode = detector.detectAndDecode(image)

# print the data
if vertices_array is not None:
    print("QRCode data: ", data)
    # open link automatically
    webbrowser.open(data)
else:
    print("There was some error")
