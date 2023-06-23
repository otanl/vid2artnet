import cv2
import time
from stupidArtnet import StupidArtnet

TARGET_IP = '127.0.0.1'  # typically in 2.x or 10.x range

# open the video (HAP format is recommended.)
cap = cv2.VideoCapture('test.mov')

# get the video dimensions and frame rate
frame_width = int(cap.get(3))
frame_height = int(cap.get(4))
frame_rate = cap.get(cv2.CAP_PROP_FPS)

# calculate the frame duration
frame_duration = 1 / frame_rate

# create a StupidArtnet instance for each row of pixels
artnets = [StupidArtnet(TARGET_IP, universe, frame_width * 3) for universe in range(frame_height)]

while cap.isOpened():
    # get the current time
    start_time = time.time()

    # read a frame from the video
    ret, frame = cap.read()
    if not ret:
        break

    # extract the pixel data from the frame
    pixels = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

    # send the pixel data as Art-Net data
    for row, artnet in enumerate(artnets):
        packet = pixels[row].flatten().tolist()
        artnet.set(packet)
        artnet.show()

    # wait until it's time to show the next frame
    elapsed_time = time.time() - start_time
    remaining_time = frame_duration - elapsed_time
    if remaining_time > 0:
        time.sleep(remaining_time)

# release the video capture
cap.release()
