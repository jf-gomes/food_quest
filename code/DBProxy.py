import sqlite3

class DBProxy:

    def __init__(self, db_name: str):
        self.db_name = db_name
        self.conn = sqlite3.connect(db_name)
        self.conn.execute(
            '''CREATE TABLE IF NOT EXISTS data (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            score INTEGER NOT NULL,
            date TEXT NOT NULL
            )
            '''
        )
    
    def save(self, name, score, date):
        score_dict = {
            "name": name,
            "score": score,
            "date": date
        }
        self.conn.execute('INSERT INTO data (name, score, date) VALUES (:name, :score, :date)', score_dict,)
        self.conn.commit()

    def retrieveTop10(self):
        return self.conn.execute('SELECT * FROM data ORDER BY score DESC LIMIT 10').fetchall()
    
    def close(self):
        return self.conn.close()

