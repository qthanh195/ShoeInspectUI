import json
import numpy as np

class Setup:
    def __init__(self, name, robotCenterX, robotCenterY, startWidth, startHeight,frameAngle,exposureTimeCamera, threshold, beforBlur, afterBlur, z_robot, angleRobotOffset, curentProgram, curentConfig, flag_default):
        self.name = name
        self.robotCenterX = robotCenterX # tâm của robot nhìn từ camera
        self.robotCenterY = robotCenterY
        self.startWidth = startWidth # điểm bắt đầu cắt khung hình
        self.startHeight = startHeight
        self.frameAngle = frameAngle    # góc xoay của camera so với toạ độ robot 
        self.exposureTimeCamera = exposureTimeCamera    # thời gian mở màn trập, càng lây càng sáng 
        self.threshold = threshold  # ngưỡng lấy ảnh trên ảnh gray 
        self.beforBlur = beforBlur  # Xóa nhiễu trước khi tách ngưỡng
        self.afterBlur = afterBlur  # Xóa nhiễu sau khi tách ngưỡng
        self.z_robot = z_robot
        self.angleRobotOffset = angleRobotOffset
        self.curentProgram = curentProgram
        self.curentConfig = curentConfig
        self.flag_default = flag_default
        
    def config(self):
        pass

    def to_dict(self):
        return {
            'name': self.name,
            'robotCenterX': self.robotCenterX,
            'robotCenterY': self.robotCenterY,
            'startWidth': self.startWidth,
            'startHeight': self.startHeight,
            'frameAngle': self.frameAngle,
            'exposureTimeCamera': self.exposureTimeCamera,
            'threshold': self.threshold,
            'beforBlur': self.beforBlur,
            'afterBlur': self.afterBlur,
            'z_robot': self.z_robot,
            'angleRobotOffset': self.angleRobotOffset,
            'curentProgram': self.curentProgram,
            'curentConfig': self.curentConfig,
            'flag_default': self.flag_default,
        }
    @staticmethod
    def from_dict(data):
        return Setup(
            name=data['name'],
            robotCenterX=data['robotCenterX'],
            robotCenterY=data['robotCenterY'],
            startWidth=data['startWidth'],
            startHeight=data['startHeight'],
            frameAngle=data['frameAngle'],
            exposureTimeCamera=data['exposureTimeCamera'],
            threshold=data['threshold'],
            beforBlur=data['beforBlur'],
            afterBlur=data['afterBlur'],
            z_robot=data['z_robot'],
            angleRobotOffset=data['angleRobotOffset'],
            curentProgram=data['curentProgram'],
            curentConfig=data['curentConfig'],
            flag_default=data['flag_default'],
            
        )
    
    def save_multi_config(configs):
        data = {'data': [config.to_dict() for config in configs]}
        with open("setup.json", 'w') as f:
            json.dump(data, f, indent=4)
            
            
    def write_config(self, sample):
        try:
            with open("setup.json", 'r') as f:
                data = json.load(f)
        except FileNotFoundError:
            data = {'data': []}

        data['data'].append(sample.to_dict())

        with open("setup.json", 'w') as f:
            json.dump(data, f, indent=4)

    def load_config(self):
        try:
            with open("setup.json", 'r') as f:
                data = json.load(f)
            if not data or 'data' not in data:
                print("Tệp setup.json không chứa dữ liệu hợp lệ")
                return []
            return [Setup.from_dict(item) for item in data['data']]
        except FileNotFoundError:
            print("Tệp setup.json không tồn tại")
            return []
        except json.JSONDecodeError:
            print("Lỗi đọc tệp setup.json")
            return []
        
    def set_data_config_default(self, curentconfig):
        try:
            with open("setup.json", 'r') as f:
                data = json.load(f)
        except FileNotFoundError:
            data = {'data': []}

        data_config = data.get('data', [])
        for cf in data_config:
            if 'curentConfig' in cf and cf['curentConfig'] == curentconfig:
                cf['flag_default'] = True
            else:
                cf['flag_default'] = False
        with open("setup.json", 'w') as f:
            json.dump(data, f, indent=4)
    
    def load_config_by_currentIndex(self, curentconfig):
        try:
            with open("setup.json", 'r') as f:
                data = json.load(f)
        except FileNotFoundError:
            data = {'data': []}

        data_config = data.get('data', [])
        i = 0
        for cf in data_config:
            cf['curentConfig'] = i
            i+=1
            if 'curentConfig' in cf and cf['curentConfig'] == curentconfig:
                cf['flag_default'] = True
            else:
                cf['flag_default'] = False
        with open("setup.json", 'w') as f:
            json.dump(data, f, indent=4)
    
    def load_name_config(self):
        configs = self.load_config()
        name_configs = []
        for config in configs:
            name_configs.append(config.name)
        return name_configs
    
    def delete_config_by_curentindex(self, curentconfig):
        try:
            with open("setup.json", 'r') as f:
                data = json.load(f)
        except FileNotFoundError:
            data = {'data': []}

        data_config = data.get('data', [])
        for cf in data_config:
            if 'curentConfig' in cf and cf['curentConfig'] == curentconfig:
                data_config.remove(cf)
                break
        i = 0
        for cf in data_config:
            cf['curentConfig'] = i
            i+=1
        with open("setup.json", 'w') as f:
            json.dump(data, f, indent=4)