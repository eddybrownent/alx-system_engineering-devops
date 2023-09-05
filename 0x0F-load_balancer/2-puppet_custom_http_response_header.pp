# Updating the package lists
exec { 'update':
  command => 'apt-get update',
}

# Installing nginx
package { 'nginx':
  ensure => installed,
}

# Configure nginx to add a custom header
file {'/etc/nginx/sites-enabled/default'
  ensure  => present,
  content => "add_header X-Served-By \$hostname;",
  require => Package['nginx'],
}

# Restarting nginx
exec { 'nginx-restart':
  command => 'service nginx restart',
}
