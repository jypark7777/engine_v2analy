# featuringeg-analy

피처링 프로젝트에서 사용할 분석 모듈 프로젝트 입니다. 

# API List

#### calculator
- /calculator/reach
    - 도달 예측 계산 하기
    - Method : POST
    - Parameter 
    ```json
    Profile A Mode Data
    ```

#### Text
- /text/cloud
    - 텍스트 랭크 출력 (워드 클라우드 사용)
    - Method : POST
    - Parameter 
    ```json
    {"text":"#공구\n\n아워아워는 오늘까지 구입가능하시고요 ,, 보니까 거의 꽉 찬 4개월 주기로 열게 되더라고요~ 담번 7차 공구는 12월 말이나 내년으루 넘어갈것 같아용~!\n\n주문량이 많아 걱정했는데 물류센터에서 주말동안 출근하셔서 입고작업이랑 포장작업 미리 해주셔서 오늘부터 조금씩 순차출고 시작했어요~ (그래도 배송이 밀릴 수 있으니 조금 여유있게 기다려주시면 감사하겠습니다🙏🏻)\n\n댓글후기, 구매완료 이벤트 댓글은 공구 첫 피드에 남겨주시면 좋을것 같아요 ~. \n\n내역을 보니까 70%이상이 저번공구 후 재구매해주시는 분들이시더라고요~~ 쏟아지는 세제광고 사이에서 조용히만들고 있는 아워아워인데 안사라지고 계속 나오는게 정말 신기해요 (다 구매해주시는 분들덕분🤍🤍🤍!! ) \n이게 공구때문에 제가 쓰는게 아니라 저도 모르게 계속 쓰게되다보니 없는 공구를 만들어서 하게 된 경우거든요 😂\n여기저기서 공구제안 많이 받는 세제인데 대표님이 공구 생각이 없으세요 (여기저기 노출되고 공구도 많이하면 더 많이 팔리고 좋을텐데 욕심이 정말 없으심… 단독이라 덕분에 35%할인율로 열어드릴 수 있게 된 공구입니당^^!! ) \n\n댓글도 많이 남겨주셔서 하나하나 빠짐없이 읽으면서 정말 감사했어용!!🙏🏻❣️\n\n출고 부지런히 해드릴께요 조금만 기다려주세요~ 🤍\n\n#감사합니다 \n#아워아워\n배송문의 및 궁금하신 사항은 카톡 #아워아워 에 남겨주시면 답변 가장 빠르구요 저에게 댓글이나 메세지 주셔도 확인하는대로 답 드릴께요 🙂"}
    ```
    
- /text/languages
    - 언어 판별하기
    - Method : POST
    - Parameter 
    ```json
    {"text":"문스바이블"}
    ```
#### Image

- /image/analyze/face
    - 얼굴 탐지, 얼굴 나이, 성별 예측
    - Method : POST
    - Parameter 
    ```json
    {"image_url":"https://scontent-gmp1-1.cdninstagram.com/v/t51.2885-15/e35/p1080x1080/243061932_1052439488849741_5629383268778914662_n.jpg?_nc_ht=scontent-gmp1-1.cdninstagram.com&_nc_cat=1&_nc_ohc=me7hjR0tcUQAX8FKg9y&edm=AP_V10EBAAAA&ccb=7-4&oh=e148e262703f7c73aba93c8b6ce23d43&oe=61625A5A&_nc_sid=4f375e"}
    ```


- /image/analyze/face
    - 사진 사물 탐색
    - Method : POST
    - Parameter 
    ```json
    {"image_url":"https://scontent-gmp1-1.cdninstagram.com/v/t51.2885-15/e35/p1080x1080/243061932_1052439488849741_5629383268778914662_n.jpg?_nc_ht=scontent-gmp1-1.cdninstagram.com&_nc_cat=1&_nc_ohc=me7hjR0tcUQAX8FKg9y&edm=AP_V10EBAAAA&ccb=7-4&oh=e148e262703f7c73aba93c8b6ce23d43&oe=61625A5A&_nc_sid=4f375e"}
    ```
    


# Dependencies

## Mecab Install

```commandline
python3 -m pip install konlpy
bash <(curl -s https://raw.githubusercontent.com/konlpy/konlpy/master/scripts/mecab.sh)
```

## Ployglot Install
링크 : https://polyglot.readthedocs.io/en/latest/Installation.html

```commandline
pip install polyglot pyicu
```

polyglot depends on 
`numpy <http://www.numpy.org/>`__, 
`icu <http://site.icu-project.org/home>`__ and 
`pyicu <https://github.com/ovalhub/pyicu>`.

#### 우분투 등 리눅스에서 설치하기:


```commandline
sudo apt-get install python-numpy libicu-dev python-icu
```

Or if you're using Python 3:

```commandline
sudo apt-get install python3-numpy libicu-dev python3-icu
```

Note: If you try to load ``polyglot`` and it tells you ``ImportError: No module
named 'icu'``, then it's ``pyicu`` that you're missing.


#### 맥에서 설치 하기:

```commandline
brew install intltool icu4c gettext
brew link icu4c gettext --force
pip install pycld2 morfessor six numpy polyglot

**** mac pyicu 설치시 환경변수 에러 해결 ****
PATH="/usr/local/opt/icu4c/sbin:/usr/local/opt/icu4c/bin:$PATH"

**** ubuntu 내용 ****
ImportError: libGL.so.1: cannot open shared object file: No such file or directory
해결:
sudo apt install libgl1-mesa-glx
```

## PyICU 설치
해결
```commandline
export ICU_VERSION=59
PYICU_INCLUDES=/usr/local/Cellar/icu4c/67.1/include
PYICU_LFLAGS=-L/usr/local/Cellar/icu4c/67.1/lib
pip install pyicu==1.9.7
```

## Py-Agender 트레이닝 데이터 다운로드

**./image/pyagender/pretrained_models/ 폴더에 아래를 다운 받아 저장:

https://github.com/yu4u/age-gender-estimation/releases/download/v0.5/weights.28-3.73.hdf5


## Yolo 트레이닝 데이터 다운로드

**./image/yolo/data/ 폴더에 아래를 다운 받아 저장:

https://pjreddie.com/media/files/yolov3.weights
