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

Todo For This Spec
==================
- Define consistent hashing and hinted handoff so any developer can implment.
