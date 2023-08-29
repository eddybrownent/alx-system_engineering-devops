# Installing nginx
package { 'nginx':
  ensure => installed,
}

# To make sure the nginx service is up and running
service { 'nginx':
  ensure  => running,
  require => package['nginx'],
}

# configuration for listening and redirection
file_line { 'config':
  ensure => 'present',
  path   => '/etc/nginx/sites-enabled/default',
  after  => 'listen 80 default_server;',
  line   => 'rewrite ^/redirect_me https://www.youtube.com/watch?v=QH2-TGUlwu4 permanent;',
}

# creating a page that returns Hello World!
file {'/var/www/html/index.html':
  content  => 'Hello',
}
