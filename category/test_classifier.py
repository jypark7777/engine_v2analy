import unittest
import classifier
import requests
import time
from classifier import classify_user

class CategoryClassifierTest(unittest.TestCase):
    
    def setUp(self):
        self.username = "sal_gungli" #카테고리 분류할 인스타그램 유저명

        #인스타그램에서 최신 데이터 가져오기 
        new = 0 #최신 가져오려면 1로 변경 
        if new:
            requests.get(f'https://feat.report/crawl_instagram_save?request_type=user&parameter={username}/')
            time.sleep(6) #디비 넣는 시간 기다려줌

    def test_user_category(self):

        #Data에서 유저 정보 가져오기
        response_profile_data = requests.get(f"https://data.featuringscore.ai/instagram/crawluserprofile/u/{self.username}/")
        self.assertEqual(response_profile_data.status_code, 200)
        profile_data = response_profile_data.json()
        # print(profile_data)

        response_postlist_data = requests.get(f"https://data.featuringscore.ai/instagram/crawlpost/{profile_data['insta_pk']}/list/")
        self.assertEqual(response_postlist_data.status_code, 200)
        postlist_data = response_postlist_data.json()
        if 'results' in postlist_data and len(postlist_data['results']):
            postlist_data = postlist_data['results']
        # print(postlist_data)

        classify_user_data = classify_user(profile_data, postlist_data)
        print(classify_user_data)


if __name__ == '__main__':
    unittest.main()