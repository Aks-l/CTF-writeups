# Seqences1

 We are given [a partial encryption script](enc.py), and [the output it creates](output.txt). We have to find the original secret_word, by finding the secret_number_sequence function. 
The output encrypted_secret is made by multiplying the unicode value of the flag by the corresponding number of the secret function. 
Since the flag format (the first 7 characters) are known, we can find the first outputs of the function by dividing the output by the characters.

```python
known = "CTFkom{"
given = [67,84,140,321,555,872,1599]
for i in range(len(known)):
    print(int(given[i]/ord(known[i])), end=' ')
```

```1 1 2 3 5 8 13```

This shows that the function gives a familiar sequence of numbers, Fibonacci.
Now let’s replace the known values with the Fibonacci sequence, and the flag should be revealed.

```python
def fib(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    a, b = 1, 1
    for _ in range(n - 2):
        a, b = b, a + b
    return b

given = [67, 84, 140, 321, 555, 872, 1599, 2142, 1666, 5390, 4272, 15840, 
         12116, 37323, 60390, 48363, 151715, 136952, 213231, 764445, 1280682, 
         903261, 3152270, 4590432, 3826275, 11532335, 19445382, 15254928, 
         51422900, 42434040, 44426877, 139411776, 440572250]

for i, val in enumerate(given):
    fibValue = fib(i + 1)
    print(chr(val // fibValue), end="")
```
and the flag is
`CTFkom{f1b0n4cc1_53qu3nc3_c0d3!@}`