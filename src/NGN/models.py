from . import declarative_base, Table, Column, Integer, String,\
              relationship, ForeignKey, Database, add_relationship, nntplib


Base = declarative_base()


user_channel_association = Table(
        'users_channels', Base.metadata,
        Column('user_id', Integer, ForeignKey('users.id')),
        Column('channel_id', Integer, ForeignKey('channels.id'))
    )


class Channel(Base):
    """ Channel class """
    __tablename__ = 'channels'
    id = Column(Integer, primary_key=True)
    name = Column(String)
    last_article = Column(Integer)
    # USER (Many to Many)
    users = relationship('User', secondary=user_channel_association,
                         lazy='dynamic')
    # SERVER (Channel - Many to One - Server)
    server_id = Column(Integer, ForeignKey('servers.id'))
    server = relationship('Server', uselist=False, back_populates='channels')

    def __init__(self, name, server):
        self.name = name
        self.server = server
        server = nntplib.NNTP(server.name)
        _, _, _, self.last_article, _ = server.group(name)
        server.quit()

class Server(Base):
    """ Server class """
    __tablename__ = 'servers'
    id = Column(Integer, primary_key=True)
    name = Column(String)
    channels = relationship('Channel', back_populates='server', lazy='dynamic')

    def __init__(self, name):
        self.name = name


database = Database({'sqlalchemy.url': 'sqlite:///foo.db'}, base=Base)
user_rs = relationship('Channel', secondary=user_channel_association,
                       lazy='dynamic')
add_relationship(database.user_class, 'channels', user_rs)

session = database.session_maker()
