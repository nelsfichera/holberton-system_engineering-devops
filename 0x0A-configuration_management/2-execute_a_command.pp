#exec kill
exec { 'pkill':
  command => 'pkill killmenow',
  path    => '/bin/:/sbin/:/usr/bin/:/usr/sbin/',
}
