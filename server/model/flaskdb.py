
import sys
sys.path.append('/home/vinojith/Desktop/myproject/Model-View-Controller/server/model')

from DBModel import DBModel
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy(metadata=DBModel.metadata)