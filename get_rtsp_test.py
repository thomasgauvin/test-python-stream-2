# import the necessary packages
import cv2
import os

os.environ["OPENCV_FFMPEG_CAPTURE_OPTIONS"] = "rtsp_transport;udp"
# vcap = cv2.VideoCapture("rtsp://freja.hiof.no:1935/rtplive/definst/hessdalen03.stream", cv2.CAP_FFMPEG)
vcap = cv2.VideoCapture("rtsp://localhost:8554/live", cv2.CAP_FFMPEG)


while(1):

    ret, frame = vcap.read()
    cv2.imshow('VIDEO', frame)
    cv2.waitKey(1)