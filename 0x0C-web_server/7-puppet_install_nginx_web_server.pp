i#automating my work using Puppet

package { 'nginx':

ensure => installed,

}

file_line { 'install':

ensure => 'present'

path => /etc/nginx/sites-available/default',

after => 'listen 80 default_server;',

} line => 'rewrite ^/redirect_me https://www.youtube.com/ permanent;,

file '/var/www/html/index.html':

content => 'Hello world!',

}

service 'nginx':

ensure => running,

require => Package['nginx'],
}
