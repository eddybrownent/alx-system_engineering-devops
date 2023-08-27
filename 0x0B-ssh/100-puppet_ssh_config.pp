#!/usr/bin/env puppet
# This script uses Puppet to make changes in the SSH client configuration file

file { '/etc/ssh/ssh_config':
  ensure  => present,
  content =>"
            # Puppet-managed SSH client configuration
            Host *
            IdentityFile ~/.ssh/school
            PasswordAuthentication no
            ",
}
