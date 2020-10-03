from otree.api import Currency as c, currency_range
from ._builtin import Page, WaitPage
from .models import Constants



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


page_sequence = [
    QuestionnaireF
]
