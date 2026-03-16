from ..app import app, db
from flask_sqlalchemy import text  # ← ajoutez cet import

@app.route("/test")
def test():
    result = db.session.execute(text('SELECT * FROM bird_detection')).fetchall() 
    print(result)
    return str(result)
    