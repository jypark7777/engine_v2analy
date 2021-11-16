import unittest
import text_polyglot

class TextPolyglotTest(unittest.TestCase):

    def test_text_languages(self):
        texts = "동해물과 백두산이"
        langs = text_polyglot.get_text_languages(texts)
        self.assertIn({"code":'ko', "confidence":96.0}, langs)


if __name__ == '__main__':
    unittest.main()