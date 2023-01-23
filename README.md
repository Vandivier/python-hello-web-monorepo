# python-hello-web-monorepo

a full stack educational blog application written using three python web frameworks

# architecture notes

1. why django-first?
   1. because this is the only full stack component and requires a db connection.
   2. This will be responsible for our templating and UI.
   3. other frameworks can be implemented later as microservices (flask+fastAPI)
2. why poetry over virtualenv over venv, conda env, or other? just bc the tutorial said so; it's by no means proven to be the best option
   1. specifically, tutorial recommended virtualenv for windows dev instead of venv
   2. why poetry? `It is multi-platform and the goal is to make it work equally well on Linux, macOS and Windows.` in contrast to venv/virtualenv. Also, it implements familiar idioms like lockfiles from other, non-python package managers like Yarn.
   3. poetry relies on newer versions of python (3.7+)
3. interesting tradeoff: monorepo vs multirepo
   1. in a commercial setting, we might prefer multirepo to de-noise single-project participation
   2. in this educational setting, the intent is to educate on all three frameworks, so we include all three in this single repo
4. note the use of [conventional commits](https://www.conventionalcommits.org/en/v1.0.0/) like the `chore:` prefix on the initial commit
