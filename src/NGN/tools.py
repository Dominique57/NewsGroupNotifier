from . import nntplib, Server, Channel, database

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


def add_subscription(server_address, channel_name, user):
    session = database.session
    serv = session.query(Server).filter(Server.name == server_address).scalar()

    if serv is None:
        serv = Server(server_address)
        session.add(serv)

    chan = serv.channels.filter(Channel.name == channel_name).scalar()
    if chan is None:
        chan = Channel(channel_name, serv)
        session.add(chan)

    if user.channels.filter(database.user_class.id == user.id).scalar() is None:
        chan.users.append(user)

    session.commit()
