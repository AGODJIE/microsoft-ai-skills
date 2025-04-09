from django.core.management.base import BaseCommand
from django.conf import settings
from pymongo import MongoClient

class Command(BaseCommand):
    help = 'Populate the database with test data for users, teams, activities, leaderboard, and workouts'

    def handle(self, *args, **kwargs):
        # Connect to MongoDB
        client = MongoClient(settings.DATABASES['default']['HOST'], settings.DATABASES['default']['PORT'])
        db = client[settings.DATABASES['default']['NAME']]

        # Drop existing collections
        db.users.drop()
        db.teams.drop()
        db.activity.drop()
        db.leaderboard.drop()
        db.workouts.drop()

        # Use raw MongoDB commands to insert data
        db.users.insert_many([
            {"email": "thundergod@mhigh.edu", "name": "Thunder God", "age": 16},
            {"email": "metalgeek@mhigh.edu", "name": "Metal Geek", "age": 17},
            {"email": "zerocool@mhigh.edu", "name": "Zero Cool", "age": 16},
            {"email": "crashoverride@mhigh.edu", "name": "Crash Override", "age": 18},
            {"email": "sleeptoken@mhigh.edu", "name": "Sleep Token", "age": 17},
        ])

        db.teams.insert_many([
            {"name": "Blue Team", "members": ["thundergod@mhigh.edu", "metalgeek@mhigh.edu"]},
            {"name": "Gold Team", "members": ["zerocool@mhigh.edu", "crashoverride@mhigh.edu", "sleeptoken@mhigh.edu"]},
        ])

        db.activity.insert_many([
            {"user": "thundergod@mhigh.edu", "type": "Cycling", "duration": 60, "date": "2025-04-01"},
            {"user": "metalgeek@mhigh.edu", "type": "Crossfit", "duration": 120, "date": "2025-04-02"},
            {"user": "zerocool@mhigh.edu", "type": "Running", "duration": 90, "date": "2025-04-03"},
            {"user": "crashoverride@mhigh.edu", "type": "Strength", "duration": 30, "date": "2025-04-04"},
            {"user": "sleeptoken@mhigh.edu", "type": "Swimming", "duration": 75, "date": "2025-04-05"},
        ])

        db.leaderboard.insert_many([
            {"user": "thundergod@mhigh.edu", "points": 100},
            {"user": "metalgeek@mhigh.edu", "points": 90},
            {"user": "zerocool@mhigh.edu", "points": 95},
            {"user": "crashoverride@mhigh.edu", "points": 85},
            {"user": "sleeptoken@mhigh.edu", "points": 80},
        ])

        db.workouts.insert_many([
            {"name": "Cycling Training", "description": "Training for a road cycling event"},
            {"name": "Crossfit", "description": "Training for a crossfit competition"},
            {"name": "Running Training", "description": "Training for a marathon"},
            {"name": "Strength Training", "description": "Training for strength"},
            {"name": "Swimming Training", "description": "Training for a swimming competition"},
        ])

        self.stdout.write(self.style.SUCCESS('Successfully populated the database with test data.'))
