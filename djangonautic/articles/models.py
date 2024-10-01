from django.db import models
from django.contrib.auth.models import User

class Article(models.Model):
    title = models.CharField(max_length=100)
    slug = models.SlugField(unique=True)  # Ensure unique slugs
    body = models.TextField()
    date = models.DateTimeField(auto_now_add=True)
    thumb = models.ImageField(default='default.png', blank=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE, default=None, related_name='articles')

    def __str__(self):
        return self.title

    def snippet(self):
        """Return a snippet of the article body."""
        return self.body[:50] + '...' if len(self.body) > 50 else self.body

    def word_count(self):
        """Count the number of words in the article body."""
        return len(self.body.split())

    def reading_time(self):
        """Estimate the reading time in minutes."""
        words_per_minute = 200  # Average reading speed
        minutes = self.word_count() / words_per_minute
        return round(minutes)  # Round to the nearest minute
