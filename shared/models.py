from __future__ import annotations

from sqlalchemy import (
    Integer,
    MetaData,
    String,
    TIMESTAMP,
    ARRAY
)
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column, relationship
from sqlalchemy.sql import func


class Base(DeclarativeBase):
    """Base class"""

    metadata = MetaData(
        naming_convention={
            'ix': 'ix_%(column_0_label)s',
            'uq': 'uq_%(table_name)s_%(column_0_name)s',
            'ck': 'ck_%(table_name)s_`%(constraint_name)s`',
            'fk': 'fk_%(table_name)s_%(column_0_name)s_%(referred_table_name)s',
            'pk': 'pk_%(table_name)s',
        }
    )


class Intonation(Base):
    __tablename__ = 'intonations'

    id: Mapped[int] = mapped_column(
        'id',
        Integer,
        primary_key=True,
        autoincrement=True
    )
    intonation: Mapped[str] = mapped_column('intonation', String, unique=True)


class News(Base):
    __tablename__ = 'news'

    id: Mapped[int] = mapped_column(
        'id',
        Integer,
        primary_key=True,
        autoincrement=True
    )
    title_en: Mapped[str] = mapped_column(
        'title_en',
        String,
        unique=True
    )
    title_ru: Mapped[str] = mapped_column('title_ru', String)
    href: Mapped[str] = mapped_column('href', String)
    image: Mapped[str] = mapped_column('image', String)
    country: Mapped[list[str]] = mapped_column('country', ARRAY(String))
    city: Mapped[list[str]] = mapped_column('city', ARRAY(String))
    sharps: Mapped[list[str]] = mapped_column('sharps', ARRAY(String))
    date: Mapped[TIMESTAMP] = mapped_column(
        'date',
        TIMESTAMP,
        server_default=func.now(),
        nullable=False
    )
