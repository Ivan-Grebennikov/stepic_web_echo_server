

def send(sock, msg):
    total = 0
    while total < len(msg):
        sent = sock.send(msg[total:])
        if sent == 0:
            raise RuntimeError('connection broken')
        total += sent


def receive(sock, maxlen):
    msg = sock.recv(maxlen)
    if not msg:
        raise RuntimeError('connection broken')
    return msg


# def receive(sock, msglen):
#     msg = b''
#     while len(msg) < msglen:
#         chunk = sock.recv(msglen - len(msg))
#         if not chunk:
#             raise RuntimeError('connection broken')
#         msg += chunk
#     return msg
