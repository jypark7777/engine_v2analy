import urllib.request, urllib.parse, time, traceback
import os
import datetime

def delete_old_files(path_target, elapsed):
    """path_target:삭제할 파일이 있는 디렉토리, elapsed:경과 초"""
    for f in os.listdir(path_target): # 디렉토리를 조회한다
        f = os.path.join(path_target, f)
        if os.path.isfile(f): # 파일이면
            timestamp_now = datetime.now().timestamp() # 타임스탬프(단위:초)
            # st_mtime(마지막으로 수정된 시간)기준 X일 경과 여부
            is_old = os.stat(f).st_mtime < timestamp_now - elapsed
            if is_old: # X일 경과했다면
                try:
                    os.remove(f) # 파일을 지운다
                    print(f, 'is deleted') # 삭제완료 로깅
                except OSError: # Device or resource busy (다른 프로세스가 사용 중)등의 이유
                    print(f, 'can not delete') # 삭제불가 로깅

def get_url_image_file(path_url):
    path_url_encode = path_url.replace("://", ":\\\\")
    # path_url_encode = urllib.parse.quote(path_url_encode)

    file_path = f"image/temp/{path_url_encode}"
    try:
        os.makedirs(file_path)
    except:
        pass

    file_path = f"{file_path}/image.jpg"

    print(path_url_encode)

    # delete_old_files(file_path, 3600)

    try:
        if os.path.isfile(file_path):
            return file_path
        
        urllib.request.urlretrieve(path_url, file_path)
        return file_path
    except:
        return None

get_url_image_file("https://scontent-waw1-1.cdninstagram.com/v/t51.2885-15/sh0.08/e35/s640x640/225456923_1489438378080959_8685637137734523818_n.jpg?_nc_ht=scontent-waw1-1.cdninstagram.com&_nc_cat=111&_nc_ohc=nUI85foQCtsAX_GeSXq&edm=ABfd0MgBAAAA&ccb=7-4&oh=e1bde14bb4d49a71a81f511b757afa65&oe=6174E02E&_nc_sid=7bff83")