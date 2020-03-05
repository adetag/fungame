# Aurora de Tagyos for web-app-intro for Phill Conrad, W20, CCS CS20

import os
from flask import Flask, url_for, render_template, request, session
app = Flask(__name__)
app.secret_key='w98fw9ef8hwe98fhwef'     #this sets the secret key for sessions

@app.route("/")
def hello():
    return render_template('home.html')

@app.route('/newgame')
def render_newgame():
    session['name']=request.args['name']
    return render_template('newgame.html')

@app.route('/endgame')
def endgame():
    session.clear()
    return render_template('home.html')



if __name__=="__main__":
    app.run(debug=False, port=54321)
