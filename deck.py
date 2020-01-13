import random

colorsToNumber = {'red': 0, 'blue': 1,
                  'green': 2, 'yellow': 3}

total_numbers = 10
total_colors = 4


class Card:
    def __init__(self, number, color):
        self.number = number
        self.color = color

    def __str__(self):
        return f"[Number:{self.number}, Color: {self.color}]"


class Deck:
    def __init__(self):
        self.cards = [Card(i + 1, j + 1) for i in range(total_numbers)
                      for j in range(total_colors)]

    def __str__(self) -> str:
        return str(list(map(str, self.cards)))

    def shuffle(self) -> None:
        random.shuffle(self.cards)

    def deal(self) -> Card:
        return self.cards.pop()

    def __iter__(self):
        return self

    def __next__(self) -> Card:
        if self:
            return self.deal()
        else:
            raise StopIteration

    def __getitem__(self, item: int) -> Card:
        return self.cards[item]

    def __bool__(self) -> bool:
        if self.cards:
            return True

        return False


if __name__ == '__main__':
    # for testing: decreasing the number of cards to 4 and colors to 2
    total_numbers = 4
    total_colors = 2

    size = total_colors * total_numbers

    deck = Deck()

    print(deck)

    # shuffle works fine
    # deck.shuffle()
    # print(deck)

    print(deck.deal())
    size -= 1

    print(deck.deal())
    size -= 1

    print(deck)

    it_deck = iter(deck)
    while it_deck:
        print(next(it_deck))

    # for i in range(size):
    #    print(deck[i])
