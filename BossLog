import asyncio
from telethon.tl.types import Message
from telethon import functions
from .. import loader, utils

#meta developer: @mineevor

@loader.tds
class BossLog(loader.Module):
    """Модуль на логирование боссов которых вы били, отправляются они в избранные"""
    strings={
        "name": "BossLog"
    }
    
    def __init__(self):
        self.config = loader.ModuleConfig(
                loader.ConfigValue(
                    "status",
                    False,
                    lambda: "НЕ ТРОГАТЬ!!",
                    validator=loader.validators.Boolean()
                )
            )
    
    @loader.watcher(chat_id=5522271758)
    async def main(self, message):
        if self.config["status"]:
            if "побежден игроком" in message.raw_text:
                sms = message.raw_text
                await self.client.send_message('me', sms)
                
    @loader.command()
    async def blog(self, message):
        """Вкл/Выкл"""
        self.config["status"] = not self.config["status"]
        if self.config["status"]:
            await utils.answer(message, "Модуль включен")
        else:
            await utils.answer(message, "Модуль выключен")
