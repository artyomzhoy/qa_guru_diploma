from random import randint


def tag():
    tags = ['animal',
            'parrot',
            'dog',
            'cat',
            'kitty',
            'car',
            'drums']
    return tags[randint(0, len(tags) - 1)]


def user():
    tags = ['WeirdAlisMySpiritUserName',
            'Luggagagagagagaga',
            'cKittenSmasher',
            'bjornenlinda',
            'Cyberball2073',
            'Locopogo',
            'ARussianAndHisBike']
    return tags[randint(0, len(tags) - 1)]
