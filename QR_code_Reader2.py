# Import Library
import cv2
import webbrowser

# read the QRCODE image
image = cv2.imread("myQR_code.png")

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
