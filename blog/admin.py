from django.contrib import admin
from .models import Article,Photo,Entry

# Register your models here.
admin.site.register(Article)
admin.site.register(Entry)
admin.site.register(Photo)
