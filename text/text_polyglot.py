import polyglot
from polyglot.detect import Detector

def get_text_languages(texts) -> dict:
    """텍스트 언어 추출"""

    langs = []
    detector = Detector(texts)
    for lang in detector.languages:
        if lang.code is not 'un' and lang.confidence != 0.0 :
            langs.append({"code":lang.code, "confidence":lang.confidence})
    return langs

