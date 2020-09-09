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


author = 'Your name here'

doc = """
Your app description
"""


class Constants(BaseConstants):
    name_in_url = 'dg'
    players_per_group = None
    num_rounds = 1


class Subsession(BaseSubsession):
    pass


class Group(BaseGroup):
    sent_amount = models.CurrencyField(
        max=c(100),
        min=c(0),
        label=f"How much do you want to send to another participant (Recipient)? (choose any amount from 0 to 100 cents)"
    )

    expected_sender = models.CurrencyField(
        max=c(100),
        min=c(0),
        label=""
    )

    expected_receiver = models.CurrencyField(
        max=c(100),
        min=c(0),
        label=""
    )

    def set_payoffs(self):
        dictator = self.get_player_by_role('dictator')
        receiver = self.get_player_by_role('receiver')
        dictator.payoff = Constants.endowment - self.sent_amount
        receiver.payoff = self.sent_amount


class Player(BasePlayer):
    def role(self):
        if self.id_in_group == 1:
            return 'dictator'
        else:
            return 'receiver'
    def role_desc(self):
        """Return russian description of role"""
        descs = dict(dictator="Sender",
                     receiver="Receiver")
        return descs.get(self.role())
