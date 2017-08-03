#!/usr/bin/env python
# -*- coding: utf-8 -*-

from flask import Flask, request
import fbmq
from config import CONFIG

app = Flask(__name__)

page = fbmq.Page(CONFIG['FACEBOOK_TOKEN'])

page.show_starting_button("START_PAYLOAD")


@page.callback(['START_PAYLOAD'])
def start_callback(payload, event):
    page.send(sender_id, 'Comencemos, ¡%s!' % page.get_user_profile(event.sender_id)['first_name'])


@app.route('/', methods=['POST'])
def webhook():
    page.handle_webhook(request.get_data(as_text=True))
    return "ok"


@page.handle_message
def message_handler(event):
    """:type event: fbmq.Event"""
    sender_id = event.sender_id
    message = event.message_text

    page.send(sender_id, "thank you! your message is '%s'" % message)


@page.after_send
def after_send(payload, response):
    """:type payload: fbmq.Payload"""
    print("complete")


if __name__ == '__main__':
    app.run(host='127.0.0.1',
            port='5000')
