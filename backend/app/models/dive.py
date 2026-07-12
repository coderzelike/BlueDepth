from datetime import date

from sqlalchemy import Date, Float, Integer, String, Text
from sqlalchemy.orm import Mapped, mapped_column

from app.db.database import Base


class Dive(Base):
    __tablename__ = "dives"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)

    dive_number: Mapped[int] = mapped_column(Integer, nullable=False)

    date: Mapped[date] = mapped_column(Date, nullable=False)

    location: Mapped[str] = mapped_column(String(255), nullable=False)

    max_depth: Mapped[float] = mapped_column(Float, nullable=False)

    dive_time: Mapped[int] = mapped_column(Integer, nullable=False)

    buddy: Mapped[str | None] = mapped_column(String(255), nullable=True)

    notes: Mapped[str | None] = mapped_column(Text, nullable=True)