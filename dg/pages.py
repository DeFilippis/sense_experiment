from otree.api import Currency as c, currency_range
from ._builtin import Page, WaitPage
from .models import Constants


class FirstWP(WaitPage):
    def is_displayed(self):
        return self.session.config.get('baseline')

    group_by_arrival_time = True
    body_text = 'Please wait until we find another Toloka member...'


class IntroGame(Page):
    pass


class GameDescription(Page):
    show_instructions = True


class RoleAnnouncement(Page):
    show_instructions = True


class BeforeDictatorWP(WaitPage):
    pass


class DictatorSender(Page):
    show_instructions = True
    form_model = 'group'
    form_fields = ['sent_amount']

    def is_displayed(self):
        return self.player.role() == 'dictator'


class DictatorReceiver(Page):
    show_instructions = True
    form_model = 'group'
    form_fields = ['expected_receiver']

    def is_displayed(self):
        return self.player.role() == 'receiver'


class DictatorSenderExpected(Page):
    show_instructions = True
    form_model = 'group'
    form_fields = ['expected_sender']

    def is_displayed(self):
        return self.player.role() == 'dictator'


page_sequence = [
    FirstWP,
    RoleAnnouncement,
    BeforeDictatorWP,
    DictatorSender,
    DictatorReceiver,
    DictatorSenderExpected,
]
