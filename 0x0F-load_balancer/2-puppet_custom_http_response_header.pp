# Install Nginx package using pappet
package { 'nginx':
  ensure => installed,
}

# configure HTTP header
file { '/etc/nginx/html/index.html':
  content => 'Hello World!',
}

# configure HTTP server
file_line { 'add_header':
  ensure => present,
  path   => '/etc/nginx/sites-available/default',
  line   => "\tadd_header X-Served-By '$HOSTNAME';",
  after  => "server_name _;"

# redirect
file_line { 'redirect':
  ensure => present,
  path   => '/etc/nginx/sites-available/default',
  after  => "add_header X-Server-By '$HOSTNAME'",
  line   => 'rewrite ^/redirect_me https://www.youtube.com/watch?v=QH2-TGUlwu4 permanent;',
}

# 404 error page
file { '/etc/nginx/html/404_page_error.html':
  ensure => file,
  content => "Ceci n'est pas une page",
  require => Package['nginx'],
}

# Define service
service { 'nginx':
  ensure  => running,
}
