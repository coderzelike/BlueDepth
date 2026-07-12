from app.db.database import Base, engine

# Importálni kell a modelleket, hogy az SQLAlchemy "lássa" őket.
from app.models.dive import Dive

Base.metadata.create_all(bind=engine)

print("✅ Database initialized successfully!")