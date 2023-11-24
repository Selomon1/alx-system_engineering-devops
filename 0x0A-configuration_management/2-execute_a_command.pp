# A manifest that kills a process named 'killmenow' using Puppet

exec { 'pkill':
  command => 'pkill killmenow',
  provider => 'shell',
}
