import asyncio
from asyncio import sleep
from telethon.tl.types import Message
from telethon import functions
from .. import loader, utils
from telethon.tl.types import ChatAdminRights
from ..inline.types import InlineCall

# meta developer: @mineevor
__version__ = (1,2,0)

@loader.tds
class AutoThx(loader.Module):
    """Модуль на автоматическое написание Thx"""
    strings = {
        "name": "AutoThx"
    }

    async def client_ready(self):
        self._backup_channel, _ = await utils.asset_channel(
            self.client,
            "AutoThx Group",
            "Группа для модуля AutoThx",
            silent=True,
            archive=True)
        await self.client(functions.channels.InviteToChannelRequest(self._backup_channel, ['@mine_evo_bot']))
        await self.client(functions.channels.EditAdminRequest(
                channel=self._backup_channel,
                user_id="@mine_evo_bot",
                admin_rights=ChatAdminRights(ban_users=True, post_messages=True, edit_messages=True),
                rank="AutoThx",))
        if self.db.get(self.name, "autothxstatus") == None:
            self.db.set(self.name, "autothxstatus", False)


    @loader.command()
    async def athx(self, message):
        """Включение/ выключение"""
        if self.db.get(self.name, "autothxstatus"):
            self.db.set(self.name, "autothxstatus", False)
        else:
            self.db.set(self.name, "autothxstatus", True)
        status = (
            "AutoThx включен!"
            if self.db.get(self.name, "autothxstatus")
            else "AutoThx выключен!"
        )
        await utils.answer(message, "<emoji document_id=5314346928660554905>⚠️</emoji> <b>{}</b>".format(status))


    @loader.watcher(only_message=True, chat_id=1565066632)
    async def watcher(self, message):
        statusa = self.db.get(self.name, "autothxstatus")
        if statusa:
            if "(Используй команду Thx чтобы поблагодарить и получить бонус)" in message.raw_text:
                await self.client.send_message(self._backup_channel, "Thx")
