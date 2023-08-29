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
  require => Package['nginx'],
}

# Configuring the redirection nginx server
exec { 'configure-nginx-redirect':
  command => '/bin/bash -c "sed -i \'s/server_name _;/server_name _;\n\n  location = \\/redirect_me { return 301 http:\\/\\/www.youtube.com\\/watch?v=QH2-TGUlwu4; }/\' /etc/nginx/sites-available/default"',
}

# configuring nginx to listen on port 80
exec { 'configure-nginx-listen':
  command => '/bin/bash -c "sed -i \'s/listen 80;/listen 80 default_server;/\' /etc/nginx/sites-available/default"',
  require => Package['nginx'],
}

# creatinag a page that returns Hello World!
file { '/var/www/html/index.html':
  ensure  => present,
  content => "Hello World!\n",
}

# Restarting nginx
exec {'restart':
  command  => 'service nginx restart',
  provider => shell,
}
