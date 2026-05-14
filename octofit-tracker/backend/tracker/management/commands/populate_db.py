from django.core.management.base import BaseCommand
from tracker.models import User, Team, Activity, Leaderboard, Workout

class Command(BaseCommand):
    help = 'Populate the database with test data'

    def handle(self, *args, **options):
        # Clear existing data
        User.objects.all().delete()
        Team.objects.all().delete()
        Activity.objects.all().delete()
        Leaderboard.objects.all().delete()
        Workout.objects.all().delete()

        # Sample users
        User.objects.create(name="Clark Kent", email="superman@dc.com", team="dc")
        User.objects.create(name="Bruce Wayne", email="batman@dc.com", team="dc")
        User.objects.create(name="Diana Prince", email="wonderwoman@dc.com", team="dc")
        User.objects.create(name="Tony Stark", email="ironman@marvel.com", team="marvel")
        User.objects.create(name="Steve Rogers", email="captain@marvel.com", team="marvel")
        User.objects.create(name="Peter Parker", email="spiderman@marvel.com", team="marvel")

        # Teams
        Team.objects.create(name="marvel", members=["Tony Stark", "Steve Rogers", "Peter Parker"])
        Team.objects.create(name="dc", members=["Clark Kent", "Bruce Wayne", "Diana Prince"])

        # Activities
        Activity.objects.create(user="Clark Kent", activity="Flight", duration=60)
        Activity.objects.create(user="Tony Stark", activity="Suit Training", duration=45)
        Activity.objects.create(user="Diana Prince", activity="Sword Practice", duration=30)

        # Leaderboard
        Leaderboard.objects.create(team="marvel", points=300)
        Leaderboard.objects.create(team="dc", points=250)

        # Workouts
        Workout.objects.create(user="Steve Rogers", workout="Shield Throw", reps=100)
        Workout.objects.create(user="Bruce Wayne", workout="Martial Arts", reps=80)

        self.stdout.write(self.style.SUCCESS('Database populated with test data.'))
