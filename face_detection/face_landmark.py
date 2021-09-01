import dlib

img = dlib.load_rgb_image("/me.jpg")
win = dlib.image_window(img, "Image")

detector = dlib.get_frontal_face_detector()
faces = detector(img)
win.add_overlay(faces)

predictor = dlib.shape_predictor("D:/Project series/AI/3DModel/shape_predictor_68_face_landmarks.dat")

for face in faces:
    landmarks = predictor(img, face)
    win.add_overlay(landmarks)

win.wait_until_closed()