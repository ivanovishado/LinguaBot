#!/usr/bin/env python
# -*- coding: utf-8 -*-

from __future__ import print_function

from rivescript import RiveScript
from rivescript_redis import RedisSessionManager
import sys
import argparse
import random

# Función principal (interfaz con línea de comandos)
if __name__ == '__main__':
    p = argparse.ArgumentParser("Pruebas con RiveScript en modo consola")
    p.add_argument("--rs", type=str, default="./rs", action="store",
                   help="RiveScript directory with rule files [./rs]")

    opts = p.parse_args()

    # The RiveScript constructor is the public interface to
    # the RiveScript interpreter.
    bot = RiveScript(session_manager=RedisSessionManager())

    # Use the 'load_directory' method to load the contents
    # of an RiveScript dir into the Kernel.
    bot.load_directory(opts.rs)
    bot.sort_replies()

    # Loop forever, reading user input from the command
    # line and printing responses.
    while True:
        print(bot.reply(str(None), input("> ")))
