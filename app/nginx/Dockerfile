FROM nginx:1.25-alpine
RUN rm /etc/nginx/conf.d/default.conf
RUN mkdir -p /var/www/static
COPY default.conf /etc/nginx/conf.d