import cv2
import numpy as np
from PySide6.QtGui import QImage, QPixmap
from PySide6.QtCore import Signal, QObject

class Inspection():
    image_thr = Signal(QImage)
    dimensions_updated = Signal(str, str)
    update_inspectUI = Signal((float, bool))
    cnt_None =Signal(bool)
    def __init__(self):
        self.ratio = 0.1182068543451652
        self.cnt = None
        self.width_img = 0
        self.height_img = 0
        self.centerObjectX = 0
        self.centerObjectY = 0
        
        self.centerX = 0
        self.centerY = 0
        # self.AngleRobot = -7.415 # Right
        self.AngleRobot = 0 # Left
        
        self.area_img = 0
        self.flag_qc= False
        self.threshold = 220
        self.bblur = 7
        self.ablur = 3
        
    def detect_object(self, image):
        img = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
        img = cv2.blur(img, (self.bblur, self.bblur), 2)
        ret, thresh1 = cv2.threshold(img, self.threshold, 255, cv2.THRESH_BINARY)
        thresh1 = cv2.blur(thresh1, (self.ablur, self.ablur), 2)
        contours, hierarchy = cv2.findContours(thresh1, cv2.RETR_TREE, cv2.CHAIN_APPROX_NONE)
        self.cnt = None
        for i in contours:
            # print(cv2.contourArea(i))
            area_cnt = cv2.contourArea(i)
            if 1859520.5 > area_cnt > 1702000:
                self.cnt = i
                self.dimension()
                self.area_img = area_cnt
                # Xử lý thresh ui
                white_img = np.ones(img.shape, dtype=np.uint8) * 255
                cv2.drawContours(white_img,[i], -1, (0,0,0), thickness=cv2.FILLED)
                white_img = cv2.resize(white_img, (0, 0), fx=0.08, fy=0.08) 
                
                img_thr = cv2.cvtColor(white_img, cv2.COLOR_BGR2RGB)
                h, w, ch = img_thr.shape
                bytes_per_line = ch * w
                q_image_thr = QImage(img_thr.data, w, h, bytes_per_line, QImage.Format_RGB888)
                self.image_thr.emit(q_image_thr)
        if self.cnt is None:
            self.cnt_None.emit(0)
            q_image_thr = None
            self.image_thr.emit(q_image_thr)
               
    def dimension(self):
        
        rect = cv2.minAreaRect(self.cnt)
        ((x, y),(h,w),_) = rect
        self.centerObjectX = int(y)
        self.centerObjectY = int(x)
        int(w)
        int(h)
        width = f"{w*self.ratio:.2f}"
        height = f"{h*self.ratio:.2f}"
        if width < height:
            width_img = width
            height_img = height
        else:
            width_img = height
            height_img = width
            
        # print("c",float(width_img))
        # print("b",float(self.width_img))
        # print("a",float(self.width_img)+0.1)
        
        if  (float(self.width_img)+0.1) < float(width_img) or float(width_img) < (float(self.width_img)-0.2):
            self.width_img = width_img
            # print("m")
        else:
            self.width_img = self.width_img
            # print("n")
        if  (float(self.height_img)+0.2) < float(height_img) or float(height_img) < (float(self.height_img)-0.2):
            self.height_img = height_img
            # print("p")
        else:
            self.height_img = self.height_img
            # print("q")
        # print("w", self.width_img)
        # print("h",self.height_img)
        self.dimensions_updated.emit(str(self.width_img), str(self.height_img))
        
    def check_pos_right(self):
        rect = cv2.minAreaRect(self.cnt)
        x, y = rect[0]

        mask = np.zeros((2880,2880),np.uint8)
        cnt = self.cnt + np.array([int(1440-x), int(1440-y)])
        cv2.drawContours(mask,[cnt],0,255,-1)
        
        rotation_matrix = cv2.getRotationMatrix2D((1440,1400), rect[2], 1)  # Tạo ma trận biến đổi
        mask = cv2.warpAffine(mask, rotation_matrix, (mask.shape[1], mask.shape[0]))
        
        mask1 = mask[:1440, :1440]# góc trái-trên
        mask2 = mask[1440:, :1440]# góc trái- dưới
        mask3 = mask[:1440, 1440:]# góc phải-trên
        mask4 = mask[1440:, 1440:]# góc phải dưới
        
        
        b1 = cv2.countNonZero(mask1)
        b2 = cv2.countNonZero(mask2)
        b3 = cv2.countNonZero(mask3)
        b4 = cv2.countNonZero(mask4)
        
        a_min = min(b1,b2,b3,b4)
        if a_min == b1:
            agl = 180-rect[2]
        elif a_min == b2:
            agl = -90-rect[2]
        elif a_min == b3:
            agl = 90- rect[2]
        else:
            agl = -rect[2]

        x = int(x)
        y = int(y)

        # Thực hiện các phép tính trước khi chuyển đổi thành chuỗi
        y_result = -(x - int(self.centerX)) * self.ratio
        x_result = -(y - int(self.centerY)) * self.ratio

        # Chuyển đổi kết quả thành chuỗi với định dạng .3f
        # y = f'{y_result:.3f}'
        # x = f'{x_result:.3f}'
        y = f'{y_result:.3f}'
        x = f'{x_result:.3f}'
        print("x", self.centerX)
        print("y", self.centerY)
        center = (x,y)
        # agl = f'{agl+6.56:.3f}'
        agl = f'{agl-self.AngleRobot:.3f}'
        print("a", agl)
        return center,agl

    def check_pos_left(self):
        rect = cv2.minAreaRect(self.cnt)
        x, y = rect[0]

        mask = np.zeros((2880,2880),np.uint8)
        cnt = self.cnt + np.array([int(1440-x), int(1440-y)])
        cv2.drawContours(mask,[cnt],0,255,-1)
        
        rotation_matrix = cv2.getRotationMatrix2D((1440,1400), rect[2], 1)  # Tạo ma trận biến đổi
        mask = cv2.warpAffine(mask, rotation_matrix, (mask.shape[1], mask.shape[0]))
        
        mask1 = mask[:1440, :1440]# góc trái-trên
        mask2 = mask[1440:, :1440]# góc trái- dưới
        mask3 = mask[:1440, 1440:]# góc phải-trên
        mask4 = mask[1440:, 1440:]# góc phải dưới

        
        b1 = cv2.countNonZero(mask1)
        b2 = cv2.countNonZero(mask2)
        b3 = cv2.countNonZero(mask3)
        b4 = cv2.countNonZero(mask4)
        

        a_min = min(b1,b2,b3,b4)
        if a_min == b1:
            agl = 90-rect[2]

        elif a_min == b2:
            agl = rect[2]-180

        elif a_min == b3:
            agl = -rect[2]

        else:
            agl = -(90 +rect[2])
        x = int(x)
        y = int(y)

        # Thực hiện các phép tính trước khi chuyển đổi thành chuỗi
        y_result = -(x - int(self.centerX)) * self.ratio
        x_result = -(y - int(self.centerY)) * self.ratio

        # Chuyển đổi kết quả thành chuỗi với định dạng .3f
        y = f'{y_result:.3f}'
        x = f'{x_result:.3f}'
        # y = f'{y_result:.3f}'
        # x = f'{x_result:.3f}'
        
        center = (x,y)
        # agl = f'{agl-4.94:.3f}'
        agl = f'{agl-self.AngleRobot:.3f}'
        return center,agl
    
    def qc_giay(self, wight_sample, height_sample, wight_dev,height_dev, accuracy_sample,cnt_sample):
        #kiem tra do tuong dong
        similarity = cv2.matchShapes(cnt_sample, self.cnt, cv2.CONTOURS_MATCH_I1, 0.0)
        accuracy = max(0, min(100, (1 - similarity) * 100))
        # print("accuracy",accuracy)
        # print(float(accuracy_sample))
        # accuracy = 100- similarity
        
        if ((float(wight_sample)-float(wight_dev)) <= float(self.width_img) or   float(self.width_img)<= (float(wight_sample)+float(wight_dev))) and \
            ((float(height_sample)+float(height_dev))<= float(self.height_img) or float(self.height_img) <= (float(height_sample)+float(height_dev))) and\
                (float(accuracy) >= float(accuracy_sample)):
                    return accuracy,True
        else:
            return accuracy,False