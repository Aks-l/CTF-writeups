# Inga

### Inga 1
Since this is a series of 4 beginner level challenges, I'll start as simple as it gets, by searching for the flag with CTRL+F in the page source.
It is written as a comment on line 1650:
`CTFkom{39f5058e98abf020f706395d99455ffc}`

### Inga 2
`robots.txt` is also a common place for ctf-challenges (hinted towards with the hint being "🤖"), lets check that out.
It says `User-agent: * Disallow: /ba570ef4688dd5f1010a9d6cd4cf2ab7`
The `/ba570ef4688dd5f1010a9d6cd4cf2ab7` endpoint has the flag:
`CTFkom{8930daa1a2a471f15a10c9024aaa3c8a}`

### Inga 3
This time, `robots.txt` says `User-agent: * Disallow: /admin`
`/admin` says `You are not admin!`
There is a cookie named `admin` set to `false`. If i reload the page after setting it to `true`, the flag appears:
`CTFkom{7e0b09ce06c965784865c4e1dc3ec9a5}`

### Inga 4
This time, `robots.txt` says `User-agent: * Disallow: /flag`
`/flag` says `Method not allowed`
Using the `OPTIONS` mehod shows that the only allowed method is `FLAG`
When sending a [FLAG-request to /flag](https://media1.giphy.com/media/v1.Y2lkPTc5MGI3NjExc2hvcnAxdTdleHZjN3Q3amRieGVmMWx5Z3Fjc25zbTNwcmZ0bWtrZCZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/1X7lCRp8iE0yrdZvwd/giphy.gif) (Using Postman for simplicity), i get the flag:
`CTFkom{916b8d6c45354aa3a26a93c332456ad2}`