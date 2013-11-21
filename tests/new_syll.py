# New syllable counting measures

class SyllableMachine():
    def __init__(self, word_input):
        self.word_input = word_input
        self.vowels     = 'aeiou'
        self.consonants = 'bcdfghjklmnpqrstvwxz'
        self.dipthongs  = ['ou', 'ie', 'oo', 'oi', 'ea', 'ee', 'ai', 'ae']
        self.y_as_vowel = 'y'
        self.re_vowel   = 're
        self.processed  = self.word_input.lower()

