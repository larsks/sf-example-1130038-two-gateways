# Routing with two gateways

## Topology

```
                                       gw1                           client2
                              +---------------------------+   +---------------------+
                              |                           |   |                     |
                        +-----+ 10.0.0.1 (eth0)           |   |                     |
                        |     |                           |   |                     |
      server            |     |        100.0.0.100 (eth1) +---+ 100.0.0.100 (eth0)  |
+-------------------+   |     |                           |   |                     |
|                   |   |     +---------------------------+   +---------------------+
|   10.0.0.55 (eth0)+---+
|   11.0.0.55       |   |             gw2                            client2
|                   |   |     +---------------------------+   +---------------------+
+-------------------+   |     |                           |   |                     |
                        +-----+ 11.0.0.1 (eth0)           |   |                     |
                              |                           |   |                     |
                              |        101.0.0.100 (eth1) +---+ 101.0.0.100 (eth0)  |
                              |                           |   |                     |
                              +---------------------------+   +---------------------+
```

## Running tests

To bring up the environment:

```
sudo -E mn --custom topology.py --topo custom --pre setup.mn
```

Make an http request from "outside" via gw1:

```
mininet> client1 curl http://100.0.0.100
```

Make an http request from "outside" via gw2:

```
mininet> client2 curl http://101.0.0.100
```
