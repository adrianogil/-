
class Game:
    def __init__(self):
        self.wordlist_file = '../data/wordlist.txt'
        self.load_wordlist()

    def load_wordlist(self):

        with open(self.wordlist_file, 'r') as f:
            wordlist_lines = f.readlines()

        wordlist = []

        for w in wordlist_lines:
            wordlist.append(w.strip())

        self.wordlist = wordlist


    def find_word(self, word):
        for w in self.wordlist:
            if w[0] == word[len(word)-1]:
                return w

    def play(self):
        next_word = "끝말잇기\n"

        is_playing = True

        game_turns = 0

        while is_playing:
            player_word = input(next_word + "\n>")

            if game_turns > 0 and \
                (player_word.strip() == "" or player_word[0] != next_word[len(next_word)-1]):
                print('Game Over!')
                exit(0)

            next_word = self.find_word(player_word)

            is_playing = next_word is not None

        print('You win!')

game = Game()
game.play()


