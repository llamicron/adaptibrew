#!/usr/bin/env python
import exchange
from exchange import Info
from exchange import Setting
from exchange import Request
from exchange import Recipe
import time
import settings
import version

db = exchange.connect()

if not Info.table_exists():
    db.create_tables([Info])

if not Setting.table_exists():
    db.create_tables([Setting])

if not Request.table_exists():
    db.create_tables([Request])

if not Recipe.table_exists():
    db.create_tables([Recipe])

exchange.write_settings()

print "Adaptibrew " + version.current + " running..."

while True:
    exchange.write_latest_data()
    exchange.check_for_requests()
    time.sleep(0.5)
