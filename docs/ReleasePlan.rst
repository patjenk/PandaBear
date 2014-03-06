================================
Panda Bear Database Release Plan
================================

The initial release of the Panda Bear Database is intended to be pure vapor ware. This is intentional. The project is ambitious and needs a basic framework before talented individuals devote their time to it's succcess.

Version 1.0 of Panda Bear Database has the ambitious goal of being a drop in replacement for MySQL, Memcache and Redis. The unwritten idea is that each dot release (e.e 0.1, 0.2, 0.3, etc) will get us one step closer with useable functionality. Since release 0.0 only requires detailed specs for version 0.1-0.4 that leaves a TON of room for interpretation about the back half of the project. This document is intended to be a guiding light to ensure we arrive at 1.0 successfully.

Version Functionalities
=======================

:0.1: Naive memcache functionality. This means you can connect and execute all memcache functions via the text protocol.
:0.2: Implementation of binary memcache protocol. Utilize the twisted library (or other high performance networking functionality) to handle connections
:0.3: Implement consistent hashing and hinted handoff
:0.4: Implement gossip protocol similar to Cassandra's for growing the memcache cluster.
:0.5: Implement Redis protocol and extra functionality required. 
:0.6: Add ability to read and query MySQL data files: MyISAM and InnoDB
:0.7: Add ability to write to MySQL data files: MyISAM and InnoDB
:0.8: Add ability to accept connections from a MySQL client and read and write data.
:0.9: Add ability to work as a master or slave to a MySQL 5.5 instance.
:1.0: Implement consistent hashing, hinted handoff and gossip protocol for MySQL.

Other Potential Functionalities
===============================
- Adding a persistent storage option for memcached when we add the redis functionality.
- Make Panda Bear Database computer rack and data center aware. That means that we can guard agains the failure of all nodes in a certain rack or data center and still ensure data availability.
