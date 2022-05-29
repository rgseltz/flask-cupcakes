from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


def connect_db(app):
    db.app = app
    db.init_app(app)
    print('connected.')


class Cupcake(db.Model):
    """Cupcake class that instatiates cupcake objects"""

    __tablename__ = 'cupcakes'

    id = db.Column(db.Integer, autoincrement=True, primary_key=True)

    flavor = db.Column(db.Text, nullable=False)

    size = db.Column(db.Text, nullable=False)

    rating = db.Column(db.Float, nullable=False)

    image = db.Column(db.Text, nullable=False,
                      default='https://tinyurl.com/demo-cupcake')

    def __repr__(self):
        return f"<Cupcake id={self.id}, flavor={self.flavor}, size={self.size}, rating={self.rating}, image={self.image}>"
