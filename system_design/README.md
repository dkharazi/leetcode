trade-offs:
* performance vs scalability
* latency vs throughput
* availability vs consistency

- how do i know if i have a performance issue?
if your system is slow for a single user.

- how do i know if i have a scalability issue?
if your system is fast for a single user, but slow under heavy load.

strive for maximal throughput with acceptable latency.

in a centralized system (e.g. rdbms)
we dont have network partitions, P.
so we get:
* availability
* consistency

in a distributed system, we will have network partitions, P.
thus we get:
* availability
* consistency

basicially available  
soft state  
eventually consistent

availability patterns
* fail-over
* replication
    - master-slave
    - tree replication
    - master-master
    - buddy replication

slave: read  
master: read/write

scaling reads to a rdbms is hard;  
scaling writes to a rdbms is impossible.

nosql
* key-value databases
* column databases
* document databases
* graph databases
* datastructure databases

write-through:  
1. write to cache
2. store in db
3. return to user

write-behind:  
1. write to cache  
2. add event to queue  
3. return to user  
4. asynchronously select and execute event  

messaging:  
* publish-subscribe
    - sender --> topic --> receivers
* point-to-point
    - sender --> queue --> receiver
* store-forward
 ```
     sender --> mediator --> receiver
                          --> storage```
* request-reply

loadblancing
* dns round robin
* reverse proxies
    - apache mod_proxy
    - haproxy
    - squid
    - nginx
* hardware lb

system error - resources not available  
==> verify resource availability before starting expensive task  
application error - bad user input  
==>  input validation immediately

always put logs on separate disk.
