# teman_kelas
Project Untuk kelas AWS Arsitek di www.agunacourse.com

# Cara menjalankan project
sudo yum install git gcc mysql-devel python3-devel -y
git clone https://github.com/ArRosid/teman_kelas.git
pip3 install virtualenv
virtualenv -p python3 venv
source venv/bin/activate
pip install -r requirements.txt
python manage.py migrate
python manage.py runserver 0.0.0.0:8000
