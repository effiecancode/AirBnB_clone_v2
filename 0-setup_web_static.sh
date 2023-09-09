#!/usr/bin/env bash
# sets up the web servers for the deployment of web_static

sudo apt-get -y update
sudo apt-get -y upgrade
sudo apt-get -y install nginx

# Create necessary directories
sudo mkdir -p /data/web_static/releases/test /data/web_static/shared

# Create a string for testing
echo "You got this babygirl" | sudo tee /data/web_static/releases/test/index.html

# Create if not existing a symbolic link
sudo ln -sf /data/web_static/releases/test/ /data/web_static/current

# Give ownership of the /data/ folder to the ubuntu
sudo chown -hR ubuntu:ubuntu /data/

# Update Nginx configuration to serve /data/web_static/current/ at hbnb_static folder
sudo sed -i '38i\\tlocation /hbnb_static/ {\n\t\talias /data/web_static/current/;\n\t}\n' /etc/nginx/sites-available/default
#start nginx
sudo service nginx start
