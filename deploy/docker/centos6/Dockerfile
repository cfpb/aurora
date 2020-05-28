# based on https://github.com/smerrill/docker-vagrant-centos
FROM centos:centos6

RUN yum install -y sudo initscripts openssh-clients openssh-server

# https://github.com/dotcloud/docker/issues/1240#issuecomment-21807183
RUN echo "NETWORKING=yes" > /etc/sysconfig/network

# http://gaijin-nippon.blogspot.com/2013/07/audit-on-lxc-host.html
RUN sed -i -e '/pam_loginuid\.so/ d' /etc/pam.d/sshd

# Kill udev. (http://serverfault.com/a/580504/82874)
RUN echo " " > /sbin/start_udev

# No more requiretty for sudo. (Vagrant likes to run Puppet/shell via sudo.)
RUN sed -i 's/.*requiretty$/Defaults !requiretty/' /etc/sudoers

# Let this run as an unmodified Vagrant box.
RUN groupadd vagrant && \
    useradd vagrant -g vagrant -G wheel && \
    echo "vagrant:vagrant" | chpasswd && \
    echo "vagrant        ALL=(ALL)       NOPASSWD: ALL" > /etc/sudoers.d/vagrant && \
    chmod 0440 /etc/sudoers.d/vagrant

# Installing vagrant keys
RUN mkdir -pm 700 /home/vagrant/.ssh && \
    echo "ssh-rsa AAAAB3NzaC1yc2EAAAABIwAAAQEA6NF8iallvQVp22WDkTkyrtvp9eWW6A8YVr+kz4TjGYe7gHzIw+niNltGEFHzD8+v1I2YJ6oXevct1YeS0o9HZyN1Q9qgCgzUFtdOKLv6IedplqoPkcmF0aYet2PkEDo3MlTBckFXPITAMzF8dJSIFo9D8HfdOV0IAdx4O7PtixWKn5y2hMNG0zQPyUecp4pzC6kivAIhyfHilFR61RGL+GPXQ2MWZWFYbAGjyiYJnAmCP3NOTd0jMZEnDkbUvxhMmBYSdETk1rRgm+R4LOzFUGaHqHDLKLX+FIPKcF96hrucXzcWyLbIbEgE98OHlnVYCzRdK8jlqm8tehUc9c9WhQ== vagrant insecure public key" > /home/vagrant/.ssh/authorized_keys && \
    chmod 0600 /home/vagrant/.ssh/authorized_keys && \
    chown -R vagrant /home/vagrant/.ssh

# Customize the message of the day
RUN echo 'Welcome to your Vagrant-built Docker container.' > /etc/motd

RUN yum install -y acl && \
    yum clean all && \
    rm -rf /var/cache/yum

EXPOSE 22
CMD ["/sbin/init"]