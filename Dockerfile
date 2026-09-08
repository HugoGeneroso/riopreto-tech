FROM nginx:alpine
COPY index.html /usr/share/nginx/html/index.html
# template do nginx: envsubst substitui ${PORT} automaticamente no entrypoint oficial
ENV PORT=80
COPY default.conf.template /etc/nginx/templates/default.conf.template
EXPOSE 80
