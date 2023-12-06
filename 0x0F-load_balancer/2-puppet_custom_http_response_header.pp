#!/usr/bin/env bash
# Install Nginx package using pappet
package { 'nginx':
  ensure => installed,
}

# Custome to retrieve the server's hostname
$wser_hostname = $facts['hostname']

# configure HTTP header
file { '/etc/nginx/sites-available/default':
  ensure => file,
  content => "server {
    listen 80;
    add_header X-Served-By '$HOSTNAME';

    location /redirect_me {
        return 301 https://www.youtube.com/watch?v=QH2-TGUlwu4;
    }

    error_page 404 /404_page_error.html;
    location /404 {
        root /etc/nginx/html;
        internal;
    }
  }",
  require => Package['nginx']
  notify  => Service['nginx']
}

# Define service
service { 'nginx':
  ensure => running,
  enable => true,
  require => File['/etc/nginx/sites-available/default',
		  '/etc/nginx/html/404_page_error.html'],
}
