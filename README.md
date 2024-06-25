# Деплой суперсета
## Подготовка
Из базовых требований предпочтительна свежая ОС Linux Debian / Ubuntu
Установленный git и docker.
Копируем репозиторий в целевую папку
```bash
cd /opt
git clone https://github.com/romankevich/bi_superset
```

Под пользователем root для Debian запускаем скрипт установки Docker
```bash
bash /opt/bi_superset/deploy/superset/debian-install-docker.sh
```
Для Ubuntu
```bash
bash /opt/bi_superset/deploy/superset/ubuntu-install-docker.sh
```
## Стратегия бэкапа
Непосредственно перед установкой суперсета правим/соглашаемся с бэкапом по умолчаниию
в файле /opt/bi_superset/deploy/superset/files/docker-compose-non-dev.yml
```yaml
  backup:
      image: postgres:15
      restart: unless-stopped
      depends_on:
        - db
      volumes:
        - /opt/bi/deploy/superset/backup:/backup
      command: >
        bash -c "while true; do
          PGPASSWORD=$$POSTGRES_PASSWORD pg_dump -h db-postgresql -U $$POSTGRES_USER -Fc $$POSTGRES_DB > /backup/$$(date +%Y-%m-%d-%H-%M-%S).dump
          echo ""Backup done at $$(date +%Y-%m-%d_%H:%M:%S)""
          ls -1 /backup/*.dump | head -n -7 | xargs rm -f
          sleep 86400
        done"
      environment:
        POSTGRES_USER: superset
        POSTGRES_PASSWORD: superset
        POSTGRES_DB: superset 
```
В блоке volumes прописан путь к папке, созданной в проекте. Если смонтировать постоянный внешний диск на другой ВМ, то в строке можно будет прописать путь к целевой папке

В блоке command есть настройка хранения количества дампов базы **| head -n -7 |** - по умолчанию хранится 7 дампов.
Интервалы между дампами задаются в секундах **sleep 86400** - по умолчанию раз в сутки.

## Установка и запуск суперсета
Всю работу по установке и запуску делает скрипт
```bash
bash /opt/bi_superset/deploy/superset/install-superset.sh
```
Порт в docker-compose-non-dev.yml по умолчанию выставлен на 8088. Сервис на хосте доступен по адресу http://localhost:8088/ с логином/паролем admin/admin

Сменить пароль админа можно через команду
```bash
docker exec -it superset_app /bin/bash
superset fab reset-password --username admin --password yourpassword
```
## Настройка https через Ngnix
Если провайдер хоста имеет сертификат верхнеуровневого домена, то для работы через https необходимо прописать следующие настройки.
```bash
cp /opt/bi_superset/deploy/superset/files/default.conf /etc/nginx/conf.d/
systemctl restart nginx
```
# Эксплуатация
## Остановка контейнеров и запуск сборки контейнеров
В случае наличия потребности изменить конфигуркцию в файле superset_config_docker.py необходимо остановить контейнеры и заново запустить сборку. Флаг -d запускает сборку в фоновом режиме.  
```bash
cd /opt/superset/
docker compose -f docker-compose-non-dev.yml down
docker compose -f docker-compose-non-dev.yml up -d
```
## Остановка и запуск суперсета
```bash
cd /opt/superset/
docker compose -f docker-compose-non-dev.yml stop
docker compose -f docker-compose-non-dev.yml start
```
## Восстановление из бэкапа
Останавливаем все контейнеры за исключением bd
```bash
cd /opt/superset/
docker stop superset_worker_beat
docker stop superset_worker
docker stop superset_app
docker stop superset_cache
docker stop backup
docker exec -i superset_db psql -U superset -d postgres -c "DROP DATABASE superset;"
docker exec -i superset_db psql -U superset -d postgres -c "CREATE DATABASE superset;"
docker exec -i superset_db psql -U superset -d superset -f /backup/file_name.dump
## если будут ошибки docker exec -it superset_db bin/bash -c "psql -U superset -d superset -c 'update dbs set password=null ; update dbs set encrypted_extra=null'"
docker stop superset_db;
docker compose -f docker-compose-non-dev.yml start
```