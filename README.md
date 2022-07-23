# teman_kelas
Project Untuk kelas AWS Arsitek di www.agunacourse.com

# Cara menjalankan project
- sudo yum install git gcc mysql-devel python3-devel -y

- git clone https://github.com/ArRosid/teman_kelas.git
- cd teman_kelas

- pip3 install virtualenv
- virtualenv -p python3 venv
- source venv/bin/activate

- pip install -r requirements.txt

- cp teman_kelas/.env.example teman_kelas/.env
- nano teman_kelas/.env

- python manage.py migrate
- python manage.py runserver 0.0.0.0:8000


# serve with uwsgi & nginx
- sudo amazon-linux-extras enable nginx1
- sudo yum clean metadata
- sudo yum install nginx

- sudo nano /etc/nginx/conf.d/django.conf
```
upstream django {
    server unix:///run/uwsgi/teman_kelas.sock;
}

server {
    listen	80;
    server_name 54.89.170.191;
    charset     utf-8;

    location = /favicon.ico { access_log off; log_not_found off; }
    location /static/ {
        alias /usr/share/nginx/html/static/;
    }

    location / {
        uwsgi_pass  django;
        include     /etc/nginx/uwsgi_params;
    }
}
```

- sudo cp static /usr/share/nginx/html/ -rf
- sudo systemctl restart nginx
- sudo systemctl enable nginx

- pip install uwsgi
- sudo mkdir /run/uwsgi/
- sudo chown ec2-user:ec2-user /run/uwsgi/

- uwsgi --socket /run/uwsgi/teman_kelas.sock --chdir /home/ec2-user/teman_kelas/ --module teman_kelas.wsgi --chmod-socket=666

- sudo mkdir -p /etc/uwsgi/sites
- sudo nano /etc/uwsgi/sites/teman_kelas.ini

```
[uwsgi]
chdir = /home/ec2-user/teman_kelas/
module = teman_kelas.wsgi
home = /home/ec2-user/teman_kelas/venv/
master = true
processes = 10
socket = /run/uwsgi/teman_kelas.sock
chmod-socket = 666
vacuum = true
```


- sudo nano /etc/systemd/system/teman_kelas.service
```
[Unit]
Description=Teman Kelas Emperor service

[Service]
ExecStartPre=/bin/bash -c 'mkdir -p /run/uwsgi; chown ec2-user:ec2-user /run/uwsgi'
ExecStart=/home/ec2-user/teman_kelas/venv/bin/uwsgi --emperor /etc/uwsgi/sites
Restart=always
KillSignal=SIGQUIT
Type=notify
NotifyAccess=all

[Install]
WantedBy=multi-user.target
```

- sudo systemctl start teman_kelas
- sudo systemctl enable teman_kelas
