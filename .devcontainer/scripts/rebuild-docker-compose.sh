#!/bin/bash
export WORKSPACE=${WORKSPACE:-/workspace}

#inventory="$(cat $WORKSPACE/.devcontainer/scripts/tmp_inventory.csv | grep ssh_host | sed 's/ ansible_ssh_host=/,/' | sed 's/ .*$//')"
inventory="$(cat $WORKSPACE/.devcontainer/scripts/tmp_inventory.csv | grep -v '^#' | sed 's/ ansible_ssh_host=/,/' | sed 's/ .*$//')"
tmp_file="$WORKSPACE/.devcontainer/tmp_docker_compose.yml"

IFS=$'\n'
#echo $inventory
cat $WORKSPACE/.devcontainer/docker-compose-base.yml >$tmp_file
hosttemplate="$WORKSPACE/.devcontainer/docker-compose-host-template.yml"
networks="$WORKSPACE/.devcontainer/docker-compose-networks.yml"
while IFS= read -r line; do
    echo "... $line ..."
    IFS=', ' read -r -a array <<< "$line"

    hostname="${array[0]}"
    ipv4="${array[1]}"
    #appending network to bottom
    cat $hosttemplate | sed "s/HOSTNAME/$hostname/"|sed "s/IPV4/$ipv4/">>$tmp_file
done <<< "$inventory"

#appending network to bottom
cat $networks >>$tmp_file
cat $tmp_file >$WORKSPACE/.devcontainer/docker-compose.yml
