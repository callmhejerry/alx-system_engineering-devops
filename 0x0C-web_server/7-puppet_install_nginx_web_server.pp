# configuration for the nginx server

package { 'nginx':
  name		   => 'nginx',
  ensure	   => installed,
  install_options  => ['-y'],
  provider         => 'apt',
}

service { 'nginx':
  name		=> 'nginx',
  ensure	=> running,
  hasrestart    => true,
  restart	=> 'sudo service nginx restart',
  require	=> [
    Package['nginx'],
    File['default_server'],
    File['homepage'],
  ],
}

$server_content = "
server {
	listen 80 default_server;
	listen [::]:80 default_server;

	root /var/www/html;
	rewrite ^/redirect_me \"https://github.com\" permanent;
	
	index index.html index.htm;

	location /{
		try_files \$uri \$uri/ =404;
	}
	server_name _;
}
"


file { 'default_server':
  ensure	=> present,
  path		=> '/etc/nginx/sites-available/default',
  content	=> $server_content,
  replace	=> true,
  require	=> File['homepage'],
}


file { 'homepage':
  ensure	=> present,
  path		=> '/var/www/html/index.html',
  content	=> "Hello World!\n",
  replace	=> true,
}
