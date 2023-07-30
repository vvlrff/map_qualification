from datetime import datetime
from sqlalchemy import Table, Column, Integer, String, MetaData, TIMESTAMP

metadata = MetaData()


news = Table(
    "news",
    metadata,
    Column("id", Integer, primary_key=True),
    Column("title", String),
    Column("href", String),
    Column("date", TIMESTAMP, default=datetime.today().strftime('%d-%m-%Y'))
)

country = Table(
    "country",
    metadata,
    Column("id", Integer, primary_key=True),
    Column("text", String),
    Column("country", String),
    Column("date", TIMESTAMP, default=datetime.today().strftime('%d-%m-%Y'))
    # Column("date", DateTime, default=datetime.today().strftime('%d-%m-%Y'))
)

