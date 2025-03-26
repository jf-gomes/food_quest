import sqlite3

conn = sqlite3.connect("game_data")

results = conn.execute('SELECT * FROM data ORDER BY score DESC LIMIT 10').fetchall()

for result in results:
    print (result)

print(f'Total de registros: {len(results)}')