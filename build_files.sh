# Add the --break-system-packages flag to bypass the error
pip install -r requirements.txt --break-system-packages

python3.9 manage.py collectstatic --noinput
