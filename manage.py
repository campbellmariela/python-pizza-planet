import pytest
from flask.cli import FlaskGroup
from flask_migrate import Migrate

from app import flask_app
from app.plugins import db
# flake8: noqa
from app.repositories.models import Beverage, Ingredient, Order, OrderDetail, Size
from app.data.populate import populate_database


manager = FlaskGroup(flask_app)

migrate = Migrate()
migrate.init_app(flask_app, db)


@manager.command('test', with_appcontext=False)
def test():
    return pytest.main(['-v', './app/test', '-W ignore::pytest.PytestAssertRewriteWarning'])


@manager.command('populate_db')
def populate_db():
    populate_database()


if __name__ == '__main__':
    manager()
