===============================
Panda Bear Database Release 0.2
===============================

Mission
=======
Improve upon the work of release 0.1 by focusing on adding the best python technologies and ensuring feature parity with c-based memcached.

Future Considerations
=====================
- Code structure at this stage is very important. When we begin to add fancy features in future releases it will be important that we only have to touch small areas. Specifically, the way we store data should be as abstracted as possible.

Functional Requirements
=======================
In bullet form for now...

- The finished application should be able to accept hundreds of thousands of concurrent connections and utilize an established python library to do so.
- The finished application should correct implement the memcached binary protocol defined here: https://code.google.com/p/memcached/wiki/MemcacheBinaryProtocol
- Update the website documentation for version 2.0 in english.
