import classes
import pytest

deck = classes.Deck()

def test_deck_size():
    assert len(deck.cards) == 52

def test_suffle_deck_size():
    deck_shuffeled = deck.shuffle_deck()
    assert len(deck_shuffeled) == 52

def test_shuffle():
    deck_shuffeled = deck.shuffle_deck()
    assert set(deck_shuffeled) == set(deck.cards)

if __name__=='__main__':
    pytest.main()
        



