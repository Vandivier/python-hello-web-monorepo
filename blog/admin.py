import requests

from django.contrib.auth.mixins import UserPassesTestMixin
from django.views.generic import View
from django.contrib import admin
from .models import Post

class PostAdmin(UserPassesTestMixin, View, admin.ModelAdmin):
    list_display = ('title', 'slug', 'status','created_on')
    list_filter = ("status",)
    search_fields = ['title', 'content']
    prepopulated_fields = {'slug': ('title',)}

    # ref: https://stackoverflow.com/questions/53572251/django-2-1-3-error-init-takes-1-positional-argument-but-2-were-given
    # ref: https://stackoverflow.com/questions/45891128/django-cbv-userpassestestmixin-test-func-not-running
    def test_func(self):
        print("test......!!!")
        x = requests.get('https://w3schools.com/python/demopage.htm')
        print(x.text)
        # TODO: if authorized by third party
        # probably via https://docs.djangoproject.com/en/4.1/ref/middleware/#django.contrib.auth.middleware.PersistentRemoteUserMiddleware
        # https://gist.github.com/hughsaunders/1042719/bd78963eadf3efcc21ac35ac96912c5dbd1a2ff5
        return self.request.user.is_staff

admin.site.register(Post, PostAdmin.as_view())