import cv2
import webbrowser

# initialize the camera
cap = cv2.VideoCapture(0)

# initialize the QRCode detector
detector = cv2.QRCodeDetector()

while True:
    _, img = cap.read()
    # detect and decode
    data, vertices_array, _ = detector.detectAndDecode(img)

    # check if there is a QRCode in the image
    if vertices_array is not None:
        if data:
            # print the QR code data
            print("QR Code detected, data:", data)
            # open link automatically
            webbrowser.open(data)
            break
    # display the result
    cv2.imshow('img', img)
    # Enter q to Quit
    if cv2.waitKey(1) == ord("q"):
        break

# destroy all windows
cap.release()
cv2.destroyAllWindows()
exit(0)
