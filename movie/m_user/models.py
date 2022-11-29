

from django.db import models

class MUser(models.Model):
    use_in_migrations = True
    id = models.IntegerField(primary_key=True, auto_created=True)
    email = models.TextField()
    nickname = models.TextField()
    password = models.TextField()
    age = models.IntegerField()

    class Meta:
        db_table = "m_user"

    def __str__(self):
        return f'{self.pk}{self.email}{self.nickname}{self.password}{self.age}'

class Movie(models.Model):
    use_in_migrations = True
    id = models.IntegerField(primary_key=True, auto_created=True)
    title = models.TextField()
    director = models.TextField()
    description = models.TextField()
    poster_url = models.TextField()
    running_time = models.IntegerField()
    age_rating = models.IntegerField()


    class Meta:
        db_table = "Movie"

    def __str__(self):
        return f'{self.pk}{self.title}{self.director}{self.description}{self.poster_url}{self.running_time}{self.age_rating}'

class Cinema(models.Model):
    use_in_migrations = True
    id = models.IntegerField(primary_key=True, auto_created=True)
    title = models.TextField()
    image_url = models.TextField()
    address = models.TextField()
    detail_address = models.TextField()



    class Meta:
        db_table = "Cinema"

    def __str__(self):
        return f'{self.pk}{self.title}{self.image_url}{self.address}{self.detail_address}'


class Showtime(models.Model):
    use_in_migrations = True
    id = models.IntegerField(primary_key=True, auto_created=True)
    start_time = models.TextField()
    end_time = models.TextField()


    class Meta:
        db_table = "Showtime"

    def __str__(self):
        return f'{self.pk}{self.start_time}{self.end_time}'


class Theater(models.Model):
    use_in_migrations = True
    id = models.IntegerField(primary_key=True, auto_created=True)
    title = models.TextField()
    seat = models.TextField()

    class Meta:
        db_table = "Theater"

    def __str__(self):
        return f'{self.pk}{self.title}{self.seat}'

class TheaterTicket(models.Model):
    use_in_migrations = True
    id = models.IntegerField(primary_key=True, auto_created=True)
    x = models.IntegerField()
    y = models.IntegerField()

    class Meta:
        db_table = "TheaterTicket"

    def __str__(self):
        return f'{self.pk}{self.x}{self.y}'