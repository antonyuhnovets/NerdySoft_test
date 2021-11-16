import fire
from wordcloud import WordCloud

from config import VOCABULARY_LARGE

# Class of words data
class Vocabulary(object):

    # In constructor declare class var vocabulary
    def __init__(self, *args, **kwargs):
        self.vocabulary = []

        # Greetings!
        print('\nMy name is Anton Yukhnovets\n'
              'This is my test task for NerdySoft\n')

    # Function ask user about data for vocabulary
    def ask_user_and_fill(self):
        user_enter = input('Do you want vocabulary to be completed automatically?(y/n): ')
        answer = str(user_enter).upper()

        # If user say yes, list will be filled by config data
        if answer == ('Y' or 'YES'):
            self.vocabulary = VOCABULARY_LARGE

        # Another way - to fill vocabulary with own hands
        elif answer == ('N' or 'NO'):
            print('\nThere are two ways to fill vocabulary: '
                  '\n1 - You can do it word by word. '
                  'Use Enter to accept and start writing next one.\n'
                  'Commands "help" or "info" serve in getting information about '
                  'list length. Use "stop" to finish.'
                  '\n2 - You can enter entire list in one go. You need to use Space '
                  'button or comma as separator between words.'
                  '\nPlease choose way by writing 1 or 2!\n')

            self.set_full_vocabulary()

        # Catch bad input
        else:
            print('\nWrong enter! Please use only letter "y" as YES or "n" as NO. Try again: ')
            self.ask_user_and_fill()

        return f'Vocabulary list has {len(self.vocabulary)} elements'
        # We can use string below if we want out full vocabulary
        # return f'Vocabulary list - [{", ".join(self.vocabulary)}]'

    # Function for choice between two options and realize second one (2)
    def set_full_vocabulary(self):
        solution_way = input('')

        # First option
        if str(solution_way) == '1':
            print('You chose 1st option. Enter words one by one. '
                  'Commands "help" or "info" may be useful. When finish, write "stop".')
            self.add_word()

        # Second option
        elif str(solution_way) == '2':
            print('You chose 2nd option. Enter words list jf words with space/comma separator.\n ')

            # Input full words list and make format operations
            word_list = str(input('Enter your list: ')).lower().replace(',', ' ').split()

            # Filter list from non-alphabets symbols
            for word in word_list:
                if not word.isalpha():
                    print(f'Incorrect word {word} will not be included in vocabulary.')

                # Fill our vocabulary list with correct words
                else:
                    self.vocabulary.append(word)

        # Out number of elements
        return f'Vocabulary list has {len(self.vocabulary)} elements'

    # First option (1)
    def add_word(self):
        while True:

            # User type one word for vocabulary every cycle life
            word = str(input('')).lower()

            # Cycle running till user not write stop command
            if not word == 'stop':

                # Make sure that word correct
                if not word.isalpha():
                    print('Wrong! Only alphabet symbols can be used.')

                # Reserved info and help commands, it`s one command with two different names
                elif word == 'info' or word == 'help':
                    print(f'Vocabulary now contains {len(self.vocabulary)}. '
                          f'If you have finished filling it, you should use command "stop".')

                # Word appends in vocabulary
                else:
                    self.vocabulary.append(word)

            # Stop command activates
            else:
                break

        return f'Vocabulary list has {len(self.vocabulary)} elements'


# Child class for count words with letters and output
class WordCount(Vocabulary):
    def __init__(self, *args, **kwargs):
        super(WordCount, self).__init__()
        self.output_list = []
        self.letters = self.ask_for_letters()

    # User input letters to find
    def ask_for_letters(self):
        letters = input('Enter the letters to be found in the dictionary: \n')

        # Check input
        if str(letters).isalpha():
            return str(letters).lower()

        else:
            print('Wrong type. Please enter only alphabet letters.')
            self.ask_for_letters()

    # Function search for words with letters and count them
    def words_with_letters(self):
        for word in self.vocabulary:
            if str(self.letters) in word:
                self.output_list.append(word)

        # Call graphic output
        self.show_output(self.output_list)

        return f'{self.letters} ~~~ {len(self.output_list)} words'

    # Generating image using output
    def show_output(self, data_for_image):
        wordcloud = WordCloud().generate(' '.join(data_for_image))
        image = wordcloud.to_image()
        image.show()


# Making class object and activate in console using fire lib
def main():
    voc1 = WordCount()
    fire.Fire(voc1.ask_user_and_fill())
    fire.Fire(voc1.words_with_letters())


# Start point
if __name__ == '__main__':
    main()
