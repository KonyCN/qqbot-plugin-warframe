# -*- coding: utf-8 -*-

import wfstate as wf

def onQQMessage(bot, contact, member, content):
    if bot.isMe(contact, member):
        return
    if content == '警报':
        bot.SendTo(contact, wf.get_alerts())