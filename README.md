REST API Challenge
=========================

The architecture is set up in two elements:

1. Client - application that sends JSON requests
2. Server - application that receives JSON requests 

The first step is to run server.py, which handles POST requests from 
http://localhost:8080/decision. The second test is to run the client.py
which will simulate POST request and send JSON strings. The approach is
fairly simple it uses array to store the json data, first the json request
is converted into Movie() object and after that for each incoming movie it
tries to find match based on some rules. Also i have used Cosine scorer in
order to find string similarities of the tokens, this can be changed if tested
which scorer will be the most appropriate.

The needed requirements for the challenge are in the "requirements.txt"


Complexity analysis
=========================
Considering that we are using an array, searching in the array wll be
O(n), the comparisons are O(1) and the cosine simularity calculation is O(n^2),
but considering that the titles of the movies are short, it can probably perform
O(n*m).

Possible improvments: 

Alternative solutions - improvements
=========================
All depends on the data and how it changes, which
fields are availible and which are not.

1. Hash table
2. Vector space model
2. Fuzzy string matching
3. Clustering (not very memory efficent)


