# A Hash 

The challenge is to find a social security number given its hash.
Since the format of a Norwegian social security is known and has relativley few possibilities, it can be brute forced.

I'll put the given hash `a979d4d0511b9dccceeee018de45c4ee` in a file `hash.txt`
The format mask (11 digits) is written as 11 `?d`s and I'm gonna assume it is md5 (it is always md5) so i run the command `hashcat -a 3 -m 0 hash.txt ?d?d?d?d?d?d?d?d?d?d?d`.

After a while, hashcat returns `a979d4d0511b9dccceeee018de45c4ee:27103926640` so the flag is `CTFkom{27103926640}`