# python-hello-web-monorepo

a full stack educational blog application written using three python web frameworks

# architecture notes

1. why django-first?
   1. because this is the only full stack component and requires a db connection.
   2. This will be responsible for our templating and UI.
   3. other frameworks can be implemented later as microservices (flask+fastAPI)
2. why poetry over virtualenv over venv, conda env, or other? just bc the tutorial said so; it's by no means proven to be the best option
   1. `It is multi-platform and the goal is to make it work equally well on Linux, macOS and Windows.` in contrast to other options.
   2. It's lighter weight than conda.
   3. Poetry implements familiar idioms like lockfiles found in other, non-python package managers like Yarn.
   4. Poetry relies on newer versions of python (3.7+). This means that resources like tutorials and documentation using poetry will generally be more recent, which is a nice-to-have.
3. interesting tradeoff: monorepo vs multirepo
   1. in a commercial setting, we might prefer multirepo to de-noise single-project participation
   2. in this educational setting, the intent is to educate on all three frameworks, so we include all three in this single repo
4. note the use of [conventional commits](https://www.conventionalcommits.org/en/v1.0.0/) like the `chore:` prefix on the initial commit
5. related django tutorials:
   1. https://rasulkireev.com/managing-django-with-poetry/
   2. https://justdjango.com/blog/build-a-blog-with-django

### Build and Deploy Process

1. Vercel, Render, and Railway are all live options
   1. For now, let's try Vercel
   2. Deploying all three to railway might put us over free tier, so we might pick multiple
   3. Downside of multiple: harder to build and deploy.
2. not using docker (for now)
   1. note a docker option: https://github.com/cloudacademy/python-flask-microservices
   2. but, where to deploy that?
3. Flask impl ref: https://github.com/vercel/examples/tree/main/python/flask
