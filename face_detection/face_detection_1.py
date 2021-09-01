# import dlib

# img = dlib.load_rgb_image("D:/Project series/AI/3DModel/me.jpg")
# win = dlib.image_window(img)

# detector = dlib.get_frontal_face_detector()
# face = detector(img)

# win.add_overlay(face)

# win.wait_until_closed()

import dlib

img = dlib.load_rgb_image("/multiple.jpg")
win = dlib.image_window(img)

detector = dlib.get_frontal_face_detector()
face = detector(img, 1)

win.add_overlay(face)

win.wait_until_closed()