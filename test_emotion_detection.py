"""
Unit Tests for Emotion Detection Package
"""
import unittest
from EmotionDetection.emotion_detection import emotion_detector

class TestEmotionDetection(unittest.TestCase):
    """
    Test cases for emotion_detector function.
    """
    def test_emotion_detector(self):
        """
        Tests emotion detection statements for joy, anger, disgust, fear, and sadness.
        """
        # Test case 1: Joy
        result_1 = emotion_detector('I am glad this happened')
        self.assertEqual(result_1['dominant_emotion'], 'joy')

        # Test case 2: Anger
        result_2 = emotion_detector('I am really angry about this')
        self.assertEqual(result_2['dominant_emotion'], 'anger')

        # Test case 3: Disgust
        result_3 = emotion_detector('I feel disgusted just thinking about this')
        self.assertEqual(result_3['dominant_emotion'], 'disgust')

        # Test case 4: Fear
        result_4 = emotion_detector('I am so afraid that this will happen')
        self.assertEqual(result_4['dominant_emotion'], 'fear')

        # Test case 5: Sadness
        result_5 = emotion_detector('I am so sad about this')
        self.assertEqual(result_5['dominant_emotion'], 'sadness')

if __name__ == '__main__':
    unittest.main()
