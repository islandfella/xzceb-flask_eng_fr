import unittest
from translator import english_to_french, french_to_english

class TranslatorTestCase(unittest.TestCase):
    
    def test_english_to_french_translation(self):
        # Test English to French translation
        result = english_to_french('Hello')
        self.assertEqual(result, 'Bonjour')

    def test_french_to_english_translation(self):
        # Test French to English translation
        result = french_to_english('Bonjour')
        self.assertEqual(result, 'Hello')

if __name__ == '__main__':
    unittest.main()
