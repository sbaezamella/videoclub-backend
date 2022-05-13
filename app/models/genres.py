from tortoise import fields
from tortoise.models import Model


class Genre(Model):
    id = fields.IntField(pk=True)
    name = fields.CharField(
        min_length=1, max_length=50, unique=True, null=False
    )  # noqa
    created_at = fields.DatetimeField()
    updated_at = fields.DatetimeField()

    movies: fields.ManyToManyRelation["Movie"]

    class Meta:
        table = "genre"
        ordering = ["created_at"]

    def __str__(self):
        return self.name
