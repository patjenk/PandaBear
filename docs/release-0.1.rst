===============================
Panda Bear Database Release 0.1
===============================

Mission
=======
Create a basic memcache implementation to build upon for future releases.

Future Considerations
=====================
- Creating tests at this stage is very important. If we have tests for all features of the memcache functionality then we can accelerate our development in future releases.

Functional Requirements
=======================
In bullet form for now...

- The finished application needs to accept more than one connection at any one time. This is so we can use it in an actual production environemnt.
- The finished application should correctly implement the memcached text protocol defined here: https://github.com/memcached/memcached/blob/master/doc/protocol.txt
- The finished application should have tests that verify the functionality of all requests types in the memcached text protocol.
- The finished application should have the ability to white list servers which are allowed to connect.
- The finished application should have command line switches for the following options:
  :memory_size: The amount of memory in megabytes the server is able to store. The default is 100.
  :incoming_ip: A cidr representation of ip addresses that are allowed to connect.
  :port: The port the server should listen.
  :ip: The IP the server should listen.
- Determine the connection library to utilize in release 0.2. The frontrunner is twisted.
- There should be a seperate performance project created to spin up and measure the effectiveness of scenarios in the AWS cluster.
- The website should be updated to provide a quick start guide for people interested in using Panda Bear.
- The website should begin to maintain technical documentation about the implementation specifics and release notes by version and by language.
