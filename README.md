# python-hello-web-monorepo

a full stack educational blog application written using three python web frameworks

## contents

1. architecture notes
2. contributing guidelines
   1. before coding
   2. while coding

## architecture notes

1. why django-first?
   1. because this is the only full stack component and requires a db connection.
   2. This will be responsible for our templating and UI.
   3. other frameworks can be implemented later as microservices (flask+fastAPI)
2. why poetry over virtualenv over venv, conda env, or other?
   1. `It is multi-platform and the goal is to make it work equally well on Linux, macOS and Windows.` in contrast to other options.
   2. It's lighter weight than conda.
   3. Poetry implements familiar idioms like lockfiles found in other, non-python package managers like Yarn.
   4. Poetry relies on newer versions of python (3.7+). This means that resources like tutorials and documentation using poetry will generally be more recent, which is a nice-to-have.
3. interesting tradeoff: monorepo vs multirepo
   1. in a commercial setting, we might prefer multirepo to de-noise single-project participation
   2. in this educational setting, the intent is to educate on all three frameworks, so we include all three in this single repo
4. note the use of [conventional commits](https://www.conventionalcommits.org/en/v1.0.0/) like the `chore:` prefix on the initial commit
5. During the installation of poetry, you may encounter 'SSL error'. In order to fix that, try directly use 'pipx install poetry'.
6. related django tutorials:
   1. https://rasulkireev.com/managing-django-with-poetry/
   2. https://justdjango.com/blog/build-a-blog-with-django

## setup

### running locally

As described in this [Flask implementation reference](https://github.com/vercel/examples/tree/main/python/flask):

```
vercel dev
```

When developing, make sure to [select the Poetry Python instance](https://code.visualstudio.com/docs/python/environments#_select-and-activate-an-environment) as the interpreter for VS Code to become aware of your installed dependencies.

If you are initially unable to locate the environment, try configuring the poetry virtualenv as follows:

```
poetry config virtualenvs.in-project true
```

You may also need to restart VS Code.

Note that this app was built in Python 3.11, although it may work with earlier versions idk.

You can also run via invoke like:
`poetry run invoke run-flask`

### build and deploy process

This app is deployed on Vercel. When you push a series of commits, please create a pull request. A Vercel GitHub Action / Hook will automatically create a preview environment and attempt to build and run tests.

After normal peer review, the code is merged to `main` and a build and deploy to PROD takes place.

## contributing guidelines

### before coding

1. please contribute a design doc design doc for major features
   1. a template can be found in `docs/template.md`
   2. existing designs are listed in `docs/index.md`
2. A major feature meets any of the following criteria:
   1. Includes a schema change
   2. Increases latency by more than 10 percent
   3. Updates more than 5 files or more than 100 lines of code
   4. Integrates a new third party service
3. Bug fixes and changes impacting less than 5 files and less than 100 lines of code do not require a design document.

### while coding

here are some code style opinions used in this repo:

1. try to recycle existing methods and patterns
2. ensure your code passes formatting and linting checks
3. For Django work, prefer Django classes where they exist.
4. For non-Django work, prefer functional patterns where possible
