from fastapi import FastAPI
from pydantic import BaseModel
from typing import Any, Dict, AnyStr, List, Union

app = FastAPI()

JSONObject = Dict[AnyStr, Any]
JSONArray = List[Any]
JSONStructure = Union[JSONArray, JSONObject]



@app.get("/")
async def root():
    return {"message": "Hello World"}


@app.post('/calculator/reach')
async def calculator_reach(reach_parameter : JSONStructure = None):
    from calculator.reach import calculate_reach

    """도달수 분석"""
    print(reach_parameter.keys())
    profile_dict = reach_parameter[b'profile_dict']
    post_list = reach_parameter[b'post_list']
    avg_like_count = reach_parameter[b'avg_like_count']
    avg_comment_count = reach_parameter[b'avg_comment_count']

    value = await calculate_reach(profile_dict, post_list, avg_like_count, avg_comment_count)

    return value

@app.post('/text/cloud')
async def text_cloud(text_parameter : JSONObject = None):
    from text.cloud import get_text_rank

    print(text_parameter)
    """텍스트 빈도수 높은 단어 추출"""
    value = await get_text_rank(text_parameter[b'text'])

    return value



@app.post('/text/languages')
async def text_languages(text_parameter : JSONObject = None):
    """텍스트 언어 예측

        Returns:
            [
                {
                    "code": "ko",
                    "confidence": 99.0
                }
                ..
            ]
    """
    from text.text_polyglot import get_text_languages

    print(text_parameter)
    value = get_text_languages(text_parameter[b'text'])

    return value


@app.post('/classifier/posttext')
def classifier_post_text(parameter : JSONStructure = None):
    from category.classifier import classify_post_text
    
    """카테고리 태그 분류하기"""
    
    text_datas = parameter[b"text"]
    value = classify_post_text(text_datas)
    return value



@app.post('/classifier/user')
def classifier_user(parameter : JSONStructure = None):
    from category.classifier import classify_user

    """카테고리 태그 분류하기"""
    profile_dict = parameter[b'profile_dict']
    post_list = parameter[b'post_list']

    value = classify_user(profile_dict, post_list)

    return value



@app.post('/image/analyze/face')
def analyze_face(parameter : JSONStructure = None):
    from image.analyze_face import predict_age_gender

    """얼굴 나이,성별 예측"""
    image_url = parameter[b'image_url']

    value = predict_age_gender(image_url)

    return value

@app.post('/image/analyze/object')
def analyze_object(parameter : JSONStructure = None):
    from image.analyze_object import detection_object

    """사물 탐색하기"""
    image_url = parameter[b'image_url']

    value = detection_object(image_url)

    return value


@app.post('/image/analyze/colortone')
def analyze_colortone(parameter : JSONStructure = None):
    from image.analyze_image import picker_feeling_color

    """컬러감 추출하기"""
    image_url = parameter[b'image_url']

    value = picker_feeling_color(image_url)

    return value