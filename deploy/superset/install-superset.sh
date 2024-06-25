#!/bin/bash

start=$SECONDS
# Проверим, что скрипт запущен от root
if [ "$(id -u)" != "0" ]; then
    echo "Скрипт должен быть запущен от пользователя root"
    exit 1
fi

cd /opt \
&& git clone https://github.com/apache/superset.git \
&& cd superset \
&& git checkout 4.0.0

echo -e '\033[1;33mКлонирование завершено, копируем файлы и запускаем compose\033[0m' #желтый

cp /opt/bi_superset/deploy/superset/files/docker-compose-non-dev.yml /opt/superset/
cp /opt/bi_superset/deploy/superset/files/.env-non-dev /opt/superset/docker/
cp /opt/bi_superset/deploy/superset/files/requirements-local.txt /opt/superset/docker/
cp /opt/bi_superset/deploy/superset/files/superset_config_docker.py /opt/superset/docker/pythonpath_dev/

docker compose -f docker-compose-non-dev.yml up -d

duration=$((SECONDS - start))
echo '\033[1;36mУстановка и запуск superset завершено за '$duration' секунд!\033[0m' #морская волна
