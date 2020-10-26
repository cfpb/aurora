FROM centos:7

# Install Ansible
RUN yum -y install epel-release
RUN yum -y install git ansible sudo wget openssh-server
RUN yum -y install acl
RUN yum clean all

# Disable requiretty
RUN sed -i -e 's/^\(Defaults\s*requiretty\)/#--- \1/'  /etc/sudoers

VOLUME [ "/sys/fs/cgroup" ]
CMD ["/usr/sbin/init"]

# Add new user called vagrant
RUN useradd -ms /bin/bash vagrant

#Create test cert for docker
RUN openssl req -x509 -nodes -days 365 -newkey rsa:2048 -subj "/C=US/ST=CFPB/L=Washington/O=Dis/CN=www.cf.gov" -keyout /etc/pki/tls/private/localhost.key -out /etc/pki/tls/certs/localhost.crt
