from peewee import BooleanField, CharField, SqliteDatabase, Model

db = SqliteDatabase("todo.db")


class BaseModel(Model):
    class Meta:
        database = db


class TodoItem(BaseModel):
    title = CharField()
    description = CharField(null=True)
    is_completed = BooleanField(default=False)


db.connect()
db.create_tables([TodoItem])
