from django.db import models

# Create your models here.


class Season(models.Model):
    season_id = models.IntegerField(unique=True, null=False, default=None)
    name = models.CharField(max_length=10, unique=True, null=False, default=None)

    class Meta:
        verbose_name_plural = "Season"

    def __str__(self):
        return self.name


class Gameweek(models.Model):
    GAMEWEEK_CHOICES = [("Gameweek {}".format(i), "GW {}".format(i)) for i in range(1, 38)]
    name = models.CharField(max_length=20, choices=GAMEWEEK_CHOICES, null=False, default=None)
    season = models.ForeignKey(Season, verbose_name="Season", on_delete=models.DO_NOTHING)
    class Meta:
        verbose_name_plural = "Game week"

    def __str__(self):
        return f"{self.season}-{self.name}"


class Winner(models.Model):
    first_name = models.CharField(max_length=100, null=False, default=None)
    middle_name = models.CharField(max_length=100, null=True, default=None)
    last_name = models.CharField(max_length=100, null=False, default=None)
    email = models.EmailField(null=False, default=None)
    phone = models.CharField(max_length=20, null=True, default=None)
    profile_pic = models.ImageField(upload_to='images/', null=True, default=None)
    game_week = models.ForeignKey(Gameweek, verbose_name="Game week", on_delete=models.DO_NOTHING)

    class Meta:
        verbose_name_plural = "Winner"

    def __str__(self):
        if self.middle_name:
            return f"{self.first_name} {self.middle_name} {self.last_name}"
        else:
            return f"{self.first_name} {self.last_name}"
