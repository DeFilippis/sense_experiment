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
from survey_sens.widgets import LikertWidget

author = 'Philipp Chapkovski, HSE-Moscow'

doc = """
Post-experimental questionnaire
"""


class Constants(BaseConstants):
    name_in_url = 'questionnaire'
    players_per_group = None
    num_rounds = 1


class Subsession(BaseSubsession):
    pass


class Group(BaseGroup):
    pass


class Player(BasePlayer):
    sex = models.IntegerField(
        label="Your gender",
        choices=[
            [0, 'Male'],
            [1, 'Female'],
        ],
        widget=widgets.RadioSelect
    )
    religion = models.IntegerField(
        label="Do you confess any religion? Which one",
        choices=[
            [1, 'Atheist'],
            [2, 'Catholic'],
            [3, 'Protestant'],
            [4, 'Eastern orthodox'],
            [5, 'Jew'],
            [6, 'Muslim'],
            [7, 'Induist'],
            [8, 'Bhuddist'],
            [9, 'Other religion']
        ],
        widget=widgets.RadioSelect
    )

    education = models.IntegerField(
        label="What is the highest educational level you attained",
        choices=[
            [1, 'Middle school'],
            [2, 'Vocational school'],
            [3, 'Unfinished higher education'],
            [4, 'Higher education (University diploma)'],
            [5, 'Ph.D'],
        ],
        widget=widgets.RadioSelect
    )

    occupation = models.IntegerField(
        label="Are you currently employed",
        choices=[
            [0, 'No'],
            [1, 'Yes']
        ],
        widget=widgets.RadioSelect,
    )

    relative_income_2 = models.IntegerField(
        label='What is the best description of the financial situation of your household?',
        choices=[
            [1, 'Not enough money for food'],
            [2, 'Enough for food, but not enough for clothes and shoes'],
            [3, 'Enough for clothes and shoes, but not enough to buy small household appliances'],
            [4,
             'Enough for small purchases, but to purchase large items (computer, washing machine, fridge) I need to save or take a credit'],
            [5,
             'Enough money to buy items for the house, but to purchase a car, summer house or an apartment квартиры I need to save or take a credit'],
            [6, 'We can afford any purchases without limits or credits']
        ],
        widget=widgets.RadioSelect,
    )

    trust = models.IntegerField(
        label="Do you think most of people can be trusted or it's always safe to be cautious",
        choices=[
            [0, 'You need to be very cautious with other people'],
            [1, 'Most of the people can be trusted'],
        ],
        widget=widgets.RadioSelect,
    )

    marital_status = models.IntegerField(
        label="Your marital status",
        choices=[
            [1, 'Not married'],
            [2, 'Married'],
            [3, 'In relations'],
            [4, 'Divorsed'],
            [5, 'Separated'],
            [6, 'Widow'],
            [7, 'Hard to say'],
        ],
        widget=widgets.RadioSelect,
    )

    happy = models.IntegerField(
        label="I can say that I am",
        choices=[
            [0, 'Unhappy person'],
            [1, 'Happy person']
        ],
        widget=widgets.RadioSelect,
    )

    satisfaction = models.IntegerField(
        label='',
        choices=range(1, 11),
        widget=LikertWidget(
            quote="Taking into account all the circumstanses, how much are you satisfied by your life these days?",
            label="Choose item on a scale from 0 to 10 where 0 means 'Completely unsatisfied' and 10 means 'Completely satisified'",
            left="Completely unsatisfied",
            right="Completely satisfied"
        )

    )
