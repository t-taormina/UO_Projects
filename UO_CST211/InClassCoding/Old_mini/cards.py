"""Playing cards (Poker deck) encoded
as one-byte integers
"""

import enum
from typing import Tuple, List

class CardSuit(enum.Enum):
    value: int      # Hint to typechecker
    Hearts = 0
    Diamonds = 1
    Spades = 2
    Clubs = 3

class CardRank(enum.Enum):
    value: int      # Hint to typechecker
    Ace = 1
    Two = 2
    Three = 3
    Four = 4
    Five = 5
    Six = 6
    Seven = 7
    Eight = 8
    Nine = 9
    Ten = 10
    Jack = 11
    Queen = 12
    King = 13

# Note we need 6 bits total for a card
#   Bits 0..3 for CardRank (4 bits)
#   Bits 4..5 for CardSuit (2 bits)
RANK_MASK = 0b1111
SUIT_MASK = 0b11
CARD_MASK = 0b11_1111
RANK_SHIFT = 4
HAND_SHIFT = 6


def encode(rank: CardRank, suit: CardSuit) -> int:
    suit_bin = suit.value << RANK_SHIFT
    rank_bin = rank.value
    card = suit_bin | rank_bin
    return card

def decode(card: int) -> Tuple[CardRank, CardSuit]:
    rank = card & RANK_MASK
    suit = (card >> RANK_SHIFT) & SUIT_MASK
    return (CardRank(rank), CardSuit(suit))

def desc(card: int):
    rank, suit = decode(card)
    return f"{rank.name} of {suit.name}"

def pack_hand(cards: List[Tuple[CardRank, CardSuit]]) -> int:
    """Pack a list of 5 (rank, suit) pairs into
    30 bits of an integer.
    """
    assert len(cards) == 5
    hand = 0

    for i in range(len(cards)):
        rank, suit = cards[i]
        card = encode(rank, suit)
        hand = (hand << HAND_SHIFT) | card

    return hand


def unpack_hand(packed: int) -> List[Tuple[CardRank, CardSuit]]:
    """Inverse of pack_hand: Unpack a single integer
    into a list of 5 (CardRank, CardSuit) pairs.
    """
    #poker hand has 5 cards
    hand = []
    for i in range(5):
        card_bin = packed & CARD_MASK
        packed = packed >> HAND_SHIFT
        rank, suit = decode(card_bin)
        hand.append((rank, suit))

    hand.reverse() # works like append in that it return None and changes list in place
    return hand

def main():
    """Smoke test"""
    card = encode(CardRank.Jack, CardSuit.Hearts)
    print(f"Jack of Hearts => {card} => {desc(card)}")
    card = encode(CardRank.Ace, CardSuit.Spades)
    print(f"Ace of Spades => {card} => {desc(card)}")
    card = encode(CardRank.Four, CardSuit.Diamonds)
    print(f"Four of Diamonds => {card} => {desc(card)}")
    card = encode(CardRank.King, CardSuit.Clubs)
    print(f"King of Clubs => {card} => {desc(card)}")

    # Expected output:
    # Jack of Hearts => 11 => Jack of Hearts
    # Ace of Spades => 33 => Ace of Spades
    # Four of Diamonds => 20 => Four of Diamonds
    # King of Clubs => 61 => King of Clubs

    hand = [(CardRank.King, CardSuit.Diamonds),
            (CardRank.Queen, CardSuit.Hearts),
            (CardRank.Jack, CardSuit.Clubs),
            (CardRank.Ten, CardSuit.Spades),
            (CardRank.Ace, CardSuit.Diamonds)]
    packed = pack_hand(hand)
    # Result should be an integer, in 30 bits.
    # It should therefore be less than 2^30.
    assert packed < (1 << 30), "Should fit in 30 bits"
    unpacked = unpack_hand(packed)
    assert unpacked == hand, "Should be the same"
    print("Hand:")
    for rank, suit in unpacked:
        print(f"{rank.name} of {suit.name}")


if __name__ == "__main__":
    main()


