from flask_sqlalchemy import SQLAlchemy
from .Expense import metadata

db = SQLAlchemy(metadata=metadata)