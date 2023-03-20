# build_files.sh
# ref: https://www.devmaesters.com/blog/15
python3 -m pip install -r requirements.txt
python3 manage.py collectstatic --noinput