


#flask
from flask import (Flask, redirect, url_for, request,
             render_template, Response, jsonify, redirect)


app = Flask(__name__)




@app.route('/', methods=['GET'])
def index():
    # Main page
    return render_template('index.html')
    #return ('index.html')




if __name__ == '__main__':
    app.run()