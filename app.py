
from flask import Flask, request
from db import db
from flask_cors import CORS



app = Flask(__name__)
CORS(app)

db = db()




@app.route('/getitem')
def get_all():
    return db.get_all()


@app.route('/getitemiId/<iId>')
def getitemiId(iId):
    return db.getitemiId(iId)


@app.route('/insert_item', methods=['POST'])
def insert_item():
    iId = str(request.json.get('iId'))
    Iname = request.json.get('Iname')
    Sprice = str(request.json.get('Sprice'))
    return db.insert_item(iId, Iname, Sprice)



@app.route("/update_item", methods=["PUT"])
def update_item():
    iId = str(request.json.get('iId'))
    Iname = str(request.json.get('Iname'))
    Sprice = str(request.json.get('Sprice'))
    return db.update_item(iId, Iname, Sprice)


@app.route("/delete_item", methods=["DELETE"])
def delete_item():
    iId = str(request.json.get('iId'))
    Iname = str(request.json.get('Iname'))
    Sprice = str(request.json.get('Sprice'))
    return db.delete_item(iId, Iname, Sprice)

@app.route('/search_item')
def search_item():
    iId = request.json.get('iId')
    return db.search_item(iId)





if __name__ == '__main__':
    app.run(debug=True)