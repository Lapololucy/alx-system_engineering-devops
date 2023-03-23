WEB INFRASTRUCTURE DESIGN
$'/c/Users/P\'LUCY/Desktop/alx pre coure/WEB INFRA 1.png'

Web Applications Infrastructure/Web Infrastructure also called internet infrastructure is the physical hardware, transmission media, and software used to interconnect computers and users on the Internet.

Simple Web Infrastructure
Distributed Web Infrastructure
Monitored Web Infrastructure
LEARNING OBJECTIVES
You must be able to draw a diagram covering the web stack you built with the *sysadmin/devops* track projects
You must be able to explain what each component is doing
You must be able to explain system redundancy
Know all the mentioned acronyms: LAMP, SPOF, QPS

SIMPLE WEB INFRASTRUCTURE
$'/c/Users/P\'LUCY/Desktop/alx pre coure/WEB INFRA 2.webp'

1 server
1 web server (Nginx)
1 application server
1 application files (your code base)
1 database (MySQL)
1 domain name foobar.com configured with a www record that points to your server IP 8.8.8.8

DISTRUBUTED WEB INFRASTURE
2 servers
1 web server (Nginx)
1 application server
1 load-balancer (HAproxy)
1 set of application files (your code base)
1 database (MySQL)

MONITORED WEB INFRASTRUCTURE

$'/c/Users/P\'LUCY/Desktop/alx pre coure/WEB INFRA 3.webp'
