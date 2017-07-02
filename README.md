# LinuxHttpBox
## Vagrant box to run an Apache HTTP server on Centos 7

This repository provides a virtual machine environment to run a web-server for development and testing.
The installation is based on Vagrant by HashiCorp https://www.vagrantup.com/

## Pre-requisites
- This installation requires about 3 to 4 GB of disk-space (VirtualBox software, and virtual machine disk) on your computer. You should have at least 4GB RAM.
- The current configuration uses ports 2222 and 8080. If you run other applications that try to use these ports you need to change the corresponding entries in the `Vagrant` file.
- You should have a fast internet connection when performing these steps.

## Setup
1. Download and install the Vagrant software from https://www.vagrantup.com/downloads.html for your operating system. Documentation https://www.vagrantup.com/intro/index.html
2. Download or clone this repository anywhere on your computer.
3. Open a terminal or command line window on your computer and navigate into the directory, that you just created by downloading this repository.
4. Run the command `vagrant up` in your terminal (or command line window). This might take a while: the system will create a new virtual machine and install the operating system with all the required packages.

There might be a couple of warnings...usually nothing to be concerned about. After the installation is completed point your browser to http://localhost:8080

## Running the virtual machine
The virtual machine is running after the installation process. If you are not using the web-server you can shut it down with the command `vagrant halt` in order to free resources.

The next time you need it, run the command `vagrant up`. This time it will not reinstall the software but start-up right away.

If you ever need to get rid of the virtual machine, or need to reinstall from scratch use the command `vagrant destroy`.

### Document root of the web-server
- The web-server expects any files (HTML, JS, CSS, images, etc.) in folders under the `www/html` directory. (`www/html` is the so-called "Document Root")
- CGI scripts are kept in `www/cgi-bin`. You'll find an example `hello.py`. Test it with http://localhost:8080/cgi-bin/hello.py
- Log files are written to the `log/httpd` directory. Here `log/httpd/access_log` tracks successful events, while `log/httpd/error_log` tracks when problems occur. This is particularly helpful when debugging CGIs.
- The directory on the host system (i.e. your computer) is mounted to `/vagrant` on the virtual machine. E.g. if you have CGI scripts that need to read or write files into the `data` directory use the path `/vagrant/data` on the virtual machine.

### SSH login
You can login to the virtual machine via SSH on port 2222. E.g. with `ssh vagrant@localhost -p 2222` from a UNIX command line. Or with any other SSH client:
- host: `localhost`
- user: `vagrant`
- password: `vagrant`
- port: `2222` (it's usually 22)


## Python CGI References
- https://www.tutorialspoint.com/python/python_cgi_programming.htm
- https://docs.python.org/2/library/cgi.html
