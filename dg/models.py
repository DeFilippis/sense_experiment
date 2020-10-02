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
Dictator's game module for sensitivity experiment
"""


class Constants(BaseConstants):
    name_in_url = 'dg'
    players_per_group = 2
    num_rounds = 1
    endowment = 100


class Subsession(BaseSubsession):
    pass


class Group(BaseGroup):
    sent_amount = models.CurrencyField(
        max=c(100),
        min=c(0),
        label=f"How much do you want to send to another participant (Recipient)? Choose any amount from 0 to 100 cents"
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

    def get_other_answer(self):
        # todo very rough naive fix. should be redone completely
        other = self.get_others_in_group()[0]
        return other.participant.survey_sens_player.first().get_other_answer()
