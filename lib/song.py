#import sqlite3
from config import DB_CONN, DB_CURSOR

# DB_CONN = sqlite3.connect('music.db')
# DB_CURSOR = DB_CONN.cursor()

class Song:

    all = []

    def __init__(self, name, album):
        self.id = None
        self.name = name
        self.album = album

    @classmethod
    def create_table(cls):
        sql = """
            CREATE TABLE IF NOT EXISTS songs (
                id INTEGER PRIMARY KEY,
                name TEXT,
                album TEXT
            )
        """

        DB_CURSOR.execute(sql)

    @classmethod
    def drop_table(cls):
        sql = """
            DROP TABLE IF EXISTS songs
        """

        DB_CURSOR.execute(sql)

    def save(self):
        sql = """
            INSERT INTO songs (name, album)
            VALUES (?, ?)
        """

        DB_CURSOR.execute(sql, (self.name, self.album))

        self.id = DB_CURSOR.execute("SELECT last_insert_rowid() FROM songs").fetchone()[0]

    @classmethod
    def create(cls, name, album):
        song = Song(name, album)
        song.save()
        return song

    # new code goes here!
    @classmethod
    def new_from_db(cls, row):
        song = cls(row[1], row[2])
        song.id = row[0]

    @classmethod
    def all(cls):
        sql = """
            SELECT *
            FROM songs
        """

        all = DB_CURSOR.execute(sql).fetchall()

    @classmethod
    def get_all(cls):
        sql = """
            SELECT *
            FROM songs
        """

        all = DB_CURSOR.execute(sql).fetchall()

        cls.all = [cls.new_from_db(row) for row in all]
