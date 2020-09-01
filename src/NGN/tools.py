from . import nntplib

def is_ntp_addres_valid(server_name):
    try:
        nntplib.NNTP(server_name)
    except Exception:
        return False
    return True


def is_ntp_channel_valid(server_address, channel_name):
    try:
        server = nntplib.NNTP(server_address)
        server.group(channel_name)
    except Exception:
        return False
    return True
