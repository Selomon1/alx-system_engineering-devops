# Client configuration file to connect to a server without passwd.

file_line { 'passwd_auth_path':
  path => '/etc/ssh/ssh_config',
  line => 'PasswordAuthentication no',
}

file_line { 'passwd_path':
  path => '/etc/ssh/ssh_config',
  line => 'IdentityFile ~/.ssh/school',
}
