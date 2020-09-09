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
from .widgets import LikertWidget
import json
import random
from django.template.loader import render_to_string
from django.utils.safestring import mark_safe

author = 'Philipp Chapkovski'

doc = """
Dictator game, social conformity game.
"""


class Constants(BaseConstants):
    name_in_url = 'survey_sens'
    players_per_group = 2
    num_rounds = 1
    Range010 = range(0, 11)
    endowment = 100
    average_quote = "In your opinion, how did the participants in this study on average answer the previous question?"
    q_to_show = 'homosexuality_attitude'
    sensquestions = [
        ['homosexuality_attitude',
         'average_choice_homosexuality', ],
        ['gender_roles_attitude',
         'average_choice_gender_roles', ],
        ['authority_attitude',
         'average_choice_authority'],
    ]
    HOMO_Q = "What is your attitude towards homosexual people, gays, lesbians?"
    GENDER_Q = "To what extent you agree with the statement: It's up to the husband to make money, and it's up to the wife to run the house and take care of the family...'"
    PUTIN_Q = "How do you think V. Putin copes with the President's duties?"
    PREV_PREFIX = mark_safe('<b>Previously we asked</b>')


def iwrapper(s):
    return f'<i>{s}</i>'


class Subsession(BaseSubsession):
    def creating_session(self):
        for p in self.get_players():
            newqs = Constants.sensquestions.copy()
            random.shuffle(newqs)
            flatten_qs = [item for sublist in newqs for item in sublist]
            p.q_order = json.dumps(flatten_qs)


class Group(BaseGroup):
    pass


class Player(BasePlayer):


    @property
    def other(self):
        return self.get_others_in_group()[0]

    def get_other_answer(self):
        """we fix the logic here showing only homosexuality question to show in info treatment.
        But we can show any other question as well by changing the param in constants.
        """
        to_show = Constants.q_to_show
        to_show_value = getattr(self.other, to_show)
        to_show_meta = self._meta.get_field(to_show)

        choices = to_show_meta.choices
        widget = to_show_meta.widget
        rendered = render_to_string('survey_sens/includes/likert_frozen.html',
                                    dict(choices=choices,
                                         widget=widget,
                                         answer=to_show_value))
        return rendered


    q_order = models.StringField(doc='to store randomized order of sensitive questions')
    age = models.IntegerField(
        min=0,
        label="Укажите Ваш возраст:"
    )


    homosexuality_attitude = models.IntegerField(
        label="",
        choices=Constants.Range010,
        widget=LikertWidget(
            quote=Constants.HOMO_Q,
            label="Select a value on a scale from 0 to 10, where 0 is Negative and 10 is Positive:",
            left="Negative",
            right="Positive",
            html_class='bg-primary text-white'
        )
    )

    average_choice_homosexuality = models.IntegerField(
        label=f'{Constants.PREV_PREFIX}: {iwrapper(Constants.HOMO_Q)}',
        choices=Constants.Range010,
        widget=LikertWidget(
            quote=Constants.average_quote,
            label="Select a value on a scale from 0 to 10, where 0 is Negative and 10 is Positive:",
            left="Negative",
            right="Positive",

        )
    )
    gender_roles_attitude = models.IntegerField(
        label="",
        choices=Constants.Range010,
        widget=LikertWidget(
            quote=Constants.GENDER_Q,
            label="Choose a value on a scale from 0 to 10, where 0 - Fully disagree, 10 - Fully agree.",
            left="I totally disagree",
            right="I totally agree.",
            html_class='bg-primary text-white'
        )
    )

    average_choice_gender_roles = models.IntegerField(
        label=f'{Constants.PREV_PREFIX}: {iwrapper(Constants.GENDER_Q)}',
        choices=Constants.Range010,
        widget=LikertWidget(
            quote=Constants.average_quote,
            label="Choose a value on a scale from 0 to 10, where 0 - Fully disagree, 10 - Fully agree.",
            left="I totally disagree",
            right="I totally agree.",
        )
    )

    authority_attitude = models.IntegerField(
        label="",
        choices=Constants.Range010,
        widget=LikertWidget(
            quote=Constants.PUTIN_Q,
            label="Select a value on a scale from 0 to 10, where 0 - Bad, 10 - Good",
            left="Bad",
            right="Good",
            html_class='bg-primary text-white'
        )
    )

    average_choice_authority = models.IntegerField(
        label=f'{Constants.PREV_PREFIX}: {iwrapper(Constants.PUTIN_Q)}',
        choices=Constants.Range010,
        widget=LikertWidget(
            quote=Constants.average_quote,
            label="Select a value on a scale from 0 to 10, where 0 - Bad, 10 - Good",
            left="Bad",
            right="Good",
        )
    )
