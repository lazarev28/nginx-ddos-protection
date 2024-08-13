FROM nginx:latest

RUN apt-get update && apt-get install -y fail2ban curl unzip


COPY nginx.conf /etc/nginx/nginx.conf
COPY fail2ban/jail.local /etc/fail2ban/jail.local
COPY fail2ban/filter.d/nginx-limit-req.conf /etc/fail2ban/filter.d/nginx-limit-req.conf

CMD service fail2ban start && nginx -g 'daemon off;'
