#!/bin/sh
# Substitui a porta 80 pela $PORT do Railway no template do nginx
sed -i "s/listen 80;/listen ${PORT:-80};/" /etc/nginx/conf.d/default.conf
exec nginx -g 'daemon off;'
