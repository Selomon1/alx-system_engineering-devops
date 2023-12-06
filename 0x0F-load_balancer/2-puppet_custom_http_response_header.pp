# HTTP header response usind pappet
exec { 'update':
  command  => 'sudo apt-get update',
  provider => shell,
}

-> package { 'nginx':
  ensure => installed,
}

-> file_line { 'add_header':
  ensure => present,
  path   => '/etc/nginx/sites-available/default',
  line   => "\tadd_header X-Served-By '$HOSTNAME';",
  after  => "server_name _;"
}

-> exec { 'restart service':
  command  => 'sudo service nginx restart',
  provider => shell,
}
