from flask import Flask, render_template, request
import json
import sqlite3
app = Flask(__name__)

con = sqlite3.connect("mittaukset.dbe3")
cur = con.cursor()
cur.execute("CREATE TABLE IF NOT EXIST mittaukset (id INTEGER PRIMARY KEY, paiva INTEGER, mittaus INTEGER)")
con.commit()
con.close()

lampotilat = [
    {'x':1, 'y':14}, 
    {'x':2, 'y':10},
    {'x':3, 'y':15}
]

paivat=['Maanantai','Tiistai','Keskiviikko', 'Torstai','Perjantai','Lauantai','Sunnuntai']


@app.route('/api', methods= ['GET'])


def index():
    return render_template("mittaukset.html", taulukko=lampotilat, paivat=paivat)

@app.route('/lisaa', methods= ['POST'])
def lisaa():
    uusimittaus = request.get_json(force=True)
    lampotilat.append(uusimittaus)
    return(json.dumps(uusimittaus))

if __name__ == "__main__":
    app.run(debug=True)
