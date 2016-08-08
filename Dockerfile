FROM centos:6

# Install Ansible
RUN yum -y install epel-release
RUN yum -y install git ansible sudo wget
RUN yum clean all

# Disable requiretty
RUN sed -i -e 's/^\(Defaults\s*requiretty\)/#--- \1/'  /etc/sudoers

VOLUME [ "/sys/fs/cgroup" ]
CMD ["/usr/sbin/init"]

# Add new user called vagrant
RUN useradd -ms /bin/bash vagrant
# USER vagrant
# WORKDIR /home/vagrant