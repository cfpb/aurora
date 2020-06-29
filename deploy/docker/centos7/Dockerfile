# https://hub.docker.com/r/centos/systemd/dockerfile
FROM centos/systemd

# Create vagrant user 
RUN useradd vagrant && \
    usermod -a -G wheel vagrant && \
    echo "vagrant" | passwd --stdin vagrant

RUN cd ~vagrant && \
    mkdir .ssh && \
    echo "ssh-rsa AAAAB3NzaC1yc2EAAAABIwAAAQEA6NF8iallvQVp22WDkTkyrtvp9eWW6A8YVr+kz4TjGYe7gHzIw+niNltGEFHzD8+v1I2YJ6oXevct1YeS0o9HZyN1Q9qgCgzUFtdOKLv6IedplqoPkcmF0aYet2PkEDo3MlTBckFXPITAMzF8dJSIFo9D8HfdOV0IAdx4O7PtixWKn5y2hMNG0zQPyUecp4pzC6kivAIhyfHilFR61RGL+GPXQ2MWZWFYbAGjyiYJnAmCP3NOTd0jMZEnDkbUvxhMmBYSdETk1rRgm+R4LOzFUGaHqHDLKLX+FIPKcF96hrucXzcWyLbIbEgE98OHlnVYCzRdK8jlqm8tehUc9c9WhQ== vagrant insecure public key" > .ssh/authorized_keys && \
    chown -R vagrant:vagrant .ssh && \
    chmod 0700 .ssh && \
    chmod 0600 .ssh/authorized_keys && \
    mkdir -p /etc/sudoers.d && \
    echo "vagrant ALL=(ALL) NOPASSWD: ALL" > /etc/sudoers.d/vagrant_user

RUN yum -y install sudo openssh-server openssh-clients initscripts && \
    systemctl enable sshd.service

RUN rm /usr/lib/tmpfiles.d/systemd-nologin.conf
RUN yum clean all && rm -rf /var/cache/yum

EXPOSE 22

CMD ["/usr/sbin/init"]

#docker run --privileged --name sshserver -v /sys/fs/cgroup:/sys/fs/cgroup:ro   -d  centos7-sshd
#docker build -f Dockerfile-base --rm --no-cache -t centos7-sshd .