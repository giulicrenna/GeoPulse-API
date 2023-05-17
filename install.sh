#!/bin/bash

SERVICE="api_service.service"
FOLDER_NAME="api_service"
ROOT_NAME="smarttag-api"
PORT=8000
PROTOCOL="tcp"

pip install -r requirements.txt --break-system-packages

ufw allow $PORT/$PROTOCOL

mkdir $ROOT_NAME
cp -r ../$ROOT_NAME /etc/$ROOT_NAME

chmod +x /etc/$ROOT_NAME/run.sh

cp $SERVICE /etc/systemd/system/$SERVICE

systemctl start $SERVICE
systemctl enable $SERVICE