# puppet manifest file to configure nginx server

exec { 'update':
  command => 'sudo apt update',
}

package { 'nginx':
  ensure => 'present',
}

file_line { 'host_name':
  ensure	=> present,
  path		=> '/etc/nginx/nginx.conf',
  line		=> "http {\n\tadd_header X-Served-By \"${hostname}\";",
  match		=> 'http {'
}

exec {'restart nginx':
  command  => 'sudo service nginx restart',
}
