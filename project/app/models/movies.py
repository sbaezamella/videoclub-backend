from tortoise import fields
from tortoise.models import Model


class Movie(Model):
    id = fields.IntField(pk=True)
    title = fields.CharField(min_length=1, max_length=170, null=False)
    year = fields.SmallIntField()
    stock = fields.IntField()
    duration = fields.IntField()
    genres: fields.ManyToManyRelation["Genre"] = fields.ManyToManyField(
        "models.Genre", related_name="genres", through="movie_genre"
    )

    created_at = fields.DatetimeField()
    updated_at = fields.DatetimeField()

    class Meta:
        table = "movie"
        ordering = ["created_at"]

    def __str__(self):
        return self.title
