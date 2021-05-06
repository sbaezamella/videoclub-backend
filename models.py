from tortoise import fields
from tortoise.models import Model


class Genre(Model):
    id = fields.IntField(pk=True)
    name = fields.CharField(max_length=50)
    created_at = fields.DatetimeField()
    updated_at = fields.DatetimeField()

    class Meta:
        table = "genre"
        ordering = ["created_at"]

    def __str__(self):
        return self.name
