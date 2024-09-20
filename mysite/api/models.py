from django.db import models

class BlogPost(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    published_data = models.DateField(auto_now_add=True)
    
    def __str__(self):
        return self.title
    
    
