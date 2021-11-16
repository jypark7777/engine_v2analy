import os, csv
from collections import Counter, defaultdict
import time

def find_matching_stargram_keywords(texts, is_exclude_stagram=False) -> list:
    """OO스타그램을 정리한 csv 파일로 텍스트에 키워드가 포함 되어있는지 찾는 함수
        Args:
            texts : 텍스트 문장 
            is_exclude_stagram : '스타그램' 제거 유무 

        CSV Format:
            Keyword(기준 카테고리 태그), "Word1, Word2, ... (연관 단어들, OO스타그램)" 
    """

    dir = os.path.join(os.path.dirname(__file__))
    filepath = os.path.join(dir, 'stargram_category.csv')

    texts_include_keyword = []
    """파일을 맵형태로 변환"""
    with open(filepath) as csvfile:
        reader = csv.reader(csvfile)
        for row in reader:
            category_keyword_name = row[0] #카테고리 키워드 (뷰티, 키즈, 화장품..)
            words = row[1] #카테고리 연관 OO스타그램 (패션스타그램, 품스타그램,..)
            words = words.replace(" ","").split(',')

            for word in words:
                if is_exclude_stagram: #스타그램 제거 유무 , Default - False`
                    if word.endswith('스타그램'):
                        word = word.replace('스타그램', '')
                    if word.endswith('그램'):
                        word = word.replace('그램', '')

            
                if word in texts and len(word) > 0: #텍스트에 OO스타그램 포함 유무
                    texts_include_keyword.append(category_keyword_name) #카테고리 키워드 추가
    
    return dict(Counter(texts_include_keyword))

def classify_post_text(text_datas) -> dict:
    """인스타 포스팅 카테고리 분류 
    Args:
        text: 글 데이터 

        Returns: 
    """

    # from .category_classifier import push_this_button
    
    # category_data = push_this_button(text_datas)[0]['subclass'].encode(encoding='ISO-8859-1',errors='strict').decode(encoding='UTF-8',errors='strict')
    # text_datas = text_datas.encode(encoding='UTF-8',errors='strict').decode(encoding='ISO-8859-1',errors='strict')
    file_name = time.time()
    os.system(f'python3 category/save_category.py -texts="{text_datas}" -name="{file_name}"')
    
    for i in range(10):
        try:
            get_result = open(f'category/temp/{file_name}.txt')
            result_text = get_result.read()
        except:
            time.sleep(1)

    result = {
        'matching_stargram_keywords' : find_matching_stargram_keywords(text_datas, True), #스타그램 분류법 
        'category_data': result_text,
        # ... 포스팅 분류법들을 추가 
    }
    get_result.close()
    os.remove(f'category/temp/{file_name}.txt')
    return result

def classify_user(profile_dict, post_list) -> dict:
    """인스타 계졍 카테고리 분류 
    
    Args:
        profile_dict:
        {
            "id": 95931091,
            "zip": null,
            "record": 5095601,
            "city_id": null,
            "category": null,
            "insta_pk": 48801826188,
            "latitude": null,
            "username": "selfme_care",
            "biography": "3분 동안 99% 살균!\n셀프미 칫솔살균기 출시🦷✨\n구매하러가기💙\n👇👇",
            "city_name": null,
            "full_name": "셀프미 케어",
            "longitude": null,
            "snap_date": "2021-08-24",
            "snap_time": "2021-08-24T12:01:14.281084",
            "is_private": false,
            "is_business": false,
            "is_favorite": false,
            "is_verified": false,
            "media_count": 4,
            "created_time": "2021-08-24T12:01:14.281065",
            "external_url": "https://smartstore.naver.com/centroshop/products/5666086075",
            "has_chaining": true,
            "is_transfile": false,
            "public_email": null,
            "updated_time": "2021-08-24T12:02:11.880345",
            "address_street": null,
            "follower_count": 371,
            "usertags_count": 6,
            "following_count": 5,
            "geo_media_count": 0,
            "profile_pic_url": "https://scontent-nrt1-1.cdninstagram.com/v/t51.2885-19/s150x150/218426401_1743765209144967_5980197994963096736_n.jpg?_nc_ht=scontent-nrt1-1.cdninstagram.com&_nc_ohc=JXFNZs0rO9sAX8UUe_W&edm=AId3EpQBAAAA&ccb=7-4&oh=576a3d17f76fe02dda2a429a548b9a26&oe=612A7A52&_nc_sid=705020",
            "direct_messaging": null,
            "is_analy_complete": true,
            "total_igtv_videos": 0,
            "hd_profile_pic_url": null,
            "is_profile_crawled": false,
            "is_report_complete": false,
            "following_tag_count": 0,
            "has_highlight_reels": null,
            "is_interest_account": null,
            "public_phone_number": null,
            "auto_expand_chaining": null,
            "contact_phone_number": null,
            "instagram_location_id": null,
            "is_analy_requirements": true,
            "is_potential_business": null,
            "mutual_followers_count": 0,
            "business_contact_method": null,
            "can_be_reported_as_fraud": null,
            "can_hide_public_contacts": false,
            "fb_page_call_to_action_id": null,
            "public_phone_country_code": null,
            "should_show_public_contacts": false,
            "has_anonymous_profile_picture": false
            }

        post_list:
            [
                {
                "id": 106486118,
                "lat": null,
                "lng": null,
                "code": "CTMN8U8v3bx",
                "user": 106509,
                "record": 5178414,
                "insta_id": null,
                "insta_pk": 2651555600881645000,
                "is_video": false,
                "taken_at": "2021-08-30T16:54:41",
                "typename": "GraphSidecar",
                "has_liked": false,
                "snap_date": "2021-08-30",
                "snap_time": "2021-08-30T19:58:08.776603",
                "like_count": 779,
                "media_type": null,
                "filter_type": null,
                "created_time": "2021-08-30T19:58:08.776584",
                "photo_of_you": false,
                "updated_time": "2021-08-30T19:58:09.749920",
                "comment_count": 20,
                "sidecar_parent": null,
                "can_viewer_save": false,
                "client_cache_key": null,
                "crawlpostcaption": [
                    {
                    "id": 369412136,
                    "post": 106486118,
                    "text": "#공구\n\n아워아워는 오늘까지 구입가능하시고요 ,, 보니까 거의 꽉 찬 4개월 주기로 열게 되더라고요~ 담번 7차 공구는 12월 말이나 내년으루 넘어갈것 같아용~!\n\n주문량이 많아 걱정했는데 물류센터에서 주말동안 출근하셔서 입고작업이랑 포장작업 미리 해주셔서 오늘부터 조금씩 순차출고 시작했어요~ (그래도 배송이 밀릴 수 있으니 조금 여유있게 기다려주시면 감사하겠습니다🙏🏻)\n\n댓글후기, 구매완료 이벤트 댓글은 공구 첫 피드에 남겨주시면 좋을것 같아요 ~. \n\n내역을 보니까 70%이상이 저번공구 후 재구매해주시는 분들이시더라고요~~ 쏟아지는 세제광고 사이에서 조용히만들고 있는 아워아워인데 안사라지고 계속 나오는게 정말 신기해요 (다 구매해주시는 분들덕분🤍🤍🤍!! ) \n이게 공구때문에 제가 쓰는게 아니라 저도 모르게 계속 쓰게되다보니 없는 공구를 만들어서 하게 된 경우거든요 😂\n여기저기서 공구제안 많이 받는 세제인데 대표님이 공구 생각이 없으세요 (여기저기 노출되고 공구도 많이하면 더 많이 팔리고 좋을텐데 욕심이 정말 없으심… 단독이라 덕분에 35%할인율로 열어드릴 수 있게 된 공구입니당^^!! ) \n\n댓글도 많이 남겨주셔서 하나하나 빠짐없이 읽으면서 정말 감사했어용!!🙏🏻❣️\n\n출고 부지런히 해드릴께요 조금만 기다려주세요~ 🤍\n\n#감사합니다 \n#아워아워\n배송문의 및 궁금하신 사항은 카톡 #아워아워 에 남겨주시면 답변 가장 빠르구요 저에게 댓글이나 메세지 주셔도 확인하는대로 답 드릴께요 🙂",
                    "type": null,
                    "record": 5178414,
                    "status": null,
                    "user_id": null,
                    "insta_pk": null,
                    "media_id": null,
                    "bit_flags": null,
                    "snap_date": "2021-08-30",
                    "snap_time": "2021-08-30T19:58:08.824861",
                    "created_at": null,
                    "content_type": null,
                    "created_time": "2021-08-30T19:58:08.824839",
                    "updated_time": "2021-08-30T19:58:08.842938",
                    "share_enabled": false,
                    "created_at_utc": null,
                    "did_report_as_spam": null
                    }
                ],
                "video_view_count": null,
                "caption_is_edited": false,
                "has_more_comments": false,
                "can_viewer_reshare": false,
                "carousel_media_count": null,
                "accessibility_caption": "Photo shared by 살궁리 on August 30, 2021 tagging @our_hour_official. May be an image of indoor.",
                "comment_likes_enabled": false,
                "organic_tracking_token": null,
                "can_see_insights_as_brand": false,
                "comment_threading_enabled": true,
                "can_view_more_preview_comments": false,
                "direct_reply_to_author_enabled": false,
                "max_num_visible_preview_comments": null,
                "inline_composer_display_condition": null
                },

                ...
        ]
    """

    if post_list != None:
        post_matching_stargram_keywords = {}

        for post in post_list: #각 포스팅 마다 분류
            post_classfication = classify_post_text(post)

            matching_stargram_keywords = post_classfication['matching_stargram_keywords']
            post_matching_stargram_keywords = {k: post_matching_stargram_keywords.get(k, 0) + matching_stargram_keywords.get(k, 0) for k in set(post_matching_stargram_keywords) | set(matching_stargram_keywords)}
        
            print("개별 포스팅 분류 : ", post_classfication)
        

        print(Counter(post_matching_stargram_keywords).most_common(5))

    return Counter(post_matching_stargram_keywords).most_common(5)
