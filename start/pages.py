from otree.api import Currency as c, currency_range
from ._builtin import WaitPage
from survey_sens.generic_pages import Page
from .models import Constants
from survey_sens.pages import GameDescription


class IntroGame(Page):
    pass


class UpdGameDesc(GameDescription):
    '''Showing DG instructiongs for dg_first only'''
    template_name = 'survey_sens/GameDescription.html'

    def is_displayed(self):
        return self.session.config.get('info')


class SurveyInfoAnnouncement(Page):
    def is_displayed(self):
        return not self.session.config.get('dg_first') and self.session.config.get('info')


class FirstPartAnnouncement(Page):
    pass


page_sequence = [
    IntroGame,
    FirstPartAnnouncement,
    SurveyInfoAnnouncement,
    UpdGameDesc
]
