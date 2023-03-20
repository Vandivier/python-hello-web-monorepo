import os
from django.http import HttpRequest
import requests

from django.contrib.auth.models import User
from django.contrib import admin
from .models import Post

# ref: https://stackoverflow.com/questions/2431727/django-admin-hide-a-model
# ref: https://docs.djangoproject.com/en/4.1/ref/middleware/#django.contrib.auth.middleware.PersistentRemoteUserMiddleware
# ref: https://gist.github.com/hughsaunders/1042719/bd78963eadf3efcc21ac35ac96912c5dbd1a2ff5
# ref: https://stackoverflow.com/questions/53572251/django-2-1-3-error-init-takes-1-positional-argument-but-2-were-given
# ref: https://stackoverflow.com/questions/45891128/django-cbv-userpassestestmixin-test-func-not-running
class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'slug', 'status','created_on')
    list_filter = ("status",)
    search_fields = ['title', 'content']
    prepopulated_fields = {'slug': ('title',)}

    def has_module_permission(self, request: HttpRequest) -> bool:
        microservice_url = os.environ.get("NEXT_PUBLIC_VERCEL_URL")
        email = ""
        if isinstance(request.user, User):
            email = request.user.email
        else:
            return False

        response: requests.Response = requests.get(f"{microservice_url}/third-party-auth?username={email}")
        return response.json().get("hasAuthor", False)

admin.site.register(Post, PostAdmin)
