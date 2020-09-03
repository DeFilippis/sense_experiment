from otree.api import Currency as c, currency_range
from ._builtin import WaitPage
from survey_sens.generic_pages import Page
from .models import Constants
import json


class FirstWP(WaitPage):
    group_by_arrival_time = True
    body_text = 'Please wait until we find another Toloka member...'


class QuestionnaireF(Page):
    form_model = 'player'
    form_fields = ['age',
                   'sex', 'marital_status',
                   'religion',
                   'education',
                   'occupation',
                   'relative_income_2',
                   'trust',
                   'happy',
                   'satisfaction',

                   ]


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


class BeforeResultsWP(WaitPage):
    after_all_players_arrive = 'set_payoffs'


class Results(Page):
    pass


page_sequence = [
    FirstWP,
    QuestionnaireS,
    QuestionnaireSAverage,
    RoleAnnouncement,
    BeforeDictatorWP,
    DictatorSender,
    DictatorReceiver,
    DictatorSenderExpected,
    BeforeResultsWP,
    QuestionnaireF,
    Results,
]
