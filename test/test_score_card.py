import pytest
from src.score_card import ScoreCard


@pytest.mark.state_n
def test_hitting_pins_regular():
    pins = "12345123451234512345"
    total = 60
    assert ScoreCard(pins).score() == total


@pytest.mark.state_n
def test_symbol_zero():
    assert ScoreCard("9-9-9-9-9-9-9-9-9-9-").score() == 90
    assert ScoreCard("9-3561368153258-7181").score() == 82


@pytest.mark.spare
def test_spare_not_extra():
    assert ScoreCard("9-3/613/815/-/8-7/8-").score() == 121


@pytest.mark.strike
def test_strike():
    assert ScoreCard("X9-9-9-9-9-9-9-9-9-").score() == 100
    assert ScoreCard("X9-X9-9-9-9-9-9-9-").score() == 110


@pytest.mark.strike
def test_two_strikes():
    assert ScoreCard("XX9-9-9-9-9-9-9-9-").score() == 120


@pytest.mark.strike
def test_three_strikes():
    assert ScoreCard("XXX9-9-9-9-9-9-9-").score() == 141


@pytest.mark.extra_rolls
def test_one_pin_in_extra_roll():
    assert ScoreCard("9-3/613/815/-/8-7/8/8").score() == 131
    assert ScoreCard("5/5/5/5/5/5/5/5/5/5/5").score() == 150


@pytest.mark.extra_rolls
def test_two_strikes_in_extra_rolls():
    assert ScoreCard("9-9-9-9-9-9-9-9-9-XXX").score() == 111


@pytest.mark.extra_rolls
def test_one_strike_in_extra_roll():
    assert ScoreCard("8/549-XX5/53639/9/X").score() == 149


@pytest.mark.extra_rolls
def test_spare_in_extra_roll():
    assert ScoreCard("X5/X5/XX5/--5/X5/").score() == 175


@pytest.mark.extra_rolls
def test_triple_strike_before_extra_rolls():
    assert ScoreCard("XXXXXXXXXXXX").score() == 300
