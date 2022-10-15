sudo unlink /etc/nginx/sites-enabled/default
sudo ln -sf /home/box/etc/nginx.conf  /etc/nginx/sites-enabled/default
sudo /etc/init.d/nginx restart
gunicorn web.hello --bind 0.0.0.0:8080