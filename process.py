from PySide6.QtCore import Qt, QCoreApplication, QTextStream
from PySide6.QtWidgets import QMainWindow, QMenu, QWidget, QApplication
from PySide6.QtGui import QAction, QImage,QPixmap
# from ui2805 import Ui_MainWindow
from codeui1306 import Ui_MainWindow
from camera import ControlCamera
from setup import Setup
import threading
from robot import ControlRobot
from addSample import Sample
import time
import cv2
import random
import math
import sys

class MySideBar(QMainWindow, Ui_MainWindow, ControlCamera,ControlRobot,Sample, Setup):
    def __init__(self):
        super().__init__()
        ControlRobot.__init__(self)
        ControlCamera.__init__(self)
        
        # # Redirect stdout and stderr to QPlainTextEdit
        # sys.stdout = QTextStream(self.textEdit_terminal.document())
        # sys.stderr = QTextStream(self.textEdit_terminal.document())
        
        self.flag_logdat = False
        self.flag_autoadjust = False 
        # self.max_row = 1
        self.stt_data = 0
        
        self.setupUi(self)
        self.setWindowTitle("ShoeInspectionUI")
        
        self.update_ccboxSample() # Update comboBox when information changes
        self.update_ccboxConfig()
        self.update_infosample() # Update infomation when information changes
        self.init_config() # innit config 
        
        self.camera_thread = None   # Flag camera thread
        
        self.cnt_None.connect(self.updatecntnone) # if none contour call funtion clear 
        self.image_signal.connect(self.update_image) # Waiting for img from image_signal
        self.image_thr.connect(self.update_image_thr) # Waiting for thresh from _signal
        self.bt_Camera.clicked.connect(self.toggleCamera) # nút bấm camera
        self.bt_Connect.clicked.connect(self.toggleConnect) # nút connect rb
        self.dimensions_updated.connect(self.update_labels) # # cập nhật thông tin kích thước 
        
        self.bt_Save.clicked.connect(self.save_samples) # button save sample 
        self.cbb_NameSm.currentIndexChanged.connect(self.update_infosample) #lineedit trang inspection
        self.bt_Delete.clicked.connect(self.remove_sample) 
        self.bt_Home.clicked.connect(self.robot_call_home)

        self.bt_Run.clicked.connect(self.toggle_maigiay)
        self.bt_Stop.clicked.connect(self.toggle_maigiay)
        self.bt_Pause.clicked.connect(self.toggle_pauserobot)
        self.bt_Start.clicked.connect(self.toggle_inspection)
        self.update_inspectUI.connect(self.update_inpect)
        
        self.bt_Setio.clicked.connect(self.setIOrobot)
        self.bt_Resetio.clicked.connect(self.resetIOrobot)
        
        self.checkBox_EnDrawLine.stateChanged.connect(self.toggle_checkbox_drawline)
        self.sp_CalibCenterX.valueChanged.connect(self.change_centerx)
        self.sp_CalibCenterY.valueChanged.connect(self.change_centery)
        self.sp_widthframe.valueChanged.connect(self.change_widthframe)
        self.sp_heightframe.valueChanged.connect(self.change_heightframe)
        self.sp_rotate.valueChanged.connect(self.change_rotateframe)
        
        #Calib
        self.sp_exposureTime.valueChanged.connect(self.change_exposuretime)
        self.sp_threshold.valueChanged.connect(self.change_exposuretime)
        
        self.bt_AutoAdjust.clicked.connect(self.toggle_autoadjust)
        self.bt_saveConfig.clicked.connect(self.saveConfig)
        
        self.point1 = None
        self.point2 = None
        self.bt_point1.clicked.connect(self.toggle_point1)
        self.bt_point2.clicked.connect(self.toggle_point2)
        self.bt_confirmcenter.clicked.connect(self.toggle_usenewcorrdinate)
        
        self.bt_UseConfig.clicked.connect(self.update_infoConfig)
        self.bt_DeleteConfig.clicked.connect(self.remove_config)
        
        # self.flag_btconfirm = 0
        
    def closeEvent(self, event):
        #tat luong cam
        self.set_data_config_default(self.cbb_ConfigName.currentIndex())
        # print("a")
        if self.camera_open:
            self.toggleCamera()
            print("Close thread camera!")
        #tat luong robot
        if self.flag_maigiay:
            self.toggle_maigiay()
            print("Close thread roobt!")
        #tat luong inspect
        if self.flag_qc:
            self.toggle_inspection()
            print("Close thread inspect!")
        if self.flag_btconfirm != 0:
            self.toggle_inspection()
            print("Close thread inspect!")
            
        event.accept()
        
    def updatecntnone(self):
        self.lb_InWidthcur.setText("")
        self.lb_InHeightcur.setText("")
        self.lb_InAccuracySample.setText("")
        
        self.lb_RoWidth.setText("")
        self.lb_RoHeight.setText("")
        # self.lb_Accuracy_2.setText("")
        
        self.le_AdWidth.setText("")
        self.le_AdHeight.setText("")
        
        self.lb_Accuracy.setText("")
        self.lb_okng.setText("")
        
        self.le_AdAccuracySample.setText("")
        # self.lb_okng.setText("")

    def toggleCamera(self):
        if self.camera_open:
            self.bt_Camera.setText("Open Camera")
            self.close_camera()
            self.updatecntnone()
            
            if self.flag_qc:
                self.toggle_inspection()
        
        else:
            # self.bt_Camera.setVisible(False)
            if self.camera is None:
                self.init_camera()
                time.sleep(1)
                self.toggleCamera()
            self.openCamera()
            self.bt_Camera.setText("Close Camera")

    def openCamera(self):
        if not self.camera_open:
            self.widthframe = self.sp_widthframe.value()
            self.heightframe = self.sp_heightframe.value()
            self.rotateframe = self.sp_rotate.value()
            # Start camera display in a separate thread
            self.camera_thread = threading.Thread(target=self.display_camera)
            self.camera_thread.start()
    
    def close_camera(self):
        if self.camera_open:
            super().close_camera()
            if self.camera_thread:
                self.camera_thread.join()  # Wait for the thread to finish
                self.camera_thread = None
    
    def update_image(self, q_image):
        if q_image is not None:
            self.lb_showcam.setPixmap(QPixmap.fromImage(q_image))
        else:self.lb_showcam.clear()
        
    def update_image_thr(self, q_image_thr):
        if q_image_thr is not None:
            self.lb_thresh.setPixmap(QPixmap.fromImage(q_image_thr))
        else:self.lb_thresh.clear()
        
    def toggleConnect(self):
        self.robot_ip = self.le_ip.text()
        print(self.robot_ip)
        if self.robot_connect:
            self.bt_Connect.setText("Connect")
            self.rb_disconnect()
        else:
            self.rb_connect()
            self.bt_Connect.setText("Disconnect")
            
    def update_labels(self, width, height):
        self.lb_InWidthcur.setText(f"{width}")
        self.lb_InHeightcur.setText(f"{height}")
        self.lb_RoWidth.setText(f"{width}")
        self.lb_RoHeight.setText(f"{height}")
        
        self.le_AdWidth.setText(f"{width}")
        self.le_AdHeight.setText(f"{height}")
   
    def save_samples(self):
        if self.cnt is not None and \
            self.le_SampleName.text() != "" and \
            self.le_AdWidthDeviation.text() != "" and \
            self.le_AdHeightDeviation.text() != "" and \
            self.le_AdAccuracySample.text() != "":
            new_sample = Sample(self.le_SampleName.text(), self.width_img, self.height_img, self.le_AdWidthDeviation.text(), self.le_AdHeightDeviation.text(), self.le_AdAccuracySample.text(), self.cnt)
            self.write_sample(new_sample)
            self.cbb_NameSm.addItem(self.le_SampleName.text())
            self.cbb_AdSampleName.addItem(self.le_SampleName.text())
            self.le_SampleName.setText("")
        else:
            print("Không đủ thông số.")
        
    def update_ccboxSample(self):
        name_sms = self.load_name_sample()
        [self.cbb_NameSm.addItem(name_sm) for name_sm in name_sms]
        [self.cbb_AdSampleName.addItem(name_sm) for name_sm in name_sms]
        
    def update_infosample(self):
        self.curr_sample = self.load_sample_by_name(self.cbb_NameSm.currentText())
        if self.curr_sample is not None:
            self.lb_InWidthSample.setText(self.curr_sample.width)
            self.lb_IHeightSample.setText(self.curr_sample.height)
            self.lb_InWidthDeviation.setText(self.curr_sample.width_dev)
            self.lb_InHeightDeviation.setText(self.curr_sample.height_dev)
            self.lb_InAccuracySample.setText(self.curr_sample.accuracy_sample)
            
    def remove_sample(self):
        
        self.delete_sample_by_name(self.cbb_AdSampleName.currentText())
        self.cbb_NameSm.removeItem(self.cbb_AdSampleName.currentIndex())
        self.cbb_AdSampleName.removeItem(self.cbb_AdSampleName.currentIndex())
    
    def toggle_pauserobot(self):
        if self.flag_maigiay and not self.flag_pause:
            self.flag_pause = True
            self.bt_Pause.setText("Resume")
            
        elif self.flag_maigiay and self.flag_pause:
            self.flag_pause = False
            self.bt_Pause.setText("Pause")
            
    def robot_call_home(self):
        self.set_user_coordinate_id(10)
        self.set_tool_id(10) 
        if not self.flag_maigiay:
            self.robot_home()
        else:
            print("Robot đang chạy chương trình khác.")

    def toggle_maigiay(self):
        if self.flag_maigiay:
            self.flag_maigiay = False
            self.flag_pause = False
            self.bt_Run.show()
            self.bt_Pause.hide()
            self.bt_Stop.hide()

            self.bt_Run.setText("Run")
            
            self.robot_thread.join()  # Wait for the thread to finish
            self.robot_thread = None
            
        else:
            if not self.camera_open:
                self.toggleCamera()
                
            if self.flag_qc:
                self.toggle_inspection
                
            
            self.robot_call_home()
            self.flag_maigiay = True
            self.bt_Run.setText("Stop")
            # 
            self.bt_Run.hide()
            self.bt_Pause.show()
            self.bt_Stop.show()

            self.robot_thread = threading.Thread(target=self.call_maigiay)
            self.robot_thread.start()
  
    def call_maigiay(self):
        self.setIO(3,1)
        time.sleep(2)
        self.setIO(3,0)
        text_dir = self.cbb_Dir.currentText()
        if text_dir == "Right":
            dir = 1
        else:
            dir = 0
            
        print("dir",dir)
        while self.flag_maigiay:
            if self.flag_pause:
                continue
            state_robot = self.get_program_state()
            print(state_robot)
            if state_robot != 0:
                continue
            if self.cnt is None:
                print("Không có Contour.")
                continue
            # similarity_ = cv2.matchShapes(cnt_sample, self.cnt, cv2.CONTOURS_MATCH_I1, 0.0)
            # accuracy = max(0, min(100, (1 - similarity) * 100))
            if 309 > float(self.height_img) > 315 and 109 > float(self.width_img) > 112:
                continue
            if dir == 1:
                pos = self.check_pos_right()
            else:
                pos = self.check_pos_left()
            print(pos)
            if pos is not None:
                self.maigiay(pos, dir)
                pos = None
        self.robot_call_home()
        
    def toggle_inspection(self):
        if self.flag_qc:
            self.flag_qc = False
            self.bt_Start.setText("Auto Inspection")
            self.lb_okng.setText("")
            
            self.inspect_thread.join()  # Wait for the thread to finish
            self.inspect_thread = None
        
        else:
            if self.flag_maigiay:
                self.toggle_maigiay()
                
            if not self.camera_open:
                self.toggleCamera()
                
            self.bt_Start.setText("Stop")
            self.inspection_thread = threading.Thread(target=self.inspect)
            self.inspection_thread.start()
            self.flag_qc = True
            
    def inspect(self):
        while self.flag_qc :
            if self.cnt is not None:
                accuracy,quality = self.qc_giay(self.curr_sample.width, 
                                    self.curr_sample.height,
                                        self.curr_sample.width_dev,
                                        self.curr_sample.height_dev,
                                        self.curr_sample.accuracy_sample,
                                        self.curr_sample.contour)
                
                self.update_inspectUI.emit(accuracy,quality)
            
            time.sleep(0.5)
        
    def update_inpect(self, accuracy,quality):
        if self.cnt is not None:
            accuracy = f"{accuracy:.2f}"
            self.lb_Accuracy.setText(str(accuracy))
            if quality:
                self.lb_okng.setText("OK")
                self.lb_okng.setStyleSheet("color: green;")
            else:
                self.lb_okng.setText("NG")
                self.lb_okng.setStyleSheet("color: red;")
                
    def setIOrobot(self):
        # print(self.get_user_coordinate_id())
        # print(self.get_tool_id())
        # self.set_tool_id(10)
        # self.set_user_coordinate_id(3)
        # print(self.get_user_coordinate_id())
        # print(self.get_tool_id())
        if not self.flag_maigiay:
            self.setIO(int(self.le_IO.text()),1)
    
    def resetIOrobot(self):
        if not self.flag_maigiay:
            self.setIO(int(self.le_IO.text()),0)
            
    def logdata(self):
        pass
        # if self.flag_maigiay:
        #     self.flag_maigiay = False
        #     self.bt_Run.setText("Run")
            
        #     self.robot_thread.join()  # Wait for the thread to finish
        #     self.robot_thread = None
            
        # if not self.camera_open:
        #     self.openCamera()
        #     self.bt_Camera.setText("Close Camera")

        # while True:
        #     if self.cnt is not None:
        #         # new_data = str(self.stt_data) + "," + str(self.height_img) + "," + str(self.width_img) + "," + str(self.area_img)
        #         new_data = "1,311.13,110.36,1772538.0"
        #         workbook = load_workbook('logDimension.xlsx')
        #         sheet = workbook.active
        #         max_row = sheet.max_row
        #         sheet[f'B{max_row+1}']= new_data
        #         workbook.save('logDimension.xlsx')
        #         self.stt_data+=1

    def toggle_checkbox_drawline(self):
        if self.checkBox_EnDrawLine.isChecked():
            self.flag_drawCenter = True
            self.centerX = self.sp_CalibCenterX.value()
            self.centerY = self.sp_CalibCenterY.value()
        else:
            self.flag_drawCenter = False
            
    def change_centerx(self):
        self.centerX = self.sp_CalibCenterX.value()
    
    def change_centery(self):
        self.centerY = self.sp_CalibCenterY.value()
    
    def change_widthframe(self):
        self.widthframe = self.sp_widthframe.value()
    
    def change_heightframe(self):
        self.heightframe = self.sp_heightframe.value()
        
    def change_rotateframe(self):
        self.rotateframe = self.sp_rotate.value()
        
    def change_exposuretime(self):
        self.exposureTimeCamera = self.sp_exposureTime.value()
        self.camera.ExposureTime.SetValue(self.exposureTimeCamera)
        
    def change_threshold(self):
        self.threshold = self.sp_threshold.value()
        
    def toggle_autoadjust(self):
        if self.flag_autoadjust:
            self.flag_autoadjust = False
            self.bt_AutoAdjust.setText("Auto Adjust")
            
            self.autoadjust_thread.join()  # Wait for the thread to finish
            self.autoadjust_thread = None
        
        else:
            if self.flag_maigiay:
                self.toggle_maigiay()
                
            if not self.camera_open:
                self.toggleCamera()
                
            self.bt_AutoAdjust.setText("Adjusting....")
            self.flag_autoadjust = True
            self.autoadjust_thread = threading.Thread(target=self.autoAdjust)
            self.autoadjust_thread.start()
        
    def evaluate_contour(self,tolerance=0.1):

        # Kiểm tra kích thước trong khoảng +/- tolerance
        width_in_range = (float(self.curr_sample.width) - tolerance) <= float(self.width_img) <= (float(self.curr_sample.width) + tolerance)
        height_in_range = (float(self.curr_sample.height) - tolerance) <= float(self.height_img) <= (float(self.curr_sample.height) + tolerance)

        if width_in_range and height_in_range:
            similarity = cv2.matchShapes(self.curr_sample.contour, self.cnt, cv2.CONTOURS_MATCH_I1, 0.0)
            accuracy = max(0, min(100, (1 - similarity) * 100))
            return accuracy
        else:
            return 0
        
    def autoAdjust(self):
        #kiem tra phai co contour ban dau
        if self.cnt is None:
                print("Contour None")
                self.exposureTimeCamera = 30000
                self.camera.ExposureTime.SetValue(self.exposureTimeCamera)
                
        while self.flag_autoadjust and self.cnt is None:
            self.exposureTimeCamera+=10
            self.camera.ExposureTime.SetValue(self.exposureTimeCamera)
            self.sp_exposureTime.setValue(self.exposureTimeCamera)
            time.sleep(0.2)
            if self.exposureTimeCamera >= 1000000:
                self.toggle_autoadjust()
            print(".")
            
        
        print("Contour.................") 

        while self.flag_autoadjust:

            for _ in range(1000):  # Số lần thử ngẫu nhiên
                # exposure_time = random.randint(0, 1600000)
                bblur = random.choice([3, 5, 7])
                ablur = random.choice([3, 5, 7])
                threshold = random.randint(150, 250)

                self.exposureTimeCamera+=50
                self.camera.ExposureTime.SetValue(self.exposureTimeCamera)
                self.bblur = bblur
                self.ablur = ablur
                self.threshold = threshold
                
                accuracyauto = self.evaluate_contour()
                self.sp_exposureTime.setValue(self.exposureTimeCamera)
                self.sp_threshold.setValue(self.threshold)
                # self.cbb_bblur.setCurrentText(self.bblur)
                # self.cbb_ablur.setCurrentText(self.ablur)
                
                if accuracyauto >= 99:
                    best_params = (self.exposureTimeCamera, bblur, ablur, threshold)
                    print("self.exposureTimeCamera", self.exposureTimeCamera)
                    print("bblur", bblur)
                    print("ablur", ablur)
                    print("threshold", threshold)
                    print("w", self.curr_sample.width)
                    print("h", self.curr_sample.height)
                    
                    self.toggle_autoadjust()
                    
            self.toggle_autoadjust()

    def saveConfig(self):
        # data = self.load_config()
        # for dt in data:
        #     if dt.name == "Default":
        #         print("Ten da ton tai")
        #         return
        new_config = Setup(self.le_configName.text(),self.sp_CalibCenterX.value(), self.sp_CalibCenterY.value(),\
            self.sp_widthframe.value(), self.sp_heightframe.value(),\
                self.sp_rotate.value(), self.sp_exposureTime.value(),\
                    self.sp_threshold.value(), int(self.cbb_bblur.currentText()),\
                        int(self.cbb_ablur.currentText()), float(self.le_Zrobot.text()),\
                            float(self.le_Anglerobot.text()), self.cbb_Dir.currentIndex(),self.cbb_ConfigName.count(), True)
        self.write_config(new_config)
        self.cbb_ConfigName.addItem(self.le_configName.text())
        self.le_configName.clear()
        print("Write Config")

    def init_config(self):

        self.bt_Pause.hide()
        self.bt_Stop.hide()
        init_config = self.load_config()
        for cf in init_config:
            if cf.flag_default:
                self.sp_CalibCenterX.setValue(cf.robotCenterX)
                self.sp_CalibCenterY.setValue(cf.robotCenterY)
                self.sp_widthframe.setValue(cf.startWidth)
                self.sp_heightframe.setValue(cf.startHeight)
                self.sp_rotate.setValue(cf.frameAngle)
                self.sp_exposureTime.setValue(cf.exposureTimeCamera)
                self.sp_threshold.setValue(cf.threshold)
                # self.cbb_bblur.setValue(cf.robotCenterX)
                # self.cbb_ablur.setValue(cf.robotCenterX)
                self.le_Zrobot.setText(str(cf.z_robot))
                self.le_Anglerobot.setText(str(cf.angleRobotOffset))
                self.cbb_Dir.setCurrentIndex(cf.curentProgram)
                self.cbb_ConfigName.setCurrentIndex(cf.curentConfig)
        self.centerX = self.sp_CalibCenterX.value()
        self.centerY = self.sp_CalibCenterY.value()
        self.z_robot = float(self.le_Zrobot.text())
        self.AngleRobot = float(self.le_Anglerobot.text())
    
    def update_infoConfig(self):
        init_config = self.load_config()
        for cf in init_config:
            # print("a",cf.curentConfig)
            # print("b",self.cbb_ConfigName.currentIndex())
            if cf.curentConfig == self.cbb_ConfigName.currentIndex():
                self.sp_CalibCenterX.setValue(cf.robotCenterX)
                self.sp_CalibCenterY.setValue(cf.robotCenterY)
                self.sp_widthframe.setValue(cf.startWidth)
                self.sp_heightframe.setValue(cf.startHeight)
                self.sp_rotate.setValue(cf.frameAngle)
                self.sp_exposureTime.setValue(cf.exposureTimeCamera)
                self.sp_threshold.setValue(cf.threshold)
                # self.cbb_bblur.setValue(cf.robotCenterX)
                # self.cbb_ablur.setValue(cf.robotCenterX)
                self.le_Zrobot.setText(str(cf.z_robot))
                self.le_Anglerobot.setText(str(cf.angleRobotOffset))
                self.cbb_Dir.setCurrentIndex(cf.curentProgram)
                self.cbb_ConfigName.setCurrentIndex(cf.curentConfig)
                
                self.centerX = self.sp_CalibCenterX.value()
                self.centerY = self.sp_CalibCenterY.value()
                self.z_robot = float(self.le_Zrobot.text())
                self.AngleRobot = float(self.le_Anglerobot.text())
                break
    
    def update_ccboxConfig(self):
        name_cfs = self.load_name_config()
        [self.cbb_ConfigName.addItem(name_cf) for name_cf in name_cfs]
    
    def remove_config(self):
        self.delete_config_by_curentindex(self.cbb_ConfigName.currentIndex())
        self.cbb_ConfigName.removeItem(self.cbb_ConfigName.currentIndex())
        self.update_ccboxConfig()
    # Calib center by 3 point
    def toggle_point1(self):
        # if not self.flag_point1:
        #     self.flag_point2 = False
        #     self.flag_point1 = True
        #     self.bt_point1.setText("Save")
        #     self.bt_point2.setText("Point2")
        #     self.confirm3point()
        # else:
            p1 = "(" + str(self.centerObjectY) +"; " + str(self.centerObjectX)+")"
            self.le_point1.setText(p1)
            self.point1 = (self.centerObjectX,self.centerObjectY)
            text_dir = self.cbb_Dir.currentText()
            if text_dir == "Right":
                dir = 1
            else:
                dir = 0
            self.AngleRobot = 0
            if dir == 1:
                pos = self.check_pos_right()
            else:
                pos = self.check_pos_left()
            angle = float(pos[1])
            self.le_Anglerobot.setText(str(angle))
            self.flag_point1 = False
            # self.bt_point1.setText("Point1")
            self.confirm3point()
            
    def toggle_point2(self):
        # if not self.flag_point2:
        #     self.flag_point2 = True
        #     self.flag_point1 = False
        #     self.bt_point2.setText("Save")
        #     self.bt_point1.setText("Point1")
        #     self.confirm3point()
        # else:
            p2 = "(" + str(self.centerObjectY) +"; " + str(self.centerObjectX)+")"
            self.le_point2.setText(p2)
            self.point2 = (self.centerObjectX,self.centerObjectY)
            self.flag_point2 = False
            # self.bt_point2.setText("Point2")
            self.confirm3point()
            
    def confirm3point(self):
        if self.point2 and self.point1 is not None:
            self.bt_confirmcenter.setText("Use New Coordinates")
            self.flag_btconfirm = 2        
    
    def toggle_usenewcorrdinate(self):
        if self.flag_btconfirm == 0: #Dang trangj thai 0 hienj clibnew
            self.flag_btconfirm = 1
            self.bt_confirmcenter.setText("Cancel")
            # self.newcorrdinate_thread = threading.Thread(target=self.handle_calibcorrdinate)
            # self.newcorrdinate_thread.start()
        elif self.flag_btconfirm == 1: #dang cancel da du thong so
            self.point1 = None
            self.point2 = None
            self.le_point1.clear()
            self.le_point2.clear()
            self.bt_confirmcenter.setText("Calib New Coordinates")
            self.flag_btconfirm = 0
            # self.newcorrdinate_thread.join()  # Wait for the thread to finish
            # self.newcorrdinate_thread = None
        else:
            self.sp_CalibCenterX.setValue(self.point1[1])
            self.sp_CalibCenterY.setValue(self.point1[0])
            self.Zrobot = float(self.le_Zrobot.text())
            self.AngleRobot = float(self.le_Anglerobot.text())
            
            slope = (self.point2[1] - self.point1[1]) / (self.point2[0] - self.point1[0])
            theta = math.atan(slope)
            theta_degrees = math.degrees(theta)
            # angle_with_vertical = 90 - theta_degrees
            print(theta_degrees)
            self.sp_rotate.setValue(self.sp_rotate.value()-theta_degrees)
            
            self.point1 = None
            self.point2 = None
            print("Use new Corrdinate.")
            self.le_point1.clear()
            self.le_point2.clear()
            self.bt_confirmcenter.setText("Calib New Coordinates")
            self.flag_btconfirm = 0
            # self.newcorrdinate_thread.join()  # Wait for the thread to finish
            # self.newcorrdinate_thread = None
    
    def handle_calibcorrdinate(self):
        while self.flag_btconfirm != 0:
            if self.flag_point1:
                p1 = "(" + str(self.centerObjectY) +"; " + str(self.centerObjectX)+")"
                self.le_point1.setText(p1)
                self.point1 = (self.centerObjectX,self.centerObjectY)
            if self.flag_point2:
                p2 = "(" + str(self.centerObjectY) +"; " + str(self.centerObjectX)+")"
                self.le_point2.setText(p2)
                self.point2 = (self.centerObjectX,self.centerObjectY)