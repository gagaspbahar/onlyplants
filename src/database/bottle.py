import bottle
import sqlite3
from sqlite3 import template, HTTPError

app = bottle.Bottle()
plugin = bottle.ext.sqlite.Plugin(dbfile='test.db')
app.install(plugin)

@app.route('/show/:item')
def show(item, db):
    cursor = db.cursor()
    cursor.execute('SELECT id, description from items where name=?', item)
    row = cursor.fetchone()
    if row:
        return template('showitem', page=row)
    return HTTPError(404, "Page not found")

def create_table(db):
    """Create database table for the likes application
    given a database connection 'db'.
    Removes any existing data that might be in the
    database."""

    cursor = db.cursor()
    cursor.execute("DROP TABLE IF EXISTS likes")
    cursor.execute("""
    CREATE TABLE likes (
       thing text
    )
    """)

def store_like(db, like):
    """Store a new like in the database"""

    cursor = db.cursor()
    cursor.execute("INSERT INTO likes (thing) VALUES (?)", [like])
    db.commit()
  
def get_likes(db):
   """Return a list of likes from the database"""

   cursor = db.cursor()
   cursor.execute("SELECT thing FROM likes")
   result = []
   for row in cursor:
       result.append(row['thing'])
   return result

@app.route('/')
def index(db):
    """Home page"""

    info = {
        'title': 'Welcome Home!',
        'likes': get_likes(db)
    }

    return template('dblikes.tpl', info)

@app.post('/likes')
def like(db):
    """Process like form post request"""

    # get the form field
    likes = request.forms.get('likes')

    if likes:
        store_like(db, likes)

    return redirect('/')

if __name__ == "__main__":
    # code to connect to the database and create the tables
    DATABASE_NAME = 'onlyplants.db'
    db = sqlite3.connect(DATABASE_NAME)
    create_table(db)

    # code to run our web application
    plugin = bottle.ext.sqlite.Plugin(dbfile=DATABASE_NAME)
    app.install(plugin)
    
    # run the application
    app.run()