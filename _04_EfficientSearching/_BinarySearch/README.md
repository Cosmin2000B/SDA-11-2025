
# Binary Search

> Main idea (given via the most abstract problem):
>> Consier the following vector:
>>  [F, F, F, .... , F, T, ... , T, T]
>>                   ^
>>                   |
>>                 found
>> And we want to obtain the most right F value (i.e. highest index that holds F).

> Divide et Impera approach
  [l, r]

while r - l >= 2:
    mid = (l + r) / 2 # in reality, to avoid overflows when adding left with right: l + (r - l) / 2
    if v[mid] == F:
        l = mid
    else:
        r = mid - 1

if v[l] == T : return -1
while l + 1 <= r && v[l + 1] == F:
  l ++
return l

Complexity: O(log(n)) | O(log(r - l))

> Step solution
>> see code. maybe add description