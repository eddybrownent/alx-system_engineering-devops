# Updating the package lists
exec { 'update':
  command => '/usr/bin/apt-get update',
}

# Installing nginx
package { 'nginx':
  ensure => installed,
}

# Configure nginx to add a custom header
file {'/etc/nginx/sites-enabled/default':
  ensure  => present,
  content => "add_header X-Served-By \$hostname;",
  require => Package['nginx'],
}

# Restarting nginx
exec { 'nginx-restart':
  command => '/usr/sbin/service nginx restart',
}
