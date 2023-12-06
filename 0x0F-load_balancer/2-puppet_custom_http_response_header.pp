#!/usr/bin/env bash
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
  line   => "\tadd_header X-Served-By ${hostname};",
  after  => "server_name _;"
}

-> exec { 'restart_service':
  command  => 'sudo service nginx restart',
  provider => shell,
  require  => Package['nginx'],
}
