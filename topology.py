from mininet.topo import Topo

class Custom(Topo):
    def build(self):
        sw_int = self.addSwitch('sw_int', dpid='100')

        gw1 = self.addHost('gw1', ip='10.0.0.1/24')
        gw2 = self.addHost('gw2', ip='11.0.0.1/24')
        server = self.addHost('server', ip='10.0.0.55/24')

        self.addLink(server, sw_int)
        self.addLink(gw1, sw_int)
        self.addLink(gw2, sw_int)

        sw_ext_1 = self.addSwitch('sw_ext_1', dpid='101')
        sw_ext_2 = self.addSwitch('sw_ext_2', dpid='102')

        self.addLink(gw1, sw_ext_1, params1={'ip': '100.0.0.100/24'})
        self.addLink(gw2, sw_ext_2, params1={'ip': '101.0.0.100/24'})

        client1 = self.addHost('client1', ip='100.0.0.10/24')
        client2 = self.addHost('client2', ip='101.0.0.10/24')
        self.addLink(client1, sw_ext_1)
        self.addLink(client2, sw_ext_2)

topos = {"custom": Custom}
