'''
Generate a url to JiLin University VPN
'''
import urllib.parse, os
import sys
key = [0x6f, 0x68, 0xde, 0x3, 0xb8, 0xaf, 0xf7, 0xcf, 0xe1, 0x97, 0x16, 0x33, 0x7, 0xca, 0xbc, 0xaa, 0xc6]
meaningless_bullshit = '77726476706e69737468656265737421'
for z in range(255):
    for o in range(255):
        origin = 'http://10.0.' + str(z) +'.'+ str(o)
        info = urllib.parse.urlparse(origin)
        host = info.hostname
        print('Original Host Name : %s' % host)
        tmp = []
        for i in range(len(host)):
            tmp.append(hex(ord(host[i]) ^ 0xff ^ key[i])[2:])
        for index, t in enumerate(tmp):
            if len(t) < 2:
                tmp[index] = '0' + t
        text = ''.join(tmp)
#        full = 'https://ip/' + info.scheme + '/' + meaningless_bullshit + text + info.path
        full = ''+info.scheme +'/'+ meaningless_bullshit + text + info.path
        if info.params:
            full += '?' + info.params
        if info.query:
            full += '?' + info.query
        if info.fragment:
            full += '#' + info.fragment
        with open('ip.txt',mode='a') as f:
            f.writelines(full+'\n')



