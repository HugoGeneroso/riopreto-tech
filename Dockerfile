FROM nginx:alpine
COPY index.html /usr/share/nginx/html/index.html
COPY logo.svg /usr/share/nginx/html/logo.svg
COPY logo.jpg /usr/share/nginx/html/logo.jpg
COPY rio-webgl.html /usr/share/nginx/html/rio-webgl.html
COPY p/ /usr/share/nginx/html/p/
ENV PORT=80
COPY default.conf.template /etc/nginx/templates/default.conf.template
EXPOSE 80
