from otree.api import *


class C(BaseConstants):
    NAME_IN_URL = "survey"
    PLAYERS_PER_GROUP = None
    NUM_ROUNDS = 1


class Subsession(BaseSubsession):
    pass


class Group(BaseGroup):
    pass


class Player(BasePlayer):
    pass


# FUNCTIONS


# PAGES
class MyPage(Page):
    @staticmethod
    def vars_for_template(player: Player):
        return dict(
            my_var="あいうえお",
        )


page_sequence = [MyPage]
