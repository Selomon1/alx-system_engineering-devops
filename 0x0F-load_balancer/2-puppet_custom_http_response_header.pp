# Install Nginx package using pappet
exec { 'update':
  command  => 'sudo apt-get update',
  provider => shell,
}

-> package { 'nginx':
  ensure => installed,
}

# configure HTTP server
-> file_line { 'add_header':
  ensure => present,
  path   => '/etc/nginx/sites-available/default',
  line   => "\tadd_header X-Served-By '$HOSTNAME';",
  after  => "server_name _;"
}

service { 'nginx':
  ensure  => running,
}
