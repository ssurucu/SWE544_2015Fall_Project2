# SWE544_2015Fall_Project2
This repository is created for the Project2 assigned in the class SWE544-2015Fall to Sinan Can SÜRÜCÜ

Commits to this project will be detailed in the Commit List, and will be updated within each commit.

Commit List

1) Commit:dbab848 04/01/2016 - Repository has been created and first commit has been tried with a readme file.

2) Commit:9238c10 04/01/2016 - Requirements and Design document has been added to the repository.

3) Commit:a05b709 08/01/2016 - Server - Client basic functions and protocol interfaces are defined

4) Commit:fdce351 08/01/2016 - UI design completed and related files are added to the repo

5) Commit:0f04003 11/01/2016 - Server side Ticket and User classes are defined, when a client connects Server creates a ticket for the user with random number between 1-99

6) Commit:c60aa36 11/01/2016 - Server is picking up number from the numbers list and returns it. Client side command is available now, for testing protocol rules

7) Commit:68f350a 12/01/2016 - Broadcast message in server has been defined. Server-multiple client messaging added

8) Commit:6805e9c 12/01/2016 - Server side now has two threads for incoming-outgoing messages.

9) Commit:05c0bdf 12/01/2016 - Client side now has two threads for incoming-outgoing messages.

10) Commit:66a2ffa 12/01/2016 - Client side now has two threads for incoming-outgoing messages. (FIX: Wrong file commit)

11) Commit:13b1bd1 12/01/2016 - Picked number on the server now broadcast to all clients, client can check for Cinko (dummy service). Client-Server messaging is succesfully implemented. Broadcast and message sendin to a selected client is completed. Server side has been redesigned, it now creates a new thread for every client connection.

12) Commit:6d79da0 12/01/2016 - Server side generates the tickets and assigns it to the clients, and clients shows the tickets to the user

13) Commit:3c7bc03 12/01/2016 - UI fixes has been made. User can se the picked number with different background color, so the numbers that are picked before can be seen on the left side of the UI. USer also can sign/select number on his/her ticket

14) Commit:413bd9e 12/01/2016 - Cinko validation is added, user is banned after 3 invalid cinko requests

15) Commit:        12/01/2016 - Game winning condition and announcement has been added. Players can see each other's cinko status dynamically