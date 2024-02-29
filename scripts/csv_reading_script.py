from django.utils import timezone
from myapp.models import Card, Delivered, DeliveryException, Pickup, Returned
import csv
from datetime import datetime

# helper function to parse timestamp
def parse_timestamp(val):
    formats = ["%d-%m-%Y %H:%M", "%Y-%m-%dT%H:%M:%SZ",
               "%d-%m-%Y %I:%M %p", "%d-%m-%Y %I:%M%p"]
    for fmt in formats:
        try:
            dt = datetime.strptime(val, fmt)
            return timezone.make_aware(dt)
        except ValueError:
            pass
    raise ValueError(f"No valid date format found for {val}")

def run():
    # open delivered.csv
    with open('data/delivered.csv') as file:
        reader = csv.reader(file)
        next(reader) # skip header row
        for row in reader:
            id, card_id, user_phone, timestamp, comment = row
            card, _ = Card.objects.get_or_create(card_id=card_id, user_contact=user_phone.strip('"'))
            Delivered.objects.update_or_create(
                id=id, 
                defaults={
                    'card': card,
                    'timestamp': parse_timestamp(timestamp),
                    'comment': comment
                }
            )

    # open delivery_exception.csv
    with open('data/delivery_exception.csv') as file:
        reader = csv.reader(file)
        next(reader) # skip header row
        for row in reader:
            id, card_id, user_phone, timestamp, comment = row
            card, _ = Card.objects.get_or_create(card_id=card_id, user_contact=user_phone.strip('"'))
            DeliveryException.objects.update_or_create(
                id=id, 
                defaults={
                    'card': card,
                    'timestamp': parse_timestamp(timestamp),
                    'comment': comment
                }
            )

    # open pickup.csv
    with open('data/pickup.csv') as file:
        reader = csv.reader(file)
        next(reader) # skip header row
        for row in reader:
            id, card_id, user_phone, timestamp = row
            card, _ = Card.objects.get_or_create(card_id=card_id, user_contact=user_phone.strip('"'))
            Pickup.objects.update_or_create(
                id=id, 
                defaults={
                    'card': card,
                    'timestamp': parse_timestamp(timestamp),
                }
            )

    # open returned.csv
    with open('data/returned.csv') as file:
        reader = csv.reader(file)
        next(reader) # skip header row
        for row in reader:
            id, card_id, user_phone, timestamp = row
            card, _ = Card.objects.get_or_create(card_id=card_id, user_contact=user_phone.strip('"'))
            Returned.objects.update_or_create(
                id=id, 
                defaults={
                    'card': card,
                    'timestamp': parse_timestamp(timestamp),
                }
            )
