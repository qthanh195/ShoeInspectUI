import cv2
import numpy as np
from pypylon import pylon
from PySide6.QtGui import QImage, QPixmap
from PySide6.QtCore import Signal, QObject
from inspection import Inspection
import genicam

class ControlCamera(Inspection):
    image_signal = Signal(QImage)
    def __init__(self):
        super().__init__()
        
        self.widthframe = 0
        self.heightframe = 0
        self.rotateframe = 0
        self.angleRightDeviation = 0
        self.angleLeftDeviation = 0
        self.flag_drawCenter = False
        
        self.flag_point1 = False
        self.flag_point2 = False
        self.flag_btconfirm = 0
        
        self.exposureTimeCamera = 35000
        
        self.camera = None
        self.camera_open = False  # Khởi tạo biến trạng thái camera
        # self.camera = pylon.InstantCamera(pylon.TlFactory.GetInstance().CreateFirstDevice())
        self.converter = pylon.ImageFormatConverter()
        self.converter.OutputPixelFormat = pylon.PixelType_BGR8packed
        self.converter.OutputBitAlignment = pylon.OutputBitAlignment_MsbAligned

    def init_camera(self):
        try:
            self.camera = pylon.InstantCamera(pylon.TlFactory.GetInstance().CreateFirstDevice())
        except genicam.RuntimeException as e:
            print(f"Error initializing camera: {e}")
            self.camera = None

    def start_camera(self):
        if not self.camera_open:
            self.camera.Open()
            self.camera.StartGrabbing(pylon.GrabStrategy_LatestImageOnly)
            self.camera_open = True

    def stop_camera(self):
        if self.camera_open:
            self.camera_open = False
            self.camera.StopGrabbing()
            self.camera.Close()
            cv2.destroyAllWindows()

    def display_camera(self):
        self.start_camera()  # Ensure the camera is started before displaying images

        while self.camera_open:
            # Chờ có ảnh từ camera
            try:
                grabResult = self.camera.RetrieveResult(self.exposureTimeCamera, pylon.TimeoutHandling_ThrowException)
                if grabResult.GrabSucceeded():
                    image = self.converter.Convert(grabResult)
                    img = image.GetArray()
                    # print(img.shape)
                    #rotate
                    M = cv2.getRotationMatrix2D((1374, 1920), self.rotateframe, 1.0)
                    img = cv2.warpAffine(img, M, (3840, 2748))
                    ##
                    img_rb = img[self.heightframe:self.heightframe+2310, self.widthframe:self.widthframe+3350]
                    self.detect_object(img_rb)
                    if self.flag_drawCenter:
                        # cv2.line(img_rb, (0,self.centerX), (3350,self.centerX), (0,255,0), thickness=3)
                        # cv2.line(img_rb, (self.centerY,0), (self.centerY,2310), (0,0,255), thickness=3)
                        cv2.line(img_rb, (0,self.centerY), (3350,self.centerY), (0,255,0), thickness=3)
                        cv2.line(img_rb, (self.centerX,0), (self.centerX,2310), (0,0,255), thickness=3)
                        print("xx",self.centerX)
                        print("yy",self.centerY)
                    if self.flag_btconfirm != 0:
                        cv2.line(img_rb, (0,self.centerObjectX), (3350,self.centerObjectX), (0,255,0), thickness=3)
                        cv2.line(img_rb, (self.centerObjectY,0), (self.centerObjectY,2310), (0,0,255), thickness=3)
                        p = "(" + str(self.centerObjectY) +"; " + str(self.centerObjectX)+")"
                        cv2.putText(img_rb,p,(self.centerObjectX+50,self.centerObjectY-50), cv2.FONT_HERSHEY_SIMPLEX, 4, (0, 0, 0), thickness=4)
                    # Xử lý cho Qlable
                    img_rgb = cv2.resize(img_rb, (0, 0), fx=0.3, fy=0.3) 
                    img_rgb = cv2.cvtColor(img_rgb, cv2.COLOR_BGR2RGB)
                    h, w, ch = img_rgb.shape
                    bytes_per_line = ch * w
                    q_image = QImage(img_rgb.data, w, h, bytes_per_line, QImage.Format_RGB888)
                    self.image_signal.emit(q_image)
                    # print(f"Current exposure time: {self.camera.ExposureTime.GetValue()} µs")
                
                grabResult.Release()
            except Exception as e:
                print(f"Error: {e}")
                break

        self.stop_camera()  # Ensure the camera is stopped and resources are cleaned up
        q_image = None
        self.image_signal.emit(q_image)
    
    def close_camera(self):
        self.stop_camera()

# Setup
# Độ sáng cam, Cropcam, self.ratio, blur trước, blur sau, threshold, max-min area, center, cộng trừ dài rộng,
# +/- góc xoay, 