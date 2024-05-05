#!/usr/bin/env bash
# Install Nginx if it's not already installed
apt-get update
apt-get install -y nginx

# Create the necessary directories
mkdir -p /data/web_static/releases/test/
mkdir -p /data/web_static/shared/

# Create a fake HTML file
echo "<html>
  <head>
  </head>
  <body>
    Holberton School
  </body>
</html>" > /data/web_static/releases/test/index.html

# Create a symbolic link
if [ -h /data/web_static/current ]; then
    rm /data/web_static/current
fi
ln -sf /data/web_static/releases/test/ /data/web_static/current

# Change the ownership of the /data/ folder
chown -R ubuntu:ubuntu /data/

# Update the Nginx configuration
cat << EOF > /etc/nginx/sites-available/default
server {
    listen 80;
    listen [::]:80;
    
    root /var/www/html;
    index index.html index.htm index.nginx-debian.html;

    location /hbnb_static/ {
        alias /data/web_static/current/;
        index index.html;
    }
}
EOF

# Restart Nginx
sudo service nginx restart

# Exit successfully
exit 0

