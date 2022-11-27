import unittest
from RandomWord import RandomWord
from App import App


class RandomWordTest(unittest.TestCase):

    def setUp(self):
        self.obj = RandomWord()
        self.test_word = self.obj.word
        self.test_chars = self.obj.chars

    def test_get(self):
        res_one = self.obj.get()
        self.assertEqual(res_one, "Successfully got word.")

        self.obj.url = "https://api.api-ninjas.com/v1/intentionallybadurl"
        res_two = self.obj.get()
        self.assertEqual(res_two, "Unable to get word.")

    def test_get_setup(self):
        self.assertTrue(self.test_word)
        self.assertListEqual(list(self.test_word), self.test_chars)

    def test_length(self):
        self.assertEqual(len(self.test_word), len(
            self.test_chars), self.obj.length)


class AppTest(unittest.TestCase):

    def setUp(self):
        self.obj = App()
        self.obj.secret.word = "TESTING"

    def test_reset(self):
        self.obj.incorrect_count = 1
        self.obj.correct_count = 2
        self.obj.guessed_chars = ['A', 'B']
        self.obj.reset()
        self.assertEqual(self.obj.incorrect_count, 0)
        self.assertEqual(self.obj.correct_count, 0)
        self.assertEqual(self.obj.guessed_chars, [])

    def test_intro(self):
        pass

    def test_display_word(self):
        self.obj.guessed_chars = []
        res_one = self.obj.display_word()
        self.assertEqual(res_one, "_  _  _  _  _  _  _\n")

        self.obj.guessed_chars = ["X", "R"]
        res_two = self.obj.display_word()
        self.assertEqual(res_two, "_  _  _  _  _  _  _\n")

        self.obj.guessed_chars = ["T", "I"]
        res_three = self.obj.display_word()
        self.assertEqual(res_three, "T  _  _  T  I  _  _\n")

        self.obj.guessed_chars = ["T", "E", "S", "I", "N", "G"]
        res_four = self.obj.display_word()
        self.assertEqual(res_four, "T  E  S  T  I  N  G\n")

        self.obj.guessed_chars = ["X", "Y", "Z", "T", "E", "S", "I", "N", "G"]
        res_five = self.obj.display_word()
        self.assertEqual(res_five, "T  E  S  T  I  N  G\n")

    def test_display_guessed(self):
        self.obj.guessed_chars = ["C", "B", "A"]
        res_one = self.obj.display_guessed()
        self.assertEqual(res_one, "GUESSED LETTERS:\nA B C\n")

        self.obj.guessed_chars = ["A", "B", "C"]
        res_two = self.obj.display_guessed()
        self.assertEqual(res_two, "GUESSED LETTERS:\nA B C\n")

    def test_display_banter(self):
        res_one = self.obj.display_banter("pep")
        self.assertIn(res_one, self.obj.dialogue["banter"]["pep"])

        res_two = self.obj.display_banter("smack")
        self.assertIn(res_two, self.obj.dialogue["banter"]["smack"])

        res_three = self.obj.display_banter("win")
        self.assertIn(res_three, self.obj.dialogue["banter"]["win"])

        res_four = self.obj.display_banter("lose")
        self.assertIn(res_four, self.obj.dialogue["banter"]["lose"])

    def test_guess(self):
        pass

    def test_check_letter(self):
        pass

    def test_again(self):
        pass

    def test_player_won(self):
        self.obj.correct_count = self.obj.secret.length
        self.assertTrue(self.obj.player_won)

        self.obj.correct_count = 0
        self.assertFalse(self.obj.player_won)

        self.obj.correct_count = self.obj.secret.length - 1
        self.assertFalse(self.obj.player_won)

    def test_player_lost(self):
        self.obj.incorrect_count = 99
        self.assertTrue(self.obj.player_lost)

        self.obj.incorrect_count = self.obj.lives
        self.assertTrue(self.obj.player_lost)

        self.obj.incorrect_count = 0
        self.assertFalse(self.obj.player_lost)

    def test_play(self):
        pass


if __name__ == "__main__":
    unittest.main()
