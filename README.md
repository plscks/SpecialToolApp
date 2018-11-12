A little project I have been working on to catalog the special tools at my job, so as to circumvent the parts depatment.
I initially followed the tutorial from https://github.com/driscollis/flask101 to start to understand working with flask, I then altered the basic scafolding to fit my own purposes.


runs on python 3.7 with flask and SQLite3

the required modules are as follows:

```
sudo pacman -S sqlite3
pip install flask
pip install flask-sqlalchemy
pip install Flask-WTF
pip install flask_table
```

run webapp with:
```
FLASK_APP=main.py flask run
```
