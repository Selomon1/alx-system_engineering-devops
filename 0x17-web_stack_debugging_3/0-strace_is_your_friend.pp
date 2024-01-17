# Fix the problem identified
file { '/var/www/html/wp-settings.php':
  ensure  => file,
  content => inline_template('<%= File.read("/var/www/html/wp-settings.php").gsub("phpp", "php") %>'),
  notify  => Exec['reload-apache'],
}

exec { 'reload-apache':
  command => 'service apache2 reload',
  refreshonly => true,
}
