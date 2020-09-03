from . import nntplib, Server, Channel, database, messenger


def check_subscription_updates():
    session = database.session_maker()
    for server in session.query(Server).all():
        serv = nntplib.NNTP(server.name)
        for channel in server.channels.all():
            _, _, _, last, _ = serv.group(channel.name)
            if True or last != channel.last_article:
                channel.last_article = last
                session.add(channel)
                infos = serv.over((channel.last_article, last))[1]
                for info in infos:
                    info = info[1]
                    subject = info['subject']
                    from_ = info['from']
                    message_id = info['message-id']
                    raw_lines = serv.body(message_id)[1].lines
                    lines = [line.decode('utf-8') for line in raw_lines]
                    content = "\n".join(lines)
                    final_message = f'{subject}\n{from_}\n{content}'
                    for user in channel.users:
                        messenger.send(user.fb_id, final_message)
            else:
                print("No updates found for", server.name, channel.name)
    session.commit()
    session.close()
