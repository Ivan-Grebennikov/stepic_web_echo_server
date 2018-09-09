import socket
import io_common
import echo_server


if '__main__' == __name__:
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.connect((socket.gethostname(), echo_server.PORT_NUMBER))
    msg = ''

    while msg != 'close':
        msg = input('--> ').encode('utf-8')
        if len(msg) > echo_server.MESSAGE_LENGTH:
            print('ERROR', 'too long request (must be <= {0})'.format(echo_server.MESSAGE_LENGTH))
            continue
        try:
            io_common.send(server_socket, msg)
            response = io_common.receive(server_socket, echo_server.MESSAGE_LENGTH)
            print('RESPONSE-->', response.decode('utf-8'))
        except RuntimeError as err:
            print('ERROR', err)
            break
        except KeyboardInterrupt:
            break

    server_socket.close()
