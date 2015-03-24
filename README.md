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
which scorer will be the most appropriate. The cosine scorers finds string
similarities in the "title" and "description" fields.

The needed requirements for the challenge are in the "requirements.txt"


Complexity analysis
=========================
Considering that we are using an array, searching in the array wll be
O(n), the comparisons are O(1) and the cosine simularity calculation is O(n^2),
but considering that the titles of the movies are short, it can probably perform
O(n*m).

Possible improvements: well depends on the data, if we assume that the title is not
changing and we have imdb_id we can have a hash table (hash map). The scorer without
doubt can be better, but that requires more testing. We can probably use some kind of
search algorithm, but that depends on which fields, because if we have more variations
in the data, more memory will be required.

Alternative solutions - improvements
=========================
All depends on the data and how it changes, which fields are availible and which are not.
Better web framework, better data validation, better scorer for fuzzy string matching, maybe
use clustering, but that is not very memory efficent and you also have undefined centroids.
Have some kind of indexing, we can also use the architecture of the current systems are 
working like use sharding in order to split the index. Instead of raising an exception for
406 status, i could add it to the dictionary..


