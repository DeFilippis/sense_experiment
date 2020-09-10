from otree.api import (
    models,
    widgets,
    BaseConstants,
    BaseSubsession,
    BaseGroup,
    BasePlayer,
    Currency as c,
    currency_range,
)

author = 'Philip Chapkovski, HSE'

doc = """
Sorter module. Consists of only one page, we need it only for GBAT. We can't put GBAT page at the beginning of 
any other app because under some treatments the order of apps change (DG first, DG second)
"""


class Constants(BaseConstants):
    name_in_url = 'sorter'
    players_per_group = 2
    num_rounds = 1


class Subsession(BaseSubsession):
    pass


class Group(BaseGroup):
    pass


class Player(BasePlayer):
    pass
