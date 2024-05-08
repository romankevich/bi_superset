#!/bin/bash

start=$(date +%s)
# Проверим, что скрипт запущен от root
if [ "$(id -u)" != "0" ]; then
    echo "Скрипт должен быть запущен от пользователя root"
    exit 1
fi

apt-get update -y \
&& apt-get install -y \
    apt-transport-https \
    ca-certificates \
    curl \
&& install -m 0755 -d /etc/apt/keyrings \
&& curl -fsSL https://download.docker.com/linux/ubuntu/gpg -o /etc/apt/keyrings/docker.asc  \
&& chmod a+r /etc/apt/keyrings/docker.asc \
&& echo \
  "deb [arch=$(dpkg --print-architecture) signed-by=/etc/apt/keyrings/docker.asc] https://download.docker.com/linux/ubuntu \
  $(. /etc/os-release && echo "$VERSION_CODENAME") stable" | \
  tee /etc/apt/sources.list.d/docker.list > /dev/null \
&& apt-get update -y \
&& apt-get install -y docker-ce docker-ce-cli containerd.io docker-buildx-plugin docker-compose-plugin \
&& systemctl start docker \
&& systemctl enable docker.service \
&& systemctl enable containerd.service \
&& docker run hello-world

end=$(date +%s)
echo '\033[1;36mУстановка docker завершена за '$(($end-$start))' секунд!\033[0m' #морская волна
systemctl status docker.service \
&& docker version