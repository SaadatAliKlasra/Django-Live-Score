from django.core.management.base import BaseCommand
from main.models import Tournament, Team, Fixture

TEAMS = [
    "Islamabad United",
    "Karachi Kings",
    "Lahore Qalandars",
    "Multan Sultans",
    "Peshawar Zalmi",
    "Quetta Gladiators",
]


class Command(BaseCommand):
    help = "Load EPL teams and fixtures"

    def handle(self, *args, **kwargs):
        # add tournament
        tournament, created = Tournament.objects.get_or_create(name="PSL")

        # add the teams
        if Team.objects.count() == 0:
            team_obj = [Team(name=team_name) for team_name in TEAMS]
            teams = Team.objects.bulk_create(team_obj)
            teams = Team.objects.all()
        else:
            teams = Team.objects.all()

        fixtures = []
        for i in range(0, len(teams), 2):
            fixtures.append(
                Fixture(
                    home_team=teams[i], away_team=teams[i + 1], tournament=tournament
                )
            )
        if Fixture.objects.count() == 0:
            fixtures = Fixture.objects.bulk_create(fixtures)
