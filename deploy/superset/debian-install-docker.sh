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
    gnupg2 \
    software-properties-common \
&& curl -fsSL https://download.docker.com/linux/debian/gpg | apt-key add -  \
&& add-apt-repository --yes \
   "deb [arch=amd64] https://download.docker.com/linux/debian \
   $(lsb_release -cs) \
   stable" \
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