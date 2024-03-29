from invoke import Context, task
from third_party_auth_api.app import app

@task
def run_flask(c: Context):
    app.run()

@task
def run_django(c: Context):
    c.run('python manage.py runserver')
