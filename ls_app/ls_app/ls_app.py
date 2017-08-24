"""
The flask application controls and website structure
"""
import os
import sqlite3
from .process_text import spookify_adjectives, remove_adjectives
from flask import Flask, request, session, g, redirect, url_for, abort, \
     render_template, flash

app = Flask(__name__)
app.config.from_object(__name__)

# Load default config and override config from an environment variable
app.config.update(dict(
    DATABASE=os.path.join(app.root_path, 'ls_app.db'),
    SECRET_KEY='development key',
    USERNAME='admin',
    PASSWORD='default'
))
app.config.from_envvar('LS_APP_SETTINGS', silent=True)


def connect_db():
    """Connects to the specific database."""
    rv = sqlite3.connect(app.config['DATABASE'])
    rv.row_factory = sqlite3.Row
    return rv


def init_db():
    """ function to initialize database"""
    db = get_db()
    with app.open_resource('schema.sql', mode='r') as f:
        db.cursor().executescript(f.read())
    db.commit()


@app.cli.command('initdb')
def initdb_command():
    """Initializes the database."""
    init_db()
    print('Initialized the database.')


def get_db():
    """Opens a new database connection if there is none yet for the
    current application context.
    """
    if not hasattr(g, 'sqlite_db'):
        g.sqlite_db = connect_db()
    return g.sqlite_db


@app.teardown_appcontext
def close_db(error):
    """Closes the database again at the end of the request."""
    if hasattr(g, 'sqlite_db'):
        g.sqlite_db.close()


@app.route('/')
def show_entries():
    """ Home page of the app """
    db = get_db()
    cur = db.execute('select * from entries order by id desc')
    entries = cur.fetchall()
    return render_template('show_entries.html', entries=entries)


@app.route('/<int:id>')
def show_text(id):
    """ displays a text, unspookified """
    db = get_db()
    cur = db.execute('select * from entries where id=?', [id])
    entry = cur.fetchone()
    return render_template('show_text.html', entry=entry)


@app.route('/spookify/<int:id>', methods=['POST'])
def spookify_text(id):
    """ displays a text, spookified """
    db = get_db()
    cur = db.execute('select * from entries where id=?', [id])
    entry = cur.fetchone()
    #entry.text = spookify_adjectives(entry.text)
    return render_template('show_text_sp.html', entry=entry)


@app.route('/add', methods=['POST'])
def add_entry():
    db = get_db()
    db.execute('insert into entries (title, text) values (?, ?)',
                 [request.form['title'], request.form['text']])
    db.commit()
    flash('New entry was successfully posted')
    return redirect(url_for('show_entries'))

"""
@app.context_processor
def utility_processor():
    return dict(spookify_adjectives=spookify_adjectives)
"""