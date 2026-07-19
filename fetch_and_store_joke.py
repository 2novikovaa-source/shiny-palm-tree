import requests

from connect_db import get_connection

INSERT_SQL = """
INSERT INTO chuck_norris_jokes (id, value, url, icon_url, categories, created_at, updated_at)
VALUES (%(id)s, %(value)s, %(url)s, %(icon_url)s, %(categories)s, %(created_at)s, %(updated_at)s)
ON CONFLICT (id) DO NOTHING;
"""

response = requests.get("https://api.chucknorris.io/jokes/random")
response.raise_for_status()
joke = response.json()

conn = get_connection()
cursor = conn.cursor()
cursor.execute(INSERT_SQL, joke)
conn.commit()
cursor.close()
conn.close()

print(f"Saved joke {joke['id']}: {joke['value']}")
