#!/usr/bin/env python3
import datajoint as dj


connection = dj.conn(host="tutorial-db.datajoint.io", user="jonathan",
                     password="testpassword123", database_name="jonathan_tutorial", reset=False, use_tls=True)

cursor = connection.fetch_query_ph(
    "select * from mouse where mouse_id = ?", 1)
try:
    l = list(cursor)
    for row in l:
        print(row.to_dict())
except AssertionError:
    print('failed :(')

connection.disconnect()
