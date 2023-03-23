WEB INFRASTRUCTURE DESIGN

![WEB INFRA 1](https://user-images.githubusercontent.com/113608901/227137232-443b7e8a-3ecb-4baf-b457-cd13cd876b35.png)

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

![download (3)](https://user-images.githubusercontent.com/113608901/227139884-10943df3-a2c0-44e8-a416-2888c8b969ef.jpg)

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

![download (4)](https://user-images.githubusercontent.com/113608901/227140075-b4948bb7-9f4c-4faf-acc2-eba64d51e47b.jpg)

3 firewalls
1 SSL certificate to serve www.foobar.com over HTTPS
3 monitoring clients (data collector for Sumologic or other monitoring services)
