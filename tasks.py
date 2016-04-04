from invoke import task

from app.database import db
from app import app


__all__ = [
    'create_db',
    'drop_db',
    'rebuild_db',
]


@task
def create_db():
    """
    Creates tables in the database
    """
    with app.app_context():
        db.create_all()


@task
def drop_db():
    """
    Drops all tables from the database
    """
    with app.app_context():
        db.drop_all()


@task
def rebuild_db():
    """
    Drops and then creates all tables from the database
    """
    with app.app_context():
        drop_db()
        create_db()
