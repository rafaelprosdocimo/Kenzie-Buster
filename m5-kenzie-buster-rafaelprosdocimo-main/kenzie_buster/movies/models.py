from django.db import models


class MovieClassificationChoices(models.TextChoices):
    PG = "PG"
    PG_13 = "PG-13"
    R = "R"
    NC_17 = "NC-17"
    G = "G"


# Create your models here.
class Movie(models.Model):
    title = models.CharField(max_length=127)
    duration = models.CharField(
        max_length=10,
        null=True,
        blank=True,
        default=None,
    )
    rating = models.CharField(
        max_length=20,
        choices=MovieClassificationChoices.choices,
        default=MovieClassificationChoices.G,
    )
    synopsis = models.TextField(
        null=True,
        blank=True,
        default=None,
    )
    user = models.ForeignKey(
        "users.User", on_delete=models.CASCADE, related_name="movies"
    )
    added_by = models.ForeignKey(
        "users.User", on_delete=models.SET_NULL, related_name="added_movies", null=True
    )
    movie_orders = models.ManyToManyField(
        "users.User",
        related_name="movie_orders",
        through="MovieOrder",
    )

    def __str__(self):
        return self.title


#
class MovieOrder(models.Model):
    price = models.DecimalField(max_digits=8, decimal_places=2)
    buyed_at = models.DateTimeField(auto_now_add=True)
    models.DecimalField(max_digits=8, decimal_places=2, null=False, blank=False)
    title = models.ForeignKey(
        "movies.Movie", on_delete=models.CASCADE, related_name="pivot_movie_order"
    )
    buyed_by = models.ForeignKey(
        "users.User", on_delete=models.CASCADE, related_name="pivot_user_order"
    )
