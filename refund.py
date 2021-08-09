#!/usr/bin/env python

import csv
from decimal import Decimal
import uuid
from datetime import datetime
import dateutil.relativedelta
import json

promotion_id = '6e85d5fd-be79-43d0-b418-e6db099c1f26'

grants = []

def create_payment(payment_id, amount):
    payment_id = payment_id.strip()
    try:
        paymentid = uuid.UUID(payment_id)
    except:
        return

    row['id'] = uuid.uuid4()
    row['created_at'] = datetime.now().isoformat()
    row['promotion_id'] = promotion_id
    row['payment_id'] = payment_id
    row['amount'] = amount
    row['legacy_claimed'] = 't'
    row['redeemed'] = 'f'
    row['bonus'] = amount
    row['redeemed_at'] = None
    row['drained'] = 'f'

    grants.append(row)
    
with open('refunds.csv') as f:
    reader = csv.DictReader(f)
    for row in reader:
        create_payment(row['PaymentID'], row['Amount (BAT)'])

with open('grants.csv', 'w+') as f:
    writer = csv.DictWriter(f, extrasaction='ignore', fieldnames=['id', 'created_at', 'promotion_id', 'payment_id', 'amount', 'legacy_claimed', 'redeemed', 'bonus', 'redeemed_at', 'drained'])
    writer.writeheader()
    writer.writerows(grants)
