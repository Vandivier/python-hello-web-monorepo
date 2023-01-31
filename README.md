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
5. related django tutorials:
   1. https://rasulkireev.com/managing-django-with-poetry/
   2. https://justdjango.com/blog/build-a-blog-with-django

## contributing guidelines

### before coding

1. please contribute a design doc design doc for major features
   1. a template can be found in `docs/template.md`
   2. existing designs are listed in `docs/index.md`
2. TODO: define a major feature
3. TODO: define safe harbor for small changes where no design doc is needed

### while coding

here are some code style opinions used in this repo:

1. try to recycle existing methods and patterns
2. ensure your code passes formatting and linting checks
3. For Django work, prefer Django classes where they exist.
4. For non-Django work, prefer functional patterns where possible
