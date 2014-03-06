===============================
Panda Bear Database Release 0.3
===============================

Mission
=======

Turn individual Panda Bear Memcache servers into a ring and implement consitent hashing and hinted handoff.

Motivation
==========

:Dynamo: http://s3.amazonaws.com/AllThingsDistributed/sosp/amazon-dynamo-sosp2007.pdf
:Pynamo: http://lurklurk.org/pynamo/pynamo.html

Future Considerations
=====================

The next release adds a gossip protocol to maintain the cluster itself. Maintaing the cluster in this release can happen via explicit configuration.

Functional Requirements
=======================

- Establish the idea of a "ring" in the Panda Bear Memcached implementation.
- Add consistent hashing to the memcached ring.
- Add hinted handoff to the memcached ring.
- The finished application should have the following command line switches:
  :memory_size: The amount of memory in megabytes the server is able to store. The default is 100.
  :incoming_ip: A cidr representation of ip addresses that are allowed to connect.
  :port: The port the server should listen.
  :ip: The IP the server should listen.
  :buckets: The number of buckets to implement in consistent hashing. The default is ten million.
  :ringnode: The ip address or network location of a node in the memcached ring.
  :redudancy: The default number of copies to store of each data entry. The default is 1.


Machine Ring
============

The machine ring is the set of nodes that make up the storage space of the memcached cluster. In our implementation every node will produce the same results as every other node for every write and read. This will be accomplished by every node working as both a storer or data and a coordinator of requests. This seamless infrastructure will utilize consistent hashing and hinted handoff to ensure success.


Consistent Hashing
==================

Consistent hashing is a technique to map objects in a ring to virtual buckets randomly distributed about a set of nodes. The randomness does not have to be perfect (e.g. it can be psuedo-random). 

Consistent hashing in Panda Bear needs to be abstrated into some reusable component. This does not necessarily have to be accomplished 100% at this release but we would like to reuse this feature in future releases that implement Redis and MySQL.

In Panda Bear, we will have an adjustable ring size that is abstracted from the hardware layer. We will use virtual nodes that map hundreds of thousands or even millions of address spaces onto machines. The advantages of this approach are described in Amazon's Dynamo paper.

We will also have a redudancy parameter that specifies how many copies of our data we want to keep in the ring. Each redudancy level requires a doubling of virtual nodes used. It is important to distribute the second ring of virtual nodes differently than the first (assuming the number of physical nodes is greater than 1). 

This release of Panda Bear will have minimal ring management and no healing functionality. The addresses of physical hardware will be specified when each node is started. Nodes will keep a list of other nodes and periodically update their health status. However, we will not rebalance the ring when a node becomes unavailable. We will begin to implement a hinted handoff protocol to implement this functionality.

Since consistent hashing spreads the data evenly across the ring it is impossible for a client to consistently find the correct node. This means that every node in the ring has the responsibility of fulfilling all requests by contacting the appropriate sibling node and returning the correct value.


Hinted Handoff
==============

Hinted handoff provides some resiliancy against temporary network outages. If a node acting as a coordinator is unable to store information in a different node the information will be stored temporarily in the coordinator node and written back later.

Motivation
----------

:Apache Cassandra: http://wiki.apache.org/cassandra/HintedHandoff

Todo For This Spec
==================

- Improve the definition for node functionality. Particular coordinator and storer nodes.
