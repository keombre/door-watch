import sqlite3

class DB:
    @classmethod
    def get_db(cls):
        con = sqlite3.connect("./db.sqlite")
        cls.__seed(con)
        return con

    @staticmethod
    def __seed(db):
        cur = db.cursor()
        cur.execute('CREATE TABLE IF NOT EXISTS entries (date INTEGER NOT NULL, read INTEGER NOT NULL DEFAULT 0);')
        db.commit()

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
