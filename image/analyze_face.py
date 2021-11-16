from deepface import DeepFace
import urllib.request, time, traceback
import random, os
from .pyagender.pyagender import PyAgender
import cv2
from image.image_utils import get_url_image_file

# https://github.com/serengil/deepface
def analyze_face(path_url, actions=['age', 'gender', 'race', 'emotion'], engine="pyagender"):
	"""얼굴 분석하기

	Args:
		engine : pyagender - Py-agender Lib, deepface - DeepFace Lib
	
	"""

	# file_path = f"image/temp/{time.time()}.{random.random()}.jpg"
	# urllib.request.urlretrieve(path_url, file_path)
	file_path = get_url_image_file(path_url)
	if file_path == None:
		return None

	results = []
	
	try:
		
		if engine == "pyagender":
			agender = PyAgender() 
			result = {}
			detect_genders_ages = agender.detect_genders_ages(cv2.imread(file_path))
			print(results)
			for item in detect_genders_ages[:5]:
				
				result = dict()
				if 'age' in actions:
					result['age'] = float(item['age'])
				if 'gender' in actions:
					gender =  "woman" if float(item['gender']) > 0.50 else 'man'
					result['gender'] = gender
				print(result)
				result['region'] = {'x': item['left'], 'y': item['top'], 'w':item['width'], 'h':item['height']}
				results.append(result)
		else:
			backends = ['opencv', 'ssd', 'dlib', 'mtcnn', 'retinaface']
			result = DeepFace.analyze(img_path = file_path, actions = actions, detector_backend = backends[4], prog_bar=False)
			results.append(result)
		"""
        [
			{
				"region": {'x': 230, 'y': 120, 'w': 36, 'h': 45},
				"age": 28.66,
				"gender": "woman",
				"dominant_emotion": "neutral",
				"emotion": {
					'sad': 37.65260875225067,
					'angry': 0.15512987738475204,
					'surprise': 0.0022171278033056296,
					'fear': 1.2489334680140018,
					'happy': 4.609785228967667,
					'disgust': 9.698561953541684e-07,
					'neutral': 56.33133053779602
				}
				"dominant_race": "white",
				"race": {
					'indian': 0.5480832420289516,
					'asian': 0.7830780930817127,
					'latino hispanic': 2.0677512511610985,
					'black': 0.06337375962175429,
					'middle eastern': 3.088453598320484,
					'white': 93.44925880432129
				}
			}
		]
        """
		print(results)
		# os.remove(file_path)
	except ValueError:
		return {}
	
	return results


def predict_age_gender(path_url):
    """얼굴 나이 성별, 예측하기"""
	
    return analyze_face(path_url=path_url, actions=['age', 'gender'])