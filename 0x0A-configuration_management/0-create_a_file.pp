# Create a file named 'school' in /tmp using puppet

file {'/tmp/school':
  ensure => file,
  mode   => '0744',
  owner  => 'www-data',
  group  => 'I love Puppet',
}
