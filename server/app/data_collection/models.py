from datetime import datetime
from sqlalchemy import Table, Column, Integer, String, MetaData, TIMESTAMP, ARRAY

metadata = MetaData()

news = Table(
    "news",
    metadata,
    Column("id", Integer, primary_key=True),
    Column("title", String, unique=True),
    Column("href", String),
    Column("image", String),
    Column("country", ARRAY(String)),
    Column("city", ARRAY(String)),
    Column("date", TIMESTAMP, default=datetime.today().strftime('%d-%m-%Y'))
)
