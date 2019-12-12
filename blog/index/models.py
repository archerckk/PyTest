from django.db import models

# Create your models here.
class Question(models.Model):
    def __str__(self):
        return self.title

    title=models.CharField(max_length=50)
    question_text=models.CharField(max_length=200)
    pub_date=models.DateTimeField('date published')

class Choice(models.Model):
    def __str__(self):
        return self.choice_text

    question=models.ForeignKey(Question,on_delete=models.CASCADE)
    choice_text=models.CharField(max_length=200)
    votes=models.IntegerField(default=0)


class Article(models.Model):
    title = models.CharField(max_length=50)
    content = models.CharField(max_length=200)


class Comment(models.Model):
    article_id=models.ForeignKey(Article,on_delete=models.CASCADE)
    content=models.CharField(max_length=500)


class User(models.Model):
    user_name=models.CharField(max_length=20,unique=True)
    password=models.CharField(max_length=20)
    article=models.ForeignKey(Article,on_delete=models.CASCADE,null=True)
    content=models.ForeignKey(Comment,on_delete=models.CASCADE,null=True)