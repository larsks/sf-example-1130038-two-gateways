ip addr add 11.0.0.55/24 dev server-eth0

ip route add default via 10.0.0.1
ip route add default via 10.0.0.1 table 101
ip route add default via 11.0.0.1 table 102
ip rule add from 10.0.0.0/24 table 101
ip rule add from 11.0.0.0/24 table 102
