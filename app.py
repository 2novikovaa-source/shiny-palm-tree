from flask import Flask, render_template_string

from connect_db import get_connection

app = Flask(__name__)

PAGE_TEMPLATE = """
<!doctype html>
<html>
<head>
    <title>Chuck Norris Jokes</title>
    <style>
        body { font-family: sans-serif; margin: 2rem; }
        table { border-collapse: collapse; width: 100%; }
        th, td { border: 1px solid #ccc; padding: 0.5rem; text-align: left; }
        th { background: #f2f2f2; }
    </style>
</head>
<body>
    <h1>Chuck Norris Jokes</h1>
    <table>
        <tr>
            {% for column in columns %}
            <th>{{ column }}</th>
            {% endfor %}
        </tr>
        {% for row in rows %}
        <tr>
            {% for value in row %}
            <td>{{ value }}</td>
            {% endfor %}
        </tr>
        {% endfor %}
    </table>
</body>
</html>
"""


@app.route("/")
def show_jokes():
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute(
        "SELECT id, value, url, categories, created_at, updated_at FROM chuck_norris_jokes;"
    )
    rows = cursor.fetchall()
    columns = [description[0] for description in cursor.description]
    cursor.close()
    conn.close()

    return render_template_string(PAGE_TEMPLATE, columns=columns, rows=rows)


if __name__ == "__main__":
    app.run(debug=True)
