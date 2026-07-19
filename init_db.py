from connect_db import get_connection

CREATE_TABLE_SQL = """
CREATE TABLE IF NOT EXISTS chuck_norris_jokes (
    id TEXT PRIMARY KEY,
    value TEXT NOT NULL,
    url TEXT,
    icon_url TEXT,
    categories TEXT[],
    created_at TIMESTAMP,
    updated_at TIMESTAMP
);
"""

conn = get_connection()
cursor = conn.cursor()
cursor.execute(CREATE_TABLE_SQL)
conn.commit()
cursor.close()
conn.close()

print("Table 'chuck_norris_jokes' is ready.")
