import json
import numpy as np

class Sample:
    def __init__(self, name, width, height, width_dev,height_dev,accuracy_sample, contour):
        self.name = name
        self.width = width
        self.height = height
        self.width_dev = width_dev
        self.height_dev = height_dev
        self.accuracy_sample = accuracy_sample
        self.contour = contour

    def to_dict(self):
        return {
            'name': self.name,
            'width': self.width,
            'height': self.height,
            'width_dev': self.width_dev,
            'height_dev': self.height_dev,
            'accuracy_sample': self.accuracy_sample,
            'contour': self.contour.tolist()  # Convert contour to list
        }
    # @staticmethod
    def from_dict(data):
        return Sample(
            name=data['name'],
            width=data['width'],
            height=data['height'],
            width_dev=data['width_dev'],
            height_dev=data['height_dev'],
            accuracy_sample=data['accuracy_sample'],
            contour=np.array(data['contour'])  # Convert list back to numpy array
        )
    
    def save_multi_samples(samples):
        data = {'data': [sample.to_dict() for sample in samples]}
        with open("sample.json", 'w') as f:
            json.dump(data, f, indent=4)
            
    def write_sample(self, sample):
        try:
            with open("sample.json", 'r') as f:
                data = json.load(f)
        except FileNotFoundError:
            data = {'data': []}

        data['data'].append(sample.to_dict())

        with open("sample.json", 'w') as f:
            json.dump(data, f, indent=4)

    def load_samples(self):
        try:
            with open("sample.json", 'r') as f:
                data = json.load(f)
            if not data or 'data' not in data:
                print("Tệp sample.json không chứa dữ liệu hợp lệ")
                return []
            return [Sample.from_dict(item) for item in data['data']]
        except FileNotFoundError:
            print("Tệp sample.json không tồn tại")
            return []
        except json.JSONDecodeError:
            print("Lỗi đọc tệp sample.json")
            return []
    
    def load_sample_by_name(self,name):
        samples = self.load_samples()
        for sample in samples:
            if sample.name == name:
                # print(name)
                return sample
        print(f"Không tìm thấy mẫu có tên '{name}'")
        return None
    
    def load_name_sample(self):
        samples = self.load_samples()
        name_samples = []
        for sample in samples:
            name_samples.append(sample.name)
        return name_samples
    
    def delete_sample_by_name(self, name):
        try:
            with open("sample.json", 'r') as f:
                data = json.load(f)
        except FileNotFoundError:
            data = {'data': []}

        samples = data.get('data', [])
        for sample in samples:
            if 'name' in sample and sample['name'] == name:
                samples.remove(sample)
                break
        with open("sample.json", 'w') as f:
            json.dump(data, f, indent=4)

    
