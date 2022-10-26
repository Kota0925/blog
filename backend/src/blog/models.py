from django.db import models

class User(models.Model):
    name = models.CharField(max_length=32)
    mail = models.EmailField()

    def __str__(self):
        return "{}: {}".format(self.pk, self.name)


class Article(models.Model):
    STATUS_SET = (
            ("draft", "下書き"),
            ("public", "公開中"),
    )
    title = models.CharField(max_length=128)
    body = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    status = models.CharField(choices=STATUS_SET, default="draft", max_length=8)
    author = models.ForeignKey(User, related_name='articles', on_delete=models.CASCADE)
    
    def __str__(self):
        return self.title
