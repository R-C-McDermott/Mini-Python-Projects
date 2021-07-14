'''
-Building a deck of cards using OOP-

To be eventually used as card game project

'''
import random # to be used for shuffling

# Card suits and values
suits = ["Hearts", "Diamonds", "Spades", "Clubs"]
values = [x for x in range(1,14)]

class Card:
    def __init__(self, suit, number):
        self.suit = suit
        self.number = number

    # Change format of some values
    def changeFormat(self, card_value):
        if card_value == 1:
            card_value = "Ace"
        if card_value == 11:
            card_value = "Jack"
        if card_value == 12:
            card_value = "Queen"
        if card_value == 13:
            card_value = "King"
        self.number = card_value

    def show(self):
        print(f"{self.number} of {self.suit}")

class Deck:
    def __init__(self):
        self.cards = []
        self.buildDeck()

    def deckSize(self):
        return len(self.cards)

    def buildDeck(self):
        for i in suits:
            for j in values:
                self.cards.append(Card(i, j))

    def printDeck(self):
        for c in self.cards:
            c.changeFormat(c.number) # changes 1, 11, 12 and 13 to Ace, Jack, Queen and King
            c.show()

    def drawCard(self):
        return self.cards.pop()

class Player:
    def __init__(self, name):
        self.name = name
        self.hand = []

    def draw(self, deck, number_of_cards):
        for i in range(number_of_cards):
            self.hand.append(deck.drawCard())

    def showHand(self):
        for h in self.hand:
            h.show()

def main():
    # Create Player and Deck
    p = Player("Ryan")
    d = Deck()

    # Check deck size
    print(f"Deck size: {d.deckSize()}")

    # Player draws hand and shows
    p.draw(d, number_of_cards=2)
    p.showHand()

    # Check deck size again to ensure everything is working properly
    print(f"Deck size: {d.deckSize()}")

if __name__ == '__main__':
    main()
