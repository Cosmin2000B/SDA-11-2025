
# Ternary Search
  <p>  Given a continious function with either one gloval max or global min
we want to find it knowing it can be found in [l, r].</p>
    ^ f(x)         
    |       /\ <---- global max   \          /
    |      /  \                    \        /
    |     /    \                    \      /
    |    /      \                    \    /
    |   /        \                    \  /
    |  /          \                    \/ <----- global min
    O --------------------------------------------------------------> x
      [                 ]        [                        ]
      l                 r        l                        r
            |      |                     |         |
            |      |                     |         |
      (2l + r)/3  (l + 2r)/3            idem       idem

> Split the interval in three and get rid of the chunk where the anwers is not present
>> compare f((2l + r) / 3) with f((l + 2r) / 3)
>>                          < skip left chunk
>>                          > skip right chunk 
(...) 1:15:47