FROM nginx:alpine
COPY index.html /usr/share/nginx/html/index.html
COPY default.conf /etc/nginx/conf.d/default.conf
COPY start.sh /docker-entrypoint.d/40-start.sh
RUN chmod +x /docker-entrypoint.d/40-start.sh
EXPOSE 80
