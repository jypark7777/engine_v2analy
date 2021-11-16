from konlpy.tag import Mecab
from konlpy.tag import Okt
import re,json

from collections import Counter, OrderedDict

def _clean_str(text):
    """순수 텍스트워드으로 치환"""
    pattern = '([a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+)' # E-mail제거
    text = re.sub(pattern=pattern, repl='', string=text)
    pattern = '(http|ftp|https)://(?:[-\w.]|(?:%[\da-fA-F]{2}))+' # URL제거
    text = re.sub(pattern=pattern, repl='', string=text)
    pattern = '([ㄱ-ㅎㅏ-ㅣ]+)'  # 한글 자음, 모음 제거
    text = re.sub(pattern=pattern, repl='', string=text)
    pattern = '<[^>]*>'         # HTML 태그 제거
    text = re.sub(pattern=pattern, repl='', string=text)
    pattern = '[^\w\s]'         # 특수기호제거
    text = re.sub(pattern=pattern, repl='', string=text)
    return text

async def get_text_rank(texts, min_word_length=2) -> dict:
    """문장을 자주 나오는 단어 빈도수로 리턴
     Args:
        texts : 텍스트 문장
        min_word_length : 검출할 최소 단어 길이
    """
    mecab = Okt()
    nouns = mecab.nouns(texts)
    print(nouns)

    if len(texts) > 0 and len(nouns) == 0:
        text = _clean_str(texts)
        text = text.replace('\n','')
        nouns = text.split(' ')
    
    res = list(filter(lambda ele: len(ele) >= min_word_length, nouns))
    count = Counter(res)
    print(count.most_common())
    return count.most_common()

# get_text_rank("이것은 메캅 메캅 테스트입니다. 사용자 사전을 등록하기 사용자 전입니다. 사용자 비타500")
