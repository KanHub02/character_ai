#!/bin/sh
cd src
echo "Подключаю Celery"
python -m celery -A core worker -l info
