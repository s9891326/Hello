from behave import *

from hello_behavior.module.card import change_card_name_to_card
from hello_behavior.module.player import Player


# use_step_matcher("re")
# @then("(?P<player_name>.+) 沒出局")
# def player_not_out(context, player_name):
#     """
#     :type context: behave.runner.Context
#     :param player_name:
#     """
#     out_player = getattr(context, player_name)
#     assert not out_player.am_i_out, f"player_name: {player_name} is out."


@given("{player_name} 持有 {cards:S}")
def player_hold_card(context, player_name, cards):
    """
    :type context: behave.runner.Context
    :type player_name: str
    :type cards: str
    """
    player = Player(player_name, cards.split(","))
    setattr(context, player_name, player)


@given("{player_name} 持有 {cards:S} 侍女保護中")
def player_hold_card_protected(context, player_name, cards):
    """
    :type context: behave.runner.Context
    :type player_name: str
    :type cards: str
    """
    player = Player(player_name, cards.split(","))
    player.protected = True
    setattr(context, player_name, player)


@when("{player_name_a} 對 {player_name_b} 出 {play_card} 指定 {card}")
def player_play_guard(context, player_name_a, player_name_b, play_card, card):
    """
    :type context: behave.runner.Context
    :type player_name_a: str
    :type player_name_b: str
    :type play_card: str
    :type card: str
    """
    active_player = getattr(context, player_name_a)
    inactive_player = getattr(context, player_name_b)
    active_player.play(
        inactive_player,
        change_card_name_to_card(play_card),
        change_card_name_to_card(card)
    )


@then("{player_name} 出局")
def player_out(context, player_name):
    """
    :type context: behave.runner.Context
    :type player_name: str
    """
    out_player = getattr(context, player_name)
    assert out_player.am_i_out, f"player_name: {player_name} is not out."


@then("{player_name} 沒出局")
def player_not_out(context, player_name):
    """
    :type context: behave.runner.Context
    :param player_name:
    """
    out_player = getattr(context, player_name)
    assert not out_player.am_i_out, f"player_name: {player_name} is out."
