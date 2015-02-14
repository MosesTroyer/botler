@command("echo", man="Usage: '!echo <message>'")
def echo(nick, channel, message):
    say(channel, '{}: {}'.format(nick, message))
