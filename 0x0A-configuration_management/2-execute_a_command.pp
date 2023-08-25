# Using exec resource to kill a process name "killmenow"
exec { 'kill_killmenow_process':
command => 'pkill killmenow',
path    => '/usr/bin:/bin:/usr/sbin:/sbin',
}
