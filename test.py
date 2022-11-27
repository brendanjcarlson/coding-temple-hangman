import unittest
from RandomWord import RandomWord
from App import App


class RandomWordTest(unittest.TestCase):

    def test_get(self):
        self.obj = RandomWord()
        test_word = self.obj.word
        test_chars = self.obj.chars
        self.assertTrue(test_word)
        self.assertListEqual(list(test_word), test_chars)

    def test_length(self):
        self.obj = RandomWord()
        test_word = self.obj.word
        test_chars = self.obj.chars
        self.assertEqual(len(test_word), len(test_chars), self.obj.length)


class AppTest(unittest.TestCase):

    def setUp(self) -> None:
        self.obj = App()

    def test_reset(self):
        self.obj.incorrect_count = 1
        self.obj.correct_count = 2
        self.obj.guessed_chars = ['a', 'b']
        self.obj.reset()

        self.assertEqual(self.obj.incorrect_count, 0)
        self.assertEqual(self.obj.correct_count, 0)
        self.assertEqual(self.obj.guessed_chars, [])

    def test_intro(self):
        pass

    def test_display_word(self):
        pass

    def test_display_banter(self):
        pass

    def test_guess(self):
        pass

    def test_check_letter(self):
        pass

    def test_again(self):
        pass

    def test_player_won(self):
        pass

    def test_player_lost(self):
        pass

    def test_play(self):
        pass


if __name__ == "__main__":
    unittest.main()
