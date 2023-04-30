# configuration for gw1
sysctl -w net.ipv4.ip_forward=1
iptables -t nat -A PREROUTING -p tcp --dport 80 -j DNAT --to-destination 10.0.0.55
iptables -t nat -A POSTROUTING -o gw1-eth1 -j MASQUERADE
