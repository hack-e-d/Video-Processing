import os
import cv2
folder = 'frames_framegetter'
os.mkdir(folder)
vidcap = cv2.VideoCapture(0)
count = 0
while True:
    success,image = vidcap.read()
    cv2.imshow('Video', image)
    if cv2.waitKey(1) & 0xFF ==ord('q'):
        break
    cv2.imwrite(os.path.join(folder,"frame{:d}.jpg".format(count)), image)     # save frame as JPEG file
    count += 1
print("{} images are extacted in {}.".format(count,folder))

try:
    img  = Image.open()
except IOError:
    pass