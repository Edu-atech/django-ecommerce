# remove the db
rm -rf db.sqlite3

# run the migrations
python manage.py makemigrations
python manage.py migrate

# create the superuser
echo "from accounts.models import CustomUser; CustomUser.objects.create_superuser('eduardo', 'eduardo@email.com', 'password123')" | python manage.py shell