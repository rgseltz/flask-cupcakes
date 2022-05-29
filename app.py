from flask import Flask, jsonify, request, redirect, render_template, session, flash
from models import db, connect_db, Cupcake
from flask_debugtoolbar import DebugToolbarExtension

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql:///cupcakes_db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_ECHO'] = True

connect_db(app)


@app.route('/api/cupcakes', methods=["GET"])
def show_all_cupcakes():
    cupcakes = Cupcake.query.all()
    serialized = [Cupcake.serialized(cupcake) for cupcake in cupcakes]
    return jsonify(data=serialized)


@app.route('/api/cupcakes/<int:id>', methods=["GET"])
def get_single_cupcake(id):
    cupcake = Cupcake.query.get_or_404(id)
    return jsonify(data=cupcake.serialized())


@app.route('/api/cupcakes', methods=["POST"])
def add_new_cupcake():
    new_cupcake = Cupcake(
        flavor=request.json["flavor"],
        size=request.json["size"],
        rating=request.json["rating"],
        image=request.json.get("image")
    )
    db.session.add(new_cupcake)
    db.session.commit()
    return (jsonify(data=new_cupcake.serialized()), 201)


@app.route('/api/cupcakes/<int:id>', methods=["PATCH"])
def update_a_cupcake(id):
    cupcake = Cupcake.query.get_or_404(id)
    cupcake.flavor = request.json.get('flavor', cupcake.flavor)
    cupcake.size = request.json.get('size', cupcake.size)
    cupcake.rating = request.json.get('rating', cupcake.rating)
    cupcake.image = request.json.get('image', cupcake.image)
    db.session.add(cupcake)
    db.session.commit()
    return jsonify(data=cupcake.serialized())


@app.route('/api/cupcakes/<int:id>', methods=["DELETE"])
def delete_cupcake(id):
    cupcake = Cupcake.query.get_or_404(id)
    db.session.delete(cupcake)
    db.session.commit()
    return jsonify(message="Deleted")


@app.route('/', methods=["GET"])
def display_cupcakes():
    # cupcakes = Cupcake.query.all()
    return render_template('index.html')
