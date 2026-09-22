FROM nginx:alpine
COPY index.html /usr/share/nginx/html/index.html
COPY logo.svg /usr/share/nginx/html/logo.svg
COPY logo-*.png /usr/share/nginx/html/
COPY p/ /usr/share/nginx/html/p/
ENV PORT=80
COPY default.conf.template /etc/nginx/templates/default.conf.template
EXPOSE 80
