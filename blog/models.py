from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse
from users.models import Profile




class Post(models.Model):
	title = models.CharField(max_length=200, help_text='Bir Post Başlığı girniz.')
	author = models.ForeignKey(User,on_delete=models.CASCADE,null=True)
	content = models.TextField()
	date_posted = models.DateField(default=timezone.now)
	


	def get_absolute_url(self):
		"""Returns the url to access a detail record for this book."""
		return reverse('post-detail',args=[str(self.pk)])
	

	def __str__(self):
		return self.title



