import sqlite3

class DB:
    @classmethod
    def get_db(cls):
        return sqlite3.connect("./db.sqlite")

    @classmethod
    def seed(cls):
        con = cls.get_db()
        con.cursor().execute('CREATE TABLE IF NOT EXISTS entries (date INTEGER NOT NULL, read INTEGER NOT NULL DEFAULT 0);')
        con.commit()

    @classmethod
    def add_entry(cls, date):
        con = cls.get_db()
        con.cursor().execute('INSERT INTO entries VALUES (?, 0);', (date,))
        con.commit()

    @classmethod
    def get_entries(cls, offset = 0, paginate_size = 10):
        return cls.get_db().cursor().execute('SELECT rowid, * FROM entries ORDER BY date DESC LIMIT ? OFFSET ?;', (paginate_size, paginate_size * offset)).fetchall()

    @classmethod
    def count_entries(cls):
        return cls.get_db().cursor().execute('SELECT COUNT(*) FROM entries;').fetchone()

    @classmethod
    def mark_read(cls, id):
        con = cls.get_db()
        con.cursor().execute('UPDATE entries SET read = 1 WHERE rowid = ?;', (id,))
        con.commit()

    @classmethod
    def mark_unread(cls, id):
        con = cls.get_db()
        con.cursor().execute('UPDATE entries SET read = 0 WHERE rowid = ?;', (id,))
        con.commit()
