# build_files.sh
# ref: https://www.devmaesters.com/blog/15
pip install -r requirements.txt
python3.9 manage.py collectstatic --noinput