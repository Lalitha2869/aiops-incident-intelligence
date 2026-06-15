from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

VECTOR_DATABASE_URL = (
    "postgresql://postgres:2869@localhost:5433/aiops_vector_db"
)

vector_engine = create_engine(
    VECTOR_DATABASE_URL
)

VectorSessionLocal = sessionmaker(
    autocommit=False,
    autoflush=False,
    bind=vector_engine
)