# from HangmanArt import HangmanArt
# from RandomWord import RandomWord
# import time
# import random
from HangmanArt import HangmanArt
from RandomWord import RandomWord
import time
import random


class App:
    TEXT = {"intro": {"welcome": "~~~~~~~~~~~ WELCOME TO HANGMAN, PARTNER! ~~~~~~~~~~~\n",
                      "hol_up": "Wait a minute... I ain't seen you 'round here before...\n",
                      "rule_check": "You know what this here game is about? (Y)es or (n)o?\n",
                      "brave": "\nWell, well, well... We got a brave one... Step on up and let's see what you're made of.\n",
                      "fresh": "\nYEEHAW! We got a fresh one, folks!\n",
                      "gentleman": "Just 'cause I'm a... 'sophisticated' gentlemen, here is a quick run down of how things are done 'round here:\n",
                      "rule_1": "1) We're gonna choose a random word.",
                      "rule_2": "2) Each turn you're gonna try to guess a letter in that there word.",
                      "rule_3": "3) If you guess wrong, well, shoot... You're one step closer to the grave. 7 wrong guesses and you're gone.",
                      "rule_4": "4) If you're able to guess all the letters in the word, we might just let ya walk away with your life.\n",
                      "play": "\nLET'S PLAY!\n", },
            "inputs": {"invalid": "Speak up now! (Y)es or (n)o?",
                       "guess": "Guess a letter.\n",
                       "long": "You're only allowed to guess one letter at a time... Try again.\n",
                       "num_sym": "Ain't no numbers or symbols in these words. Guess a letter.\n",
                       "repeat": "\nYou've already guessed that one...\nTry another.\n",
                       "play_again": "You interested in goin' again? (Y)es or (n)o.\n",
                       "agane": "\nWE GO AGAIN! YEEHAW!\n",
                       "walk_away": "\nThat's a good call, partner... Walk away while you still can.",
                       "warning": "A word of advice, I wouldn't come back 'round this way if I were you...\n", },
            "banter": {"pep": ["Lucky...\n", "Nice one.", "Look at you go...\n"],
                       "smack": ["Not even close...\n", "You really thought that one would be in there?\n", "Woah buddy. Slow down and think before you guess.\n"],
                       "win": ["We'll let you off easy this time...\n"],
                       "lose": ["Lord almighty you're so stupid we aren't even gonna hang ya... Idiot...\n"],
                       },
            }

    def __init__(self):
        self.secret = RandomWord()
        self.incorrect_count = 0
        self.correct_count = 0
        self.guessed_chars = []
        self.lives = 7
        self.visual = HangmanArt()
        self.dialogue = self.TEXT

    # GENERATES NEW WORD AND RESETS GAME VARIABLES
    def reset(self):
        self.secret = RandomWord()
        self.incorrect_count = 0
        self.correct_count = 0
        self.guessed_chars = []

    # ASKS USER IF THEY KNOW THE RULES
    def intro(self):
        print(self.dialogue["intro"]["welcome"])
        time.sleep(1)
        print(self.dialogue["intro"]["hol_up"])
        time.sleep(2)
        user_rule_check = input(self.dialogue["intro"]["rule_check"]).lower()
        introing = True
        while introing:
            if user_rule_check.startswith("y"):
                introing = False
                time.sleep(1)
                print(self.dialogue["intro"]["brave"])
            elif user_rule_check.startswith("n"):
                introing = False
                time.sleep(1.5)
                print(self.dialogue["intro"]["fresh"])
                time.sleep(1)
                print(self.dialogue["intro"]["gentleman"])
                time.sleep(2.5)
                print(self.dialogue["intro"]["rule_1"])
                time.sleep(1)
                print(self.dialogue["intro"]["rule_2"])
                time.sleep(1)
                print(self.dialogue["intro"]["rule_3"])
                time.sleep(1)
                print(self.dialogue["intro"]["rule_4"])
            else:
                time.sleep(1)
                user_rule_check = input(self.dialogue["inputs"]["invalid"])

        time.sleep(2)
        print(self.dialogue["intro"]["play"])

    # GENERATES STRING TO BE OUTPUT BASED ON CORRECT GUESSES
    def display_word(self):
        output = ''
        for char in self.secret.word:
            if char in self.guessed_chars:
                output += f" {char} "
            else:
                output += " _ "
        return f"{output.lstrip(' ')}\n"

    # GETS ASCII ART FOR AMOUNT OF LIVES REMAINING
    def display_art(self):
        return self.visual.art[self.incorrect_count]

    # TALKS SCHMIT OR GASSES UP THE PLAYER
    def display_banter(self, banter_type):
        if banter_type:
            return random.choice(self.dialogue["banter"][banter_type])

    # SELF EXPLANATORY
    def display_guessed(self):
        return f"GUESSED LETTERS:\n{' '.join(sorted(self.guessed_chars))}\n"

    # JUST CLEANS UP DRIVER CODE
    def display_all(self, banter_type=""):
        print(self.display_art())
        print(self.display_word())
        print(self.display_guessed())
        print(self.display_banter(banter_type))

    # TAKES IN USER GUESS AND ADDS IT TO GUESSED CHARACTERS LIST
    def guess(self):
        user_guess = input(self.dialogue["inputs"]["guess"]).upper()
        guessing = True
        while guessing:
            if len(user_guess) > 1:
                user_guess = input(self.dialogue["inputs"]["long"]).upper()
            elif not user_guess.isalpha():
                user_guess = input(self.dialogue["inputs"]["num_sym"]).upper()
            elif user_guess in self.guessed_chars:
                user_guess = input(self.dialogue["inputs"]["repeat"]).upper()
            else:
                self.guessed_chars.append(user_guess)
                guessing = False
        return user_guess

    # CHECKS IF USER GUESS IS IN THE SECRET WORD AND UPDATES SCORE
    def check_letter(self, guess):
        if guess not in self.secret.word:
            self.incorrect_count += 1
            return 'smack'
        else:
            self.correct_count += self.secret.chars.count(guess)
            return 'pep'

    # ASKS USER IF THEY WANT TO PLAY AGAIN
    def again(self):
        time.sleep(1)
        user_again = input(self.dialogue["inputs"]["play_again"])
        againing = True
        while againing:
            if user_again.startswith('y'):
                self.reset()
                againing = False
                print(self.dialogue["inputs"]["agane"])
                time.sleep(2)
                return True
            elif user_again.startswith('n'):
                print(self.dialogue["inputs"]["walk_away"])
                time.sleep(2)
                print(self.dialogue["inputs"]["warning"])
                againing = False
                return False
            else:
                time.sleep(1)
                user_again = input(self.dialogue["inputs"]["invalid"])

    @property
    def player_won(self):  # True only if player has guessed all letters correctly, else False
        return self.correct_count == self.secret.length

    @property
    def player_lost(self):  # 7+ wrong guesses -> True, else False
        return self.incorrect_count >= self.lives

    # DRIVER CODE
    def play(self):
        self.intro()
        playing = True
        while playing:

            gamin = True
            while gamin:
                if self.player_won or self.player_lost:
                    if self.player_won:
                        self.display_all("win")
                    else:
                        self.display_all("lose")
                        print(f"The word was {self.secret.word}.\n")
                    gamin = False
                    self.reset()
                else:
                    if not self.guessed_chars:
                        print(self.display_art())
                        print(self.display_word(), "\n\n")
                    user_letter = self.guess()
                    banter_type = self.check_letter(user_letter)
                    self.display_all(banter_type)

            playing = self.again()


if __name__ == "__main__":
    hangman = App()
    hangman.play()
