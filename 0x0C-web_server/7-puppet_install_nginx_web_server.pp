# Updating the package list
exec { 'apt-update':
  command => '/usr/bin/apt-get update',
}

# Installing nginx
package { 'nginx':
  ensure => installed,
}

# To make sure the nginx service is up and running
service { 'nginx':
  ensure  => running,
  require => package['nginx'],
}

# Configuring the redirection nginx server
exec { 'configure-nginx-redirect':
  command  => 'sed -i \'s/server_name _;\n\trewrite ^\/redirect_me https:\\/\\/www.youtube.com\\/watch?v=QH2-TGUlwu4 permanent \
  /etc/nginx/sites-enabled/default,'
  provider => shell,
}

# configuring nginx to listen on port 80
exec { 'configure-nginx-listen':
  command  => 'sed -i \'s/listen 80;/listen 80 default_server;/\' /etc/nginx/sites-available/default',
  provider => 'shell',
  require  => Package['nginx'],
}

# creatinag a page that returns Hello World!
exec {'Helloworld-file':
  command  => 'echo "Hello World!" > /var/www/html/index.html',
  provider => shell,
}

# Restarting nginx
exec {'restart':
  command  => 'service nginx restart',
  provider => shell,
}
