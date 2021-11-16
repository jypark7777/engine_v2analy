import urllib.request, time, traceback
import random, os
# from .yolo.yolov3 import detecting_objects
import cv2
import numpy as np
from image.image_utils import get_url_image_file


def detecting_objects_yolo(filepath):

    net = cv2.dnn.readNet("image/yolo/data/yolov3.weights", "image/yolo/data/yolov3.cfg")
    classes = []
    with open("image/yolo/data/coco.names", "r") as f:
        classes = [line.strip() for line in f.readlines()]
    layer_names = net.getLayerNames()
    output_layers = [layer_names[i[0] - 1] for i in net.getUnconnectedOutLayers()]

    # 이미지 가져오기
    img = cv2.imread(filepath)
    img = cv2.resize(img, None, fx=0.4, fy=0.4)
    height, width, channels = img.shape



    # 사물 탐색
    blob = cv2.dnn.blobFromImage(img, 0.00392, (416, 416), (0, 0, 0), True, crop=False)
    net.setInput(blob)
    outs = net.forward(output_layers)


    # 정보를 화면에 표시
    outputs = []

    class_ids = []
    confidences = []
    boxes = []
    for out in outs:
        for detection in out:
            scores = detection[5:]
            class_id = np.argmax(scores)
            confidence = scores[class_id]
            if confidence > 0.5:
                # Object detected
                center_x = int(detection[0] * width)
                center_y = int(detection[1] * height)
                w = int(detection[2] * width)
                h = int(detection[3] * height)
                # 좌표
                x = int(center_x - w / 2)
                y = int(center_y - h / 2)
                boxes.append([x, y, w, h])
                confidences.append(float(confidence))
                class_ids.append(class_id)

                label = str(classes[class_id])
                detectitem = (label, [x, y, w, h], float(confidence))
                outputs.append(detectitem)
    print(outputs)
    return outputs

def detection_object(path_url):
    """사물 분석하기"""


    # file_path = f"image/temp/{time.time()}.{random.random()}.jpg"
    file_path = get_url_image_file(path_url)
    if file_path == None:
        return None

    # urllib.request.urlretrieve(path_url, file_path)
    
    result = detecting_objects_yolo(file_path)

    # os.remove(file_path)

    return result


# analyze_object("https://scontent-gmp1-1.cdninstagram.com/v/t51.2885-15/e35/p1080x1080/243061932_1052439488849741_5629383268778914662_n.jpg?_nc_ht=scontent-gmp1-1.cdninstagram.com&_nc_cat=1&_nc_ohc=me7hjR0tcUQAX8FKg9y&edm=AP_V10EBAAAA&ccb=7-4&oh=e148e262703f7c73aba93c8b6ce23d43&oe=61625A5A&_nc_sid=4f375e")

