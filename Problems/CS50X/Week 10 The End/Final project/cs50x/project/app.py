from flask import Flask, flash, redirect, render_template, request, session
import sqlite3
from datetime import datetime
from cs50 import SQL

app = Flask(__name__)
db = SQL("sqlite:///messages.db")
# Database setup
def init_db():
    conn = sqlite3.connect('visitors.db')
    c = conn.cursor()
    c.execute('''CREATE TABLE IF NOT EXISTS visitors
                 (id INTEGER PRIMARY KEY AUTOINCREMENT,
                  ip TEXT,
                  user_agent TEXT,
                  visit_time TEXT)''')
    conn.commit()
    conn.close()

# Log visitor data
def log_visitor(ip, user_agent):
    conn = sqlite3.connect('visitors.db')
    c = conn.cursor()
    visit_time = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    c.execute("INSERT INTO visitors (ip, user_agent, visit_time) VALUES (?, ?, ?)",
              (ip, user_agent, visit_time))
    conn.commit()
    conn.close()

# Homepage route
@app.route('/', methods=["GET", "POST"])
def home():
    # Log visitor data
    ip = request.remote_addr
    user_agent = request.headers.get('User-Agent')
    log_visitor(ip, user_agent)
    if request.method == "POST":
        if not request.form.get("name"):
            return redirect("/apology")
        elif not request.form.get("message"):
            return redirect("/apology")
        elif not request.form.get("email"):
            return redirect("/apology")
        name = request.form.get("name")
        email = request.form.get("email")
        message = request.form.get("message")
        time = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        db.execute("INSERT INTO messages( name, email, message, time) VALUES (?,?,?,?)", name, email, message , time)
    return render_template ("portfolio.html")
@app.route('/portfolio')




# Route to view visitor logs
@app.route('/logs')
def view_logs():
    conn = sqlite3.connect('visitors.db')
    c = conn.cursor()
    c.execute("SELECT * FROM visitors")
    logs = c.fetchall()
    conn.close()
    return {"visitors": logs}

if __name__ == '__main__':
    init_db()
    app.run(debug=True)
@app.route('/apology')
def apology():
    return render_template("apology.html")
