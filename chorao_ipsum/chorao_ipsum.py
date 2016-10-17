from random import choice, randint


class ChoraoIpsum:
    CHORATIM_POOL = [
        'Santos',
        'skate',
        'charlie',
        'brown',
        'vagabundo',
        'Charlie Brown',
        'vagabundo skate',
        'vagabundo Santos',
    ]

    def __init__(self, choratim_count):
        self.count = choratim_count
        self.step = 1

    def get_initial_text(self):
        return 'Chorão Ipsum'

    def get_text(self):
        text = self.get_initial_text()
        for i in range(self.count):
            text += self.generate_choratim()
            self.step -= 1
        return text + '.'

    def generate_choratim(self):
        choratim = choice(self.CHORATIM_POOL)
        return self.embed_punctuation(choratim)

    def embed_punctuation(self, choratim):
        punctuation = ' '
        if self.step == 0:
            self.step = randint(2, 10)

            if choice([True, False]):
                punctuation = '. '
                choratim = choratim.capitalize()
            else:
                punctuation = ', '

        return punctuation + choratim

