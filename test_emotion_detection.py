from EmotionDetection.emotion_detection import emotion_detector as detect
import unittest

class TestEmotionDetector(unittest.TestCase):
    def test_emotion_detector(self):
        text_1 = "I am glad this happened"
        text_2 = "I am really mad about this"
        text_3 = "I feel disgusted just hearing about this"
        text_4 = "I am so sad about this"
        text_5 = "I am really afraid that this will happen"
        result_1 = detect(text_1) # joy
        result_2 = detect(text_2) # anger
        result_3 = detect(text_3) # disgust
        result_4 = detect(text_4) # sadness
        result_5 = detect(text_5) # fear
        self.assertEqual(result_1['dominant_emotion'], 'joy')
        self.assertEqual(result_2['dominant_emotion'], 'anger')
        self.assertEqual(result_3['dominant_emotion'], 'disgust')
        self.assertEqual(result_4['dominant_emotion'], 'sadness')
        self.assertEqual(result_5['dominant_emotion'], 'fear')        

if __name__ == "__main__":
    unittest.main()