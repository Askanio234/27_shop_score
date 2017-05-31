from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine
from config import db_configuration

base = automap_base()

engine = create_engine(db_configuration)

base.prepare(engine, reflect=True)

orders = base.classes.orders

session = Session(engine)
