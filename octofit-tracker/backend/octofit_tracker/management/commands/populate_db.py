from django.core.management.base import BaseCommand
from django.conf import settings
from django.contrib.auth import get_user_model
from django import models
from pymongo import MongoClient

class Command(BaseCommand):
    help = 'Populate the octofit_db database with test data'

    def handle(self, *args, **options):
        # Connect to MongoDB
        client = MongoClient('localhost', 27017)
        db = client['octofit_db']

        # Drop collections if they exist
        db.users.drop()
        db.teams.drop()
        db.activities.drop()
        db.leaderboard.drop()
        db.workouts.drop()

        # Create unique index on email for users
        db.users.create_index([('email', 1)], unique=True)

        # Sample users
        users = [
            {"name": "Clark Kent", "email": "superman@dc.com", "team": "dc"},
            {"name": "Bruce Wayne", "email": "batman@dc.com", "team": "dc"},
            {"name": "Diana Prince", "email": "wonderwoman@dc.com", "team": "dc"},
            {"name": "Tony Stark", "email": "ironman@marvel.com", "team": "marvel"},
            {"name": "Steve Rogers", "email": "captain@marvel.com", "team": "marvel"},
            {"name": "Peter Parker", "email": "spiderman@marvel.com", "team": "marvel"},
        ]
        db.users.insert_many(users)

        # Teams
        teams = [
            {"name": "marvel", "members": ["Tony Stark", "Steve Rogers", "Peter Parker"]},
            {"name": "dc", "members": ["Clark Kent", "Bruce Wayne", "Diana Prince"]},
        ]
        db.teams.insert_many(teams)

        # Activities
        activities = [
            {"user": "Clark Kent", "activity": "Flight", "duration": 60},
            {"user": "Tony Stark", "activity": "Suit Training", "duration": 45},
            {"user": "Diana Prince", "activity": "Sword Practice", "duration": 30},
        ]
        db.activities.insert_many(activities)

        # Leaderboard
        leaderboard = [
            {"team": "marvel", "points": 300},
            {"team": "dc", "points": 250},
        ]
        db.leaderboard.insert_many(leaderboard)

        # Workouts
        workouts = [
            {"user": "Steve Rogers", "workout": "Shield Throw", "reps": 100},
            {"user": "Bruce Wayne", "workout": "Martial Arts", "reps": 80},
        ]
        db.workouts.insert_many(workouts)

        self.stdout.write(self.style.SUCCESS('octofit_db database populated with test data.'))
