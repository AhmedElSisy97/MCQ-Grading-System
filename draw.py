
import cv2 as cv
from tkinter import messagebox

messagebox.showinfo("Welcome!", "Tap 'R' to reset the image or tap 'Q' when finished.")

refpt = []
draw = False
Finished = False


def click_to_draw(click, x, y, flags, param):

    global refpt, draw, Finished
    if not Finished:
        if click == cv.EVENT_LBUTTONDOWN:
            refpt = [(x, y)]
            draw = True

        elif click == cv.EVENT_LBUTTONUP:
            refpt.append((x, y))
            draw = False

            cv.rectangle(image, refpt[0], refpt[1], (0, 255, 0), -1)
            cv.imshow('image', image)
    elif Finished:
        return


source = cv.imread('Test.jpg')
image = cv.resize(source, (460, 654))
clone = image.copy()
cv.namedWindow("image")
cv.setMouseCallback("image", click_to_draw)
# keep looping until the 'q' key is pressed
while True:
    cv.imshow("image", image)
    key = cv.waitKey(1000)
    # if the 'r' key is pressed, reset the cropping region
    if key == ord("r"):
        image = clone.copy()
    # if the 'c' key is pressed, break from the loop
    elif key == ord("q"):
        print('finished')
        Finished = True
        break

    cv.waitKey(0)
# close all open windows
cv.imwrite('im.jpg', image)
cv.destroyAllWindows()
mask = cv.inRange(image, (0, 245, 0), (0, 255, 0))
cv.imwrite('mask.jpg', mask)
