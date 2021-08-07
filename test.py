import os
os.environ.setdefault("DJANGO_SETTINGS_MODULE", 'config.settings')
import django
django.setup()
from index.models import Ranking

def save_RankingScore():
    return

