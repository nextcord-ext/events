nextcord-ext-events
====================

|dependencies| |license|

Custom events derived from events dispatched by Discord. 

Fork
-----
This is a maintained fork of discord-ext-events

Installation
------------

This extension is currently in PyPI.

.. code-block:: sh

    $ python3 -m pip install n-ext[events]


Usage
-----

An example for when subscribing to the on_member_kick event.

.. code-block:: py

    import nextcord
    from nextcord.ext import commands, events
    from nextcord.ext.events import member_kick


    class MyBot(commands.Bot, events.EventsMixin):

        async def on_ready(self):
            print('Logged in!')

        async def on_member_kick(self, member: nextcord.Member, entry: nextcord.AuditLogEntry):
            print(f'{member} was kicked from {member.guild}!')


    bot = MyBot(command_prefix='!', intents=nextcord.Intents.all())

    bot.run("TOKEN")

.. |dependencies| image:: https://img.shields.io/librariesio/github/nextcord-ext/events
.. |license| image:: https://img.shields.io/pypi/l/nextcord-ext-events.svg
