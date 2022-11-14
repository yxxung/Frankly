# production stage

FROM nginx:stable-alpine as production-stage

COPY ./dist /usr/share/nginx/html

COPY ./nginx.conf /etc/nginx/conf.d/default.conf

#COPY ./data/certbot/conf /etc/letsencrypt
#COPY ./data/certbot/www /var/www/certbot


EXPOSE 8080

CMD ["nginx", "-g", "daemon off;"]
