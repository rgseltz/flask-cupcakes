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
