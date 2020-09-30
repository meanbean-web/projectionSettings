import keyboard
import cv2
import time


img = cv2.imread('image displays/circleGrid.png')
# key = cv2.waitKey(1) & 0xFF

#

# if key == ord('q'):


#     time.sleep(100)


while True:  # making a loop
    try:  # used try so that if user pressed other than the given key error will not be shown
        if keyboard.is_pressed('q'):  # if key 'q' is pressed

            cv2.namedWindow('image', cv2.WND_PROP_FULLSCREEN)
            cv2.setWindowProperty('image', cv2.WND_PROP_FULLSCREEN, cv2.WINDOW_FULLSCREEN)
            cv2.imshow("image", img)
            cv2.waitKey()


            print('You Pressed A Key!')
            break  # finishing the loop
    except:
        break



     #time.sleep(20)

            # status = cv2.getWindowProperty("image")
            # if status == 1:
            #     cv2.destroyAllWindows()
