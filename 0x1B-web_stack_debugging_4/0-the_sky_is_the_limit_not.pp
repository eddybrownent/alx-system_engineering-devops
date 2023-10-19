# fix the configuration of Nginx
# increase the amount of traffic an Nginx server can handle.

# increase the ULIMIT of the default file
exec { 'fix--for-nginx':
  command => '/bin/sed -i "s/15/5000/" /etc/default/nginx',
  path    => '/usr/local/bin/:/bin/'
}

# Restart Nginx
exec { 'nginx-restart':
  command => 'service nginx restart',
  path    => '/usr/local/bin/:/bin/'
}
