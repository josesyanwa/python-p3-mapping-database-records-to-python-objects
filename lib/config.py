import sqlite3

DB_CONN = sqlite3.connect('../db/music.db')
DB_CURSOR = DB_CONN.cursor()