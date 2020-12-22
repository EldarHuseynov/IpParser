import os
import re

newFile = os.system('ip addr show > ipparser.txt')
s = """
1: lo: <LOOPBACK,UP,LOWER_UP> mtu 65536 qdisc noqueue state UNKNOWN group default qlen 1000
    link/loopback 00:00:00:00:00:00 brd 00:00:00:00:00:00
        inet 127.0.0.1/8 scope host lo
               valid_lft forever preferred_lft forever
                   inet6 ::1/128 scope host 
                          valid_lft forever preferred_lft forever
                          2: enp3s0f0: <BROADCAST,MULTICAST,UP,LOWER_UP> mtu 1500 qdisc mq state UP group default qlen 1000
                              link/ether 08:9e:01:f2:c6:ea brd ff:ff:ff:ff:ff:ff
                                  inet 192.168.0.102/24 brd 192.168.0.255 scope global dynamic noprefixroute enp3s0f0
                                         valid_lft 4897sec preferred_lft 4897sec
                                             inet6 fe80::39f0:e985:5e1a:db71/64 scope link noprefixroute 
                                                    valid_lft forever preferred_lft forever
                                                    3: wlp4s0: <NO-CARRIER,BROADCAST,MULTICAST,UP,LOWER_UP> mtu 1500 qdisc fq_codel state DORMANT group default qlen 1000
                                                        link/ether 08:3e:8e:eb:8a:3f brd ff:ff:ff:ff:ff:ff
                                                        """
result = re.search('\d: (.*):', s)
"result2 = re.search('inet', result)"
print(result.group(1))
"print(result2.group(1))"
