from django.db import models

class BUser(models.Model):
    use_in_migrations = True
    id = models.IntegerField(primary_key=True, auto_created=True, max_length=30)
    email = models.TextField()
    nickname = models.TextField()
    password = models.TextField()


    class Meta:
        db_table = "b_users"

    def __str__(self):
        return f'{self.pk}{self.email}{self.nickname}{self.password}'

class Post(models.Model):
    use_in_migrations = True
    id = models.IntegerField(primary_key=True, auto_created=True, max_length=30)
    title = models.TextField()
    content = models.TextField()
    created_at = models.TextField()
    updated_at = models.TextField()


    class Meta:
        db_table = "Post"

    def __str__(self):
        return f'{self.pk}{self.title}{self.content}{self.created_at}{self.updated_at}'

class Tag(models.Model):
    use_in_migrations = True
    id = models.IntegerField(primary_key=True, auto_created=True, max_length=30)
    title = models.TextField()



    class Meta:
        db_table = "Tag"

    def __str__(self):
        return f'{self.pk}{self.title}'

class View(models.Model):
    use_in_migrations = True
    id = models.IntegerField(primary_key=True, auto_created=True, max_length=30)
    ip_address = models.TextField()
    created_at = models.TextField()

    class Meta:
        db_table = "View"

    def __str__(self):
        return f'{self.pk}{self.ip_address}{self.created_at}'

class Comment(models.Model):
    use_in_migrations = True
    id = models.IntegerField(primary_key=True, auto_created=True, max_length=30)
    content = models.TextField()
    created_at = models.TextField()
    updated_at = models.TextField()


    class Meta:
        db_table = "Comment"

    def __str__(self):
        return f'{self.pk}{self.content}{self.created_at}{self.updated_at}'
