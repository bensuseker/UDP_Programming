# UDP_Programming
UDP Programming assignment for Computer Networking Lecture

I had a hands-on introduction to Python socket programming for UDP throughout this 
assignment. I discovered how to use UDP sockets for datagram packet transmission and 
reception as well as how to establish the right socket timeout. The programs functionality is 
askin to what the standard ping apps found in modern operating systems can do. These 
programs communicate with one another using UDP, a less complicated protocol than the 
widely used Internet Control Message Protocol (ICMP). The ping protocol enables a client 
computer to broadcast a data packet to a remote computer, which subsequently transmits the 
data back to the client computer intact (this action is called echoing) (this action is called 
echoing). The ping protocol, among other things, permits hosts to provide round-trip times to 
other computers. Ten pings from the client should be sent to the server. A packet transmitted 
from the client to the server or vice versa may get lost in the network since UDP is an 
unstable protocol. This makes it impossible for the client to wait endlessly for a ping 
message's response. If no response is received after one second, my client software should 
presume that the packet was lost during network transmission, according to the code I 
provided. To learn how to change a datagram socket's timeout value, consult the Python 
manual.
- I use UDP to deliver the ping message.
- I print the server's response message, if any.
where time is the moment the client transmits the message, and sequence number begins at 1 
and increases by 10 for each subsequent ping message delivered by the client.

