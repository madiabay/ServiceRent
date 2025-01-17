# clone the project
git clone https://github.com/madiabay/ServiceRent.git

# install depends and activate venv
poetry install
poetry shell
or
python3 -m venv venv
source ./venv/bin/activate
pip install -r requirements.txt

# run project
./manage.py migrate
./manage.py runserver

# APIs swagger url
http://127.0.0.1:8000/swagger/


# Краткое описание проекта
<img width="574" alt="image" src="https://github.com/user-attachments/assets/9971f952-4e2f-47e2-b5f4-15fe11eab3c3" />
