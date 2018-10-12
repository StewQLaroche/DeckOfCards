# Deck class

from Card import Card
import hashlib
import random


class Deck:

    def __init__(self, jokers=False):

        # Defines deck state
        self.state = []

        # Out of deck card
        self.out_of_deck = set()

        # Build default deck
        _suites = ["Spades", "Diamonds", "Clubs", "Hearts"]
        _faces = ["Ace", "2", "3", "4", "5,", "6", "7", "8", "9", "10", "Jack", "Queen", "King"]

        self.deck = {}

        for s in _suites:
            for f in _faces:

                # Create 52 instances of card
                self.deck[self.create_card_id([s, f])] = Card(s, f)

        if jokers:
            for i in range(2):

                self.deck[self.create_card_id([i])] = Card(joker="True")

        # Set default deck state
        self.state = list(self.deck.keys())

    def create_card_id(self, str_lst):

        try:
            return hashlib.md5(str("".join(str(i) for i in str_lst)).encode("utf-8")).hexdigest()
        except Exception:
            raise ValueError("Input contains value that can't be cast to string.")

    def shuffle(self, gather=False):

        if gather:
            self.state.append(card_id for card_id in self.out_of_deck)
            self.out_of_deck.clear()

        random.shuffle(self.state)

    def cut_deck(self):

        cut_index = random.randint(0, len(self.state) - 1)
        self.state = self.state[cut_index::] + self.state[0:cut_index]

    def draw_top_card(self):

        if self.state:
            card = self.state[0]
            self.out_of_deck.add(card)
            del self.state[0]
            return self.deck[card]

        return None

    def _print_deck(self):

        for card_id in self.state:
            print("%s of %s" % self.deck[card_id].get_card_info())
