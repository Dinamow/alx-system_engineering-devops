#Create school file in temp

file {'school':
  ensure  => present,
  path    => '/tmp/school',
  mode    => '0744',
  content => 'I love Puppet',
  owner   => 'www-data',
  group   => 'www-data'
}