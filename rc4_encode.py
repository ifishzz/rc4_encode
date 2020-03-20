class RC4:
    def __init__(self, k):
        self.Sbox = self.RC4_init(k)

    def RC4_init(self, k):
        Sbox = [] * 255
        T = [] * 256
        for i in range(256):
            Sbox.append(i)
            T.append(ord(k[i % len(k)]))
        j = 0
        for i in range(256):
            j = (j + Sbox[i] + T[i]) % 256
            Sbox[i], Sbox[j] = Sbox[j], Sbox[i]
        return Sbox

    def RC4_crypt(self, m):
        c = ''
        i = j = 0
        S = self.Sbox
        for n in range(len(m)):
            i = (i + 1) % 256
            j = (j + S[i]) % 256
            S[i], S[j] = S[j], S[i]
            t = (S[i] + S[j]) % 256
            c += '%02x' % (ord(m[n]) ^ S[t])
        return c


k = raw_input('key:')
m = raw_input('msg:')
y = raw_input('encode or decode:')

if 'encode' in y:

    c = RC4(k).RC4_crypt(m)
    print c
else:

    c = RC4(k).RC4_crypt(m.decode('hex'))
    print(type(c))
    shellcode=c.decode('hex')

    print(shellcode)