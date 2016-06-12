#!/usr/bin/env python
#coding:utf-8
__author__ = '123'

from hosts import groups

def hosts_set():
    hosts=[]
    for group in groups:
        host_list=group.hosts
        hosts.extend(host_list)
    return set(hosts)


hostlist=hosts_set()

agent_info={}
for ip in hostlist:
    for template in groups:
        if ip in template.hosts:
            agent_info[ip]=[template.servers]
