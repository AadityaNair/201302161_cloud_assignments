#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
    Mininet-Assignment
    Author: Aaditya M Nair
    Created On: Wed Sep  2 20:46:08 IST 2015

    THis file defines the topology of the network
"""
import sys
from mininet.clean import Cleanup
from mininet.net import Mininet
from mininet.cli import CLI
from mininet.link import TCLink
from mininet.node import Controller

if __name__ == '__main__':
    y = int(raw_input("Enter number of switches: "))
    x = int(raw_input("Enter number of nodes per switch: "))
    
    net = Mininet( controller=Controller ,  link=TCLink)
    net.addController( 'c0' )
    
    switches = []
    count=1    

    ip1='10.0.1.'
    ip2='10.0.2.'

    for i in range(y):
        s = net.addSwitch('s'+str(i+1)) 
        for j in range(x):            
            ind=count
            if ind % 2 !=0:
                h = net.addHost( 'h'+str(count), ip=ip1+str(ind)+'/24')
                net.addLink( h, s, bw=1 )
            else:
                h = net.addHost( 'h'+str(count), ip=ip2+str(ind)+'/24')
                net.addLink( h, s , bw=2 )
            count= count+1
        switches.append(s)

    for i in range(y):
        if i < y-1:
            net.addLink(switches[i], switches[i+1], bw=2)

    net.start()
    CLI( net )
    net.stop()
    Cleanup.cleanup()
