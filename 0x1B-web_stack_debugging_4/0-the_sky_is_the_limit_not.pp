# fix the configuration of Nginx
# increase the amount of traffic an Nginx server can handle.

# increase the ULIMIT of the default file
exec { 'fix--for-nginx':
  command => '/bin/sed -i "s/15/4096/" /etc/default/nginx',
  path    => '/usr/local/bin/:/bin/'
}

# Restart Nginx
exec { 'nginx-restart':
  command => 'systemctl restart nginx',
  path    => '/bin/:/usr/bin/:/usr/sbin/'
}
