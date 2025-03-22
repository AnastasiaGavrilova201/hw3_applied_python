from sqlalchemy import Table, Column, Integer, DateTime, MetaData, String

metadata = MetaData()

user = Table(
    "user",
    metadata,
    Column("id", Integer, primary_key=True),
    Column("url", String, nullable=False),
    Column("url_short", String, nullable=False),
    Column("expires_at", DateTime, nullable=True),
    Column("created_at", DateTime, nullable=False)
)