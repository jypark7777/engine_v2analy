import time, traceback
import random, os,csv
from colorthief import ColorThief

import math
from PIL import Image, ImageDraw
import numpy
from image.image_utils import get_url_image_file
  
def rgb_to_hex(rgb):
    return '%02x%02x%02x' % rgb

def hex_to_rgb(hex):
    value = hex.lstrip('#')
    lv = len(value)
    return tuple(int(value[i:i + lv // 3], 16) for i in range(0, lv, lv // 3))


def color_palette(path_url):
    """컬러 피커 뽑아내기"""

    # file_path = f"image/temp/1634523635.477879.0.6951927152018041.jpg"
    # file_path = f"image/temp/{time.time()}.{random.random()}.jpg"
    # try:
    #     print(path_url)
    #     urllib.request.urlretrieve(path_url, file_path)
    # except:
    #     return None

    file_path = get_url_image_file(path_url)

    if file_path == None:
        return None
        
    color_thief = ColorThief(file_path)

    dominant_color = color_thief.get_color(quality=10)
    palettes = color_thief.get_palette(color_count=10)

    results = []
    for palette in palettes:
        hex = rgb_to_hex(palette)
        results.append(hex)
    
    # os.remove(file_path)

    return results

    
def draw_result_rect(hex_list):
    w, h = 220, 220
    print(hex_list)
    
    img = Image.new("RGB", (w*len(hex_list), h))

    img1 = ImageDraw.Draw(img)  
    for index, hex in enumerate(hex_list):
        x1 = w*index
        x2 = w*index+(w)
        
        shape = ((x1,0),(x2 ,h))
        img1.rectangle(shape, fill="#"+hex)
    
    img.show()


def color_distance(src_rgb, dst_rgb):
    rgb1 = numpy.array([ src_rgb[0]/255, src_rgb[1]/255, src_rgb[2]/255 ])
    rgb2 = numpy.array([ dst_rgb[0]/255, dst_rgb[1]/255, dst_rgb[2]/255 ])

    rm = 0.5*(rgb1[0]+rgb2[0])
    d = sum((2+rm,4,3-rm)*(rgb1 - rgb2)**2)**0.5
    return d

def rgb_to_feeling(hex_list):
    dir = os.path.join(os.path.dirname(__file__))
    filepath = os.path.join(dir, 'color_feeling_list.csv')

    results = {}

    feeling_colors = {}
    with open(filepath) as csvfile:
        reader = csv.reader(csvfile)
        for row in reader:
            feeling_name = row[0]
            feeling_rgb_hex = row[1]
            feeling_colors[feeling_rgb_hex] = feeling_name

    for rgb_hex in hex_list:
        # print(hex_to_rgb(rgb_hex))
        rgb = hex_to_rgb(rgb_hex)
        min_dis_rgb = None
        min_dis_feeling = None
        min_dis = 10
        for feeling_rgb_hex in feeling_colors.keys():
            feeling_rgb = hex_to_rgb(feeling_rgb_hex)
            distance = color_distance(rgb,feeling_rgb)

            if min_dis > distance:
                min_dis = distance
                min_dis_rgb = feeling_rgb
                min_dis_feeling = feeling_colors[feeling_rgb_hex]
        
        if min_dis_feeling != "고상한" and min_dis_feeling != "점잖은": #두개는 빈도수가 높아서 제외 
            if min_dis_feeling not in results:
                results[min_dis_feeling] = 1
            else:
                results[min_dis_feeling] += 1
        # if min_dis < 0.1:
        #     print(rgb,min_dis_rgb, min_dis, min_dis_feeling)

    """파일을 맵형태로 변환"""
    results = list(results.items())
    results.sort(key = lambda x:x[1], reverse=True)
    print(results)

    return results

    # RGB Hex값으로 느낌() 스트링으로 변경



def picker_feeling_color(path_url):
    """이미지의 컬러톤을 추출하고, 컬러감으로 변환
    
        Returns:
            list, list (tuple) : ./color_feeling_list.csv 
            , [('고상한', 3), ('점잖은', 2), ('화려한', 1), ('모던한', 1), ('은은한', 1), ('귀여운', 1)]
    """
    palette_result = color_palette(path_url)
    if palette_result != None:
        return palette_result, rgb_to_feeling(palette_result)
    return None, None

# draw_result_rect(palette_result)

# detect_human()