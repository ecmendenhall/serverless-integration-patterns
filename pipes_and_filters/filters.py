# coding=utf-8

def lowercase(message):
    return message.lower()


def exclamation_points(message):
    return '{}!!!'.format(message)


def sparkles_emoji(message):
    return '✨  {} ✨ '.format(message)


def no_fun(message):
    return 'fun' not in message


def not_too_excited(message):
    return '!!!!' not in message
