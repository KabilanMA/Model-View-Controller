from flask_sqlalchemy import SQLAlchemy

from .DBModel import metadata

db = SQLAlchemy(metadata=metadata)