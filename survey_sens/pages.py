from otree.api import Currency as c, currency_range
from ._builtin import WaitPage
from survey_sens.generic_pages import Page
from .models import Constants
import json


class PartBeginningAnnouncement(Page):
    def is_displayed(self):
        return self.session.config.get('dg_first')

class QuestionnaireS(Page):
    # TODO: do order randomization in a proper way
    form_model = 'player'
    show_instructions = True
    info = True

    def get_form_fields(self):
        fields = json.loads(self.player.q_order)
        return [f for f in fields if not f.startswith('average')]


class QuestionnaireSAverage(Page):
    form_model = 'player'
    show_instructions = True
    template_name = 'survey_sens/QuestionnaireS.html'

    def get_form_fields(self):
        fields = json.loads(self.player.q_order)
        return [f for f in fields if f.startswith('average')]


class BeforeResultsWP(WaitPage):
    after_all_players_arrive = 'set_payoffs'


class OtherInfoWP(WaitPage):
    def is_displayed(self):
        return self.session.config.get('info')


class OtherInfo(Page):
    def is_displayed(self):
        """We show other member's answer only  under info treatments
        No matter if this is DG first treatment or full treatment where
        in addition they get another member answer at dictator's decision page.
        """
        return self.session.config.get('info')


class NextPartAnnouncement(Page):
    def is_displayed(self):
        """We don't have a dg after that if dg goes first so we skip this announcmenet.
        """
        return not self.session.config.get('dg_first')


class GameDescription(Page):
    def is_displayed(self):
        """
        So it's a kind of a mess with this gamedescription page. Let's talk it through here.
        there are three possible scenarios aka treatments.
        1. baseline. they play sens.q first and then passed to DG. they DO NOT KNOW about the existence and
        essence of DG when they are in sens.q. but they also are not aware of the presence of a partner.
        that is why we show GameDescription before grouping wp. (which is here).

        2. dg first. here the DG goes first, and sens.q goes second. No need to show game description
        at the end of sens.q, but somewhere we need to show it, right? So in dg first the order is the following:
        intro, dg, sens.q. so in this scenario we show gamedescription at the end of intro.
        they are matched into groups at the beginning of dg. then we show

        3. full info treatment. here they get the announcmenet that they play dg before sensq, and before that
        they are informed that they first will answer sens.q. So:
        instructions (dg) first + announcmenet that their info may be shown at dg. so again this will happen
        at the end of intro (aka start).
        then we group.
        Then sens.q (with the announcmenet). Then we show the other info (otherinfo page above).
        then we proceed to dg where show info of another member once again.



        :return: true/false
        :rtype: bool
        """
        return not self.session.config.get('dg_first')


page_sequence = [
    PartBeginningAnnouncement,
    QuestionnaireS,
    QuestionnaireSAverage,
    OtherInfoWP,
    OtherInfo,
    NextPartAnnouncement,
    GameDescription

]
