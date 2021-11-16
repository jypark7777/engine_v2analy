import pandas as pd
from konlpy.tag import Komoran
from konlpy.tag import Twitter
import joblib
import unicodedata
import os
import emoji

komoran = Komoran()


def tokenizer_morphs(doc):
    return komoran.morphs(doc)

dir = os.path.join(os.path.dirname(__file__))


def test_preprocessor(text):
    posts = list()
    posts.append(text)

    three = pd.DataFrame(posts, columns=['text'])

    three['cleaned'] = three['text'].apply(text_cleaner)
    test_set = three

    return test_set

def text_cleaner(sentence):
    try:
        sentence = sentence.replace(')', '').replace('(', '').replace('↵', '').replace('.', '').replace(',', '').replace("'", "").replace('·', ' ').replace('=', '').replace('\n', '')
        sentence = emoji.demojize(sentence)
        sentence = unicodedata.normalize('NFC', sentence)
    except:
        sentence = sentence

    return sentence

def campaign_classifier(post):
    if '공구' in post:
        campaign_result = '공구/공동구매'
    elif '공동구매' in post:
        campaign_result = '공구/공동구매'
    elif '협찬' in post:
        campaign_result = '협찬/광고'
    elif '광고' in post:
        campaign_result = '협찬/광고'
    elif '체험단' in post:
        campaign_result = '체험단/리뷰'
    elif '리뷰' in post:
        campaign_result = '체험단/리뷰'
    else:
        campaign_result = '-'

    return campaign_result

def category_classifier(post, category_clf):
    categories = ['의류/잡화', '가구/인테리어', '식품', '뷰티', '유아/키즈',
                  '생활/건강', '디지털/가전/컴퓨터', '레저/자동차', '도서/취미', '반려동물']

    category_label = category_clf.predict(post).tolist()

    if category_label[0] != 0:
        category_result = categories[category_label[0]-1]
    else:
        category_result = '-'

    return category_label, category_result

def subclass_classifier(post, category_label, subclass_clfs):
    subclasses = ['패션의류', '스포츠/아웃도어 의류', '구두/운동화', '가방', '쥬얼리', '기타 잡화',
                  '스킨케어', '클렌징/필링', '메이크업', '헤어케어', '바디케어', '네일케어', '향수', '미용 기기',
                  '스포츠 용품', '아웃도어 용품', '자동차 용품', '자동차', '기타 동체',
                  '조리 된 음식', '스낵', '과채류', '커피', '기타 음료', '건강 식품', '베이커리', '다이어트 식품', '반찬/조미료', '인스턴트',
                  '유아 의류', '키즈 의류', '유아 용품/장난감', '키즈 용품/장난감', '유아 가구', '키즈 가구', '유아 식품',
                  '주방 용품', '생활 용품', '욕실 용품', '청소 용품', '건강 용품', '수납 용품',
                  '침실 가구', '거실 가구', '사무 가구', '주방 가구', '인테리어 소품',
                  '엔터테인먼트 가전', '계절 가전', '주방 가전', '가전 소품', '생활 가전',
                  '도서/음반', '문구/사무 용품', '악기', '취미/글귀',
                  '반려동물 용품', '반려동물 식품', '반려동물 장난감']

    if category_label[0] != 0:
        subclass_result = subclass_clfs[category_label[0] -
                                        1].predict(post).tolist()
        if subclass_result[0] != 0:
            subclass_result = subclasses[subclass_result[0]-1]
    else:
        subclass_result = '-'

    return subclass_result

def post_analyzer(test_set, category_clf, subclass_clfs):
    influencer_posts = dict()

    for index, row in test_set.iterrows():

        post = list()
        post.append(row['cleaned'])

        campaign_result = campaign_classifier(row['cleaned'])
        category_label, category_result = category_classifier(
            post, category_clf)
        subclass_result = subclass_classifier(
            post, category_label, subclass_clfs)

        influencer_posts[index] = dict()
        # influencer_posts[index]['post'] = row['cleaned']

        influencer_posts[index]['campaign_type'] = campaign_result
        influencer_posts[index]['category'] = category_result
        influencer_posts[index]['subclass'] = subclass_result

    return influencer_posts


def push_this_button(post_text):


    category_clf = joblib.load(dir + "/category_clf.joblib")
    subclass_clfs = joblib.load(dir + "/subclass_clfs.joblib")

    text = list()
    text.append(post_text)
    print(text)
    test_set = test_preprocessor(text)

    post_details = post_analyzer(test_set, category_clf, subclass_clfs)

    x = pd.DataFrame.from_dict(post_details, orient='index')
    x.to_csv('post_details.csv', index=False)

    return post_details

# print(push_this_button('#아네로즈 @anneerose21 이거 오래 기다리셨죠~? 방금 막 업.뎃.완.료! 니트는 아더컬러 착용샷도 예쁘니깐 체크꼭 해주시구, 스커트는 플리츠 디자인에 패턴감이 흔치않아, 니트 블라우스 셔츠 어디에나 코디하기에 예쁠것 같아 추천해요 '))

# [0]['subclass'].encode(encoding='ISO-8859-1',errors='strict').decode(encoding='UTF-8',errors='strict')