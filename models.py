from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine
from config import db_configuration

Base = automap_base()

engine = create_engine(db_configuration)

Base.prepare(engine, reflect=True)

Orders = Base.classes.orders

session = Session(engine)
