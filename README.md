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
Разработал проект с использованием чистой архитектуры, разделив его на слои: repository, service, view (handler).
<img width="574" alt="image" src="https://github.com/user-attachments/assets/9971f952-4e2f-47e2-b5f4-15fe11eab3c3" />

Для таких вложенных путей, как /orders/{order_pk}/products/{order_product_pk}/, использовал пакет drf-nested-routers.
Подключил Swagger API для упрощенного взаимодействия с API.
Для работы с транзакциями применял конструкцию with transaction.atomic().
Требования к статистике реализованы в эндпоинте: api/v1/order_products/statistics/.
