from db import DB
from flask import Flask, render_template, request, redirect, url_for
from datetime import datetime
app = Flask(__name__)

db = DB()

@app.route('/')
def index():
    page = request.args.get('page', 0, int)
    entries = [(e[0], datetime.strptime(e[1], "%Y-%m-%d %H:%M:%S.%f").strftime("%X %d. %m. %Y"), e[2]) for e in db.get_entries(page)]
    pages = int(db.count_entries()[0]/10)
    return render_template("index.html", entries=entries, pages=pages, page=page)

@app.route('/add', methods=['POST'])
def add():
    db.add_entry(datetime.now())
    return ('', 200)

@app.route('/read', methods=['POST'])
def read():
    id = request.args.get('id')
    page = request.args.get('page')
    try:
        id = int(id)
    except:
        abort(400)
    db.mark_read(id)
    return redirect(url_for('index', page=page))

@app.route('/unread', methods=['POST'])
def unread():
    id = request.args.get('id')
    page = request.args.get('page')
    try:
        id = int(id)
    except:
        abort(400)
    db.mark_unread(id)
    return redirect(url_for('index', page=page))
