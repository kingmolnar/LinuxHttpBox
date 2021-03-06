# -*- mode: ruby -*-
# vi: set ft=ruby :

# All Vagrant configuration is done below. The "2" in Vagrant.configure
# configures the configuration version (we support older styles for
# backwards compatibility). Please don't change it unless you know what
# you're doing.
Vagrant.configure("2") do |config|
  # The most common configuration options are documented and commented below.
  # For a complete reference, please see the online documentation at
  # https://docs.vagrantup.com.

  # Every Vagrant development environment requires a box. You can search for
  # boxes at https://atlas.hashicorp.com/search.
  config.vm.box = "bento/centos-7.3"

  # Disable automatic box update checking. If you disable this, then
  # boxes will only be checked for updates when the user runs
  # `vagrant box outdated`. This is not recommended.
  # config.vm.box_check_update = false

  # Create a forwarded port mapping which allows access to a specific port
  # within the machine from a port on the host machine. In the example below,
  # accessing "localhost:8080" will access port 80 on the guest machine.
  # NOTE: This will enable public access to the opened port
  config.vm.network "forwarded_port", guest: 80, host: 8080

  # Create a forwarded port mapping which allows access to a specific port
  # within the machine from a port on the host machine and only allow access
  # via 127.0.0.1 to disable public access
  # config.vm.network "forwarded_port", guest: 80, host: 8080, host_ip: "127.0.0.1"

  # Create a private network, which allows host-only access to the machine
  # using a specific IP.
  # config.vm.network "private_network", ip: "192.168.33.10"

  # Create a public network, which generally matched to bridged network.
  # Bridged networks make the machine appear as another physical device on
  # your network.
  # config.vm.network "public_network"

  # Share an additional folder to the guest VM. The first argument is
  # the path on the host to the actual folder. The second argument is
  # the path on the guest to mount the folder. And the optional third
  # argument is a set of non-required options.
  # config.vm.synced_folder "../data", "/vagrant_data"

  # Provider-specific configuration so you can fine-tune various
  # backing providers for Vagrant. These expose provider-specific options.
  # Example for VirtualBox:
  #
  # config.vm.provider "virtualbox" do |vb|
  #   # Display the VirtualBox GUI when booting the machine
  #   vb.gui = true
  #
  #   # Customize the amount of memory on the VM:
  #   vb.memory = "1024"
  # end
  #
  # View the documentation for the provider you are using for more
  # information on available options.

  # Define a Vagrant Push strategy for pushing to Atlas. Other push strategies
  # such as FTP and Heroku are also available. See the documentation at
  # https://docs.vagrantup.com/v2/push/atlas.html for more information.
  # config.push.define "atlas" do |push|
  #   push.app = "YOUR_ATLAS_USERNAME/YOUR_APPLICATION_NAME"
  # end

  # Enable provisioning with a shell script. Additional provisioners such as
  # Puppet, Chef, Ansible, Salt, and Docker are also available. Please see the
  # documentation for more information about their specific syntax and use.
  config.vm.provision "shell", run: "always", inline: <<-SHELL
    if [ ! -f /home/vagrant/.LinuxWebServer_install_completed ]; then
    	yum -y update
    	yum -y install epel-release
    	yum -y groupinstall "Development Tools"
      echo "installing Python 2"
    	yum -y install python-devel
    	yum -y install python2-pip
    	pip install --upgrade pip
    	yum -y install numpy
    	pip install pandas
    	pip install sklearn
    	pip install scipy
    	pip install sqlalchemy
    	pip install openpyxl
    	pip install xlrd
    	pip install xlutils
    	pip install pyexcel
    	pip install seaborn
    	pip install matplotlib
      echo "installing Python 3"
      yum -y install python34
      yum -y install  python34-pip
      pip3 install --upgrade pip
      pip3 install pandas
    	pip3 install sklearn
    	pip3 install scipy
    	pip3 install sqlalchemy
    	pip3 install openpyxl
    	pip3 install xlrd
    	pip3 install xlutils
    	pip3 install pyexcel
    	pip3 install seaborn
    	pip3 install matplotlib
      echo "installing HTTP server"
    	yum -y install httpd
    	mv /etc/httpd/conf/httpd.conf /etc/httpd/conf/bkup_httpd_conf
    	sed 's|/var/|/vagrant/|g' /etc/httpd/conf/bkup_httpd_conf  > /etc/httpd/conf/httpd.conf
    	if [ ! -d /vagrant/log ]; then
    		 mkdir /vagrant/log
    	fi
    	cp -a /var/log/httpd /vagrant/log/
    	rm -rf /var/log/httpd
    	ln -s /vagrant/log/httpd /var/log/
      date > /home/vagrant/.LinuxWebServer_install_completed
    else
	      echo -n "Running installation from "
	      cat /home/vagrant/.LinuxWebServer_install_completed
    fi
    systemctl enable httpd
    systemctl start httpd
  SHELL
end
