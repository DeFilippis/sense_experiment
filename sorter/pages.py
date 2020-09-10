from otree.api import Currency as c, currency_range
from ._builtin import Page, WaitPage
from .models import Constants


class FirstWP(WaitPage):
    def is_displayed(self):
        return not self.session.config.get('baseline')
    group_by_arrival_time = True
    body_text = 'Please wait until we find another Toloka member...'


class FirstPartAnnouncement(Page):
    pass


page_sequence = [
    FirstWP,
    FirstPartAnnouncement
]
