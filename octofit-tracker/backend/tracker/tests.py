from django.test import TestCase
from rest_framework.test import APIClient
from .models import User, Team, Activity, Leaderboard, Workout

class APITest(TestCase):
    def setUp(self):
        self.client = APIClient()
        User.objects.create(name='Test User', email='test@example.com', team='marvel')
        Team.objects.create(name='marvel', members=['Test User'])
        Activity.objects.create(user='Test User', activity='Test Activity', duration=10)
        Leaderboard.objects.create(team='marvel', points=100)
        Workout.objects.create(user='Test User', workout='Test Workout', reps=10)

    def test_user_list(self):
        response = self.client.get('/api/users/')
        self.assertEqual(response.status_code, 200)

    def test_team_list(self):
        response = self.client.get('/api/teams/')
        self.assertEqual(response.status_code, 200)

    def test_activity_list(self):
        response = self.client.get('/api/activities/')
        self.assertEqual(response.status_code, 200)

    def test_leaderboard_list(self):
        response = self.client.get('/api/leaderboard/')
        self.assertEqual(response.status_code, 200)

    def test_workout_list(self):
        response = self.client.get('/api/workouts/')
        self.assertEqual(response.status_code, 200)
