#!/usr/bin/python3
# -- coding: utf-8 --
import sys
import docker
print(sys.version)

client = docker.from_env()
print(client)

client.containers.run('alpine', 'echo hello world')

# client.swarm.get_unlock_key()