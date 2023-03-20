# build_files.sh
# ref: https://www.devmaesters.com/blog/15
pip install -r requirements.txt
python manage.py collectstatic --noinput