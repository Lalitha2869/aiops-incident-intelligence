from backend.database.db import engine
from backend.database.base import Base

from backend.database.models import Incident

Base.metadata.create_all(bind=engine)

print("Tables Created Successfully")