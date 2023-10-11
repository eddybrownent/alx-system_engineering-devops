# use to fix a line in settings for a file not found error
exec{ 'line_replace':
  command => 'sed -i s/phpp/php/g /var/www/html/wp-settings.php',
  path    => 'usr/local/bin/:/bin/'
}
