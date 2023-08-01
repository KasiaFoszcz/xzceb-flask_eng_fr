import unittest
import translator

class TestTranslator(unittest.TestCase):
    english_word = "Hello"
    french_word = "Bonjour"

    def test_english_to_french_correct(self):
        message = "English word wasn't properly translated into French."
        self.assertEqual(
            translator.english_to_french(self.english_word), 
            self.french_word, 
            message
        )
  
    def test_english_to_french_incorrect(self):
        message = "English word wasn't translated into French."
        self.assertNotEqual(
            translator.english_to_french(self.english_word), 
            self.english_word, 
            message
        )

    def test_french_to_english_correct(self):
        message = "French word wasn't properly translated into English."
        self.assertEqual(
            translator.french_to_english(self.french_word), 
            self.english_word, 
            message
        )

    def test_french_to_english_incorrect(self):
        message = "French word wasn't translated into English."
        self.assertNotEqual(
            translator.french_to_english(self.french_word), 
            self.french_word, 
            message
        )

if __name__ == '__main__':
    unittest.main()
    