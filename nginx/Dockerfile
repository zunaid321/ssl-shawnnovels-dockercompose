FROM staticfloat/nginx-certbot:latest
RUN rm -rf /etc/nginx/user.conf.d/*

COPY ./default.conf /etc/nginx/conf.d/default.conf
