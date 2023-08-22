import asyncio
from asyncio import sleep
from telethon.tl.types import Message
from telethon import functions
from .. import loader, utils
from telethon.tl.types import ChatAdminRights
from ..inline.types import InlineCall
import re

#meta developer: @modEvoLife
__version__ = (1,0,0)

@loader.tds
class Autoevo(loader.Module):
    '''Модуль на автокопание и т.д'''
    strings={"name": "AutoEvo"}
    
    async def client_ready(self):
        self._backup_channel, _ = await utils.asset_channel(
            self.client,
            "AutoEvo",
            "Группа для модуля AutoEvo",
            silent=True,
            archive=True)
        await self.client(functions.channels.InviteToChannelRequest(self._backup_channel, ['@mine_evo_bot']))
        await self.client(functions.channels.EditAdminRequest(
                channel=self._backup_channel,
                user_id="@mine_evo_bot",
                admin_rights=ChatAdminRights(ban_users=True, post_messages=True, edit_messages=True),
                rank="EvoBot",))
        if self.get("aestatus") == None:
            self.set("aestatus", False)
        if self.get("aestatusmine") == None:
            self.set("aestatusmine", False)
        if self.get("aestatusthx") == None:
            self.set("aestatusthx", False)
        if self.get("aestatuseb") == None:
            self.set("aestatuseb", False)
        if self.get("clicks") == None:
            self.set("clicks", 0)
        if self.get("kts") == None:
            self.set("kts", 0)
        if self.get("rkts") == None:
            self.set("rkts", 0)
        if self.get("ks") == None:
            self.set("ks", 0)
        if self.get("rks") == None:
            self.set("rks", 0)
        if self.get("mifs") == None:
            self.set("mifs", 0)
        if self.get("krs") == None:
            self.set("krs", 0)
        if self.get("zvs") == None:
            self.set("zvs", 0)
        if self.get("allks") == None:
            self.set("allks", 0)
        if self.get("pls") == None:
            self.set("pls", 0)
        if self.get("busts") == None:
            self.set("busts", 0)
        if self.get("plthx") == None:
            self.set("plthx", 0)
        if self.get("pleb") == None:
            self.set("pleb", 0)
        if self.get("keb") == None:
            self.set("keb", 0)
        if self.get("rkeb") == None:
            self.set("rkeb", 0)
        if self.get("mefeb") == None:
            self.set("mefeb", 0)
        if self.get("kreb") == None:
            self.set("kreb", 0)
        await self.client.send_message(5522271758, "еб")
        intervalmine=self.config["intervalmine"]
        if self.get("aestatus"):
            if self.get("aestatusmine"):
                while self.get("aestatusmine")==True and self.get("aestatus")==True:
                    await self.client.send_message("@mine_evo_bot", "коп")
                    await asyncio.sleep(intervalmine)
        async with self.client.conversation(self._backup_channel) as conv:
            while self.get('aestatuseb'):
                await conv.send_message("еб")
                try:
                    res = conv.get_response()
                except asyncio.exceptions.TimeoutError:
                    
                    await conv.send_message("еб")
                else:
                    break
                await asyncio.sleep(1800)
                conv.cancel()
                
    def __init__(self):
        self.config = loader.ModuleConfig(
                loader.ConfigValue(
                    "intervalmine",
                    2.0,
                    lambda: "Интервал копания",
                    validator=loader.validators.Float()
                )
            )
        
    @loader.command()
    async def autoevo(self, message):
        '''Управление модулем'''
        aestatus=self.get("aestatus")
        aestatusmine=self.get("aestatusmine")
        aestatusthx=self.get("aestatusthx")
        aestatuseb=self.get("aestatuseb")
        await self.inline.form(
                text=f"🎮 <b>Управление модулем</b> <b>AutoEvo</b>\n\n▫️<b>Статус:</b> {aestatus}\n▫️<b>Статус копания:</b> {aestatusmine}\n▫️<b>Статус Thx:</b> {aestatusthx}\n▫️<b>Статус еб:</b> {aestatuseb}\n\n🛑 После включения/Выключения модуля, перезагрузите или переустановите его 🛑",
                message=message,
                reply_markup=[
                        [
                            {
                                "text": "Вкл/Выкл",
                                "callback": self.inline_but_one,
                            },
                            {
                                "text": "Настройки",
                                "callback": self.settings,
                            }
                        ],
                        [
                            {
                                "text": "Статистика",
                                "callback": self.abobanatr,
                            }
                        ]
                    ]
            )
            
    async def inline_but_one(self, call: InlineCall):
        status = not self.get("aestatus")
        self.set("aestatus", status)
        status = self.get("aestatus")
        await call.answer(f"AutoEvo {status}")
        if self.get("aestatus"):
            status = "Включен"
        else:
            status = "Выключен"
        aestatus=self.get("aestatus")
        aestatusmine=self.get("aestatusmine")
        aestatusthx=self.get("aestatusthx")
        aestatuseb=self.get("aestatuseb")
        await call.edit(
                text=f"🎮 <b>Управление модулем</b> <b>AutoEvo</b>\n\n▫️<b>Статус:</b> {aestatus}\n▫️<b>Статус копания:</b> {aestatusmine}\n▫️<b>Статус Thx:</b> {aestatusthx}\n▫️<b>Статус еб:</b> {aestatuseb}\n\n🛑 После включения/Выключения модуля, перезагрузите или переустановите его 🛑",
                reply_markup=[
                        [
                            {
                                "text": "Вкл/Выкл",
                                "callback": self.inline_but_one,
                            },
                            {
                                "text": "Настройки",
                                "callback": self.settings,
                            }
                        ],
                        [
                            {
                                "text": "Статистика",
                                "callback": self.abobanatr,
                            }
                        ]
                    ]
            )
            
    async def settings(self, call: InlineCall):
        if self.get("aestatus"):
            status = "Включен"
        else:
            status = "Выключен"
        aestatus=self.get("aestatus")
        aestatusmine=self.get("aestatusmine")
        aestatusthx=self.get("aestatusthx")
        aestatuseb=self.get("aestatuseb")
        await call.edit(
                text=f"🎮 <b>Настройки модуля</b> <b>AutoEvo</b>\n\n▫️<b>Статус копания:</b> {aestatusmine}\n▫️<b>Статус Thx:</b> {aestatusthx}\n▫️<b>Статус еб:</b> {aestatuseb}\n\n🛑 После включения/Выключения модуля, перезагрузите или переустановите его 🛑",
                reply_markup=[
                    [
                            {
                                "text": "Вкл/Выкл автокопание",
                                "callback": self.amine,
                            }
                        ],
                    [
                            {
                                "text": "Вкл/Выкл автоthx",
                                "callback": self.athx,
                            }
                        ],
                    [
                            {
                                "text": "Вкл/Выкл автоеб",
                                "callback": self.aeb,
                            }
                        ],
                    [
                            {
                                "text": "Назад",
                                "callback": self.autoevob,
                            }
                        ]
                    ]

            )
            
    async def amine(self, call: InlineCall):
        aestatusmine=not self.get("aestatusmine")
        self.set("aestatusmine", aestatusmine)
        aestatus=self.get("aestatus")
        aestatusmine=self.get("aestatusmine")
        aestatusthx=self.get("aestatusthx")
        aestatuseb=self.get("aestatuseb")
        await call.edit(
                text=f"🎮 <b>Настройки модуля</b> <b>AutoEvo</b>\n\n▫️<b>Статус копания:</b> {aestatusmine}\n▫️<b>Статус Thx:</b> {aestatusthx}\n▫️<b>Статус еб:</b> {aestatuseb}\n\n🛑 После включения/Выключения модуля, перезагрузите или переустановите его 🛑",
                reply_markup=[
                    [
                            {
                                "text": "Вкл/Выкл автокопание",
                                "callback": self.amine,
                            }
                        ],
                    [
                            {
                                "text": "Вкл/Выкл автоthx",
                                "callback": self.athx,
                            }
                        ],
                    [
                            {
                                "text": "Вкл/Выкл автоеб",
                                "callback": self.aeb,
                            }
                        ],
                    [
                            {
                                "text": "Назад",
                                "callback": self.autoevob,
                            }
                        ]
                    ]

            )
    
    async def athx(self, call: InlineCall):
        aestatusthx=not self.get("aestatusthx")
        self.set("aestatusthx", aestatusthx)
        aestatus=self.get("aestatus")
        aestatusmine=self.get("aestatusmine")
        aestatusthx=self.get("aestatusthx")
        aestatuseb=self.get("aestatuseb")
        await call.edit(
                text=f"🎮 <b>Настройки модуля</b> <b>AutoEvo</b>\n\n▫️<b>Статус копания:</b> {aestatusmine}\n▫️<b>Статус Thx:</b> {aestatusthx}\n▫️<b>Статус еб:</b> {aestatuseb}\n\n🛑 После включения/Выключения модуля, перезагрузите или переустановите его 🛑",
                reply_markup=[
                    [
                            {
                                "text": "Вкл/Выкл автокопание",
                                "callback": self.amine,
                            }
                        ],
                    [
                            {
                                "text": "Вкл/Выкл автоthx",
                                "callback": self.athx,
                            }
                        ],
                    [
                            {
                                "text": "Вкл/Выкл автоеб",
                                "callback": self.aeb,
                            }
                        ],
                    [
                            {
                                "text": "Назад",
                                "callback": self.autoevob,
                            }
                        ]
                    ]

            )
    
    async def aeb(self, call: InlineCall):
        aestatuseb=not self.get("aestatuseb")
        self.set("aestatuseb", aestatuseb)
        aestatus=self.get("aestatus")
        aestatusmine=self.get("aestatusmine")
        aestatusthx=self.get("aestatusthx")
        aestatuseb=self.get("aestatuseb")
        await call.edit(
                text=f"🎮 <b>Настройки модуля</b> <b>AutoEvo</b>\n\n▫️<b>Статус копания:</b> {aestatusmine}\n▫️<b>Статус Thx:</b> {aestatusthx}\n▫️<b>Статус еб:</b> {aestatuseb}\n\n🛑 После включения/Выключения модуля, перезагрузите или переустановите его 🛑",
                reply_markup=[
                    [
                            {
                                "text": "Вкл/Выкл автокопание",
                                "callback": self.amine,
                            }
                        ],
                    [
                            {
                                "text": "Вкл/Выкл автоthx",
                                "callback": self.athx,
                            }
                        ],
                    [
                            {
                                "text": "Вкл/Выкл автоеб",
                                "callback": self.aeb,
                            }
                        ],
                    [
                            {
                                "text": "Назад",
                                "callback": self.autoevob,
                            }
                        ]
                    ]

            )
            
    async def autoevob(self, call: InlineCall):
        aestatus=self.get("aestatus")
        aestatusmine=self.get("aestatusmine")
        aestatusthx=self.get("aestatusthx")
        aestatuseb=self.get("aestatuseb")
        await call.edit(
                text=f"🎮 <b>Управление модулем</b> <b>AutoEvo</b>\n\n▫️<b>Статус:</b> {aestatus}\n▫️<b>Статус копания:</b> {aestatusmine}\n▫️<b>Статус Thx:</b> {aestatusthx}\n▫️<b>Статус еб:</b> {aestatuseb}\n\n🛑 После включения/Выключения модуля, перезагрузите или переустановите его 🛑",
                reply_markup=[
                        [
                            {
                                "text": "Вкл/Выкл",
                                "callback": self.inline_but_one,
                            },
                            {
                                "text": "Настройки",
                                "callback": self.settings,
                            }
                        ],
                        [
                            {
                                "text": "Статистика",
                                "callback": self.abobanatr,
                            }
                        ]
                    ]
            )
    async def abobanatr(self, call: InlineCall):
        kts=self.get("kts")
        rkts=self.get("rkts")
        ks=self.get("ks")
        rks=self.get("rks")
        mifs=self.get("mifs")
        krs=self.get("krs")
        zvs=self.get("zvs")
        clicks=self.get("clicks")
        allks=self.get("allks")
        pls=self.get("pls")
        busts=self.get("busts")
        plthx=self.get("plthx")
        pleb=self.get("pleb")
        keb=self.get("keb")
        rkeb=self.get("rkeb")
        mefeb=self.get("mefeb")
        kreb=self.get("kreb")
        await call.edit(
                text=f"🎮 <b>Статистика модуля</b> <b>AutoEvo</b>\n\n<i><b>🧱  | В шахте :\n\n</b></i><emoji document_id=5469718869536940860>👆</emoji> <i>| За {clicks} <b>клика\n\n✉️ | Конверт : {kts}\n</b>🧧 | Редкий Конверт : {rkts}\n📦 | Кейс : {ks}</i>\n<emoji document_id=5359741159566484212>🗳</emoji> <i>| <b>Редкий Кейс : {rks}</b> \n<b>🕋 | Мифический Кейс : {mifs}</b> </i>\n<emoji document_id=5471952986970267163>💎</emoji> <i><b>| Кристальный Кейс : {krs}</b> \n<b>🌌 | Звёздный Кейс : {zvs}</b>\nВсего кейсов с шахты : {allks}</i> \n\n<emoji document_id=5431783411981228752>🎆</emoji><b> | Плазма : {pls}</b> \n<emoji document_id=5431449001532594346>⚡️</emoji> | <b>Бусты : {busts}</b>\n\n<b>Ежедневный бонус :\n🎆 | Плазма : </b>{pleb}\n<i>📦 | <b>Кейс</b> : </i>{keb}\n🗳 <i>| <b>Редкий Кейс : </b></i>{rkeb}\n<b><i>🕋 | Мифический Кейс : </i></b>{mefeb}\n💎 <b><i>| Кристальный Кейс : </i></b>{kreb}\n\n<b>Thx :</b>\n<emoji document_id=5821388137443626414>🌐</emoji> <b>| Плазмы с 'thx' когда благодаришь ты : {plthx}</b>",
                reply_markup=[
                        [
                            {
                                "text": "Назад",
                                "callback": self.autoevob,
                            },
                            {
                                "text": "Обнулить статистику",
                                "callback": self.sbros,
                            }
                        ]
                    ]
            )
            
    @loader.watcher()
    async def thx(self, message):
        if message.chat_id == -1001565066632:
            if self.get("aestatus") == True and self.get("aestatusthx") == True:
                if "(Используй команду Thx чтобы поблагодарить и получить бонус)" in message.raw_text:
                    await self.client.send_message(5522271758, "Thx")
                    await asyncio.sleep(3)
                    await self.client.send_message(5522271758, "Thx")
        if message.chat_id == -1001876775303:
            if self.get("aestatus") == True and self.get("aestatusthx") == True:
                if "(Используй команду Thx чтобы поблагодарить и получить бонус)" in message.raw_text:
                    await self.client.send_message(5522271758, "Thx")
                    await asyncio.sleep(3)
                    await self.client.send_message(5522271758, "Thx")

    @loader.watcher(only_message=True)
    async def watcher(self, message):
        if message.chat_id == 5522271758 and "Ты нашел(ла) конверт." in message.raw_text:
            a = self.get("kts")
            a += 1
            self.set("kts", a)
            b = self.get("allks")
            b += 1
            self.set("allks", b)
        if message.chat_id == 5522271758 and "Ты нашел(ла) редкий конверт." in message.raw_text:
            a = self.get("rkts")
            a += 1
            self.set("rkts", a)
            b = self.get("allks")
            b += 1
            self.set("allks", b)
        if message.chat_id == 5522271758 and "Ты нашел(ла) Кейс!" in message.raw_text:
            a = self.get("ks")
            a += 1
            self.set("ks", a)
            b = self.get("allks")
            b += 1
            self.set("allks", b)
        if message.chat_id == 5522271758 and "Ты нашел(ла) Редкий Кейс!" in message.raw_text:
            a = self.get("rks")
            a += 1
            self.set("rks", a)
            b = self.get("allks")
            b += 1
            self.set("allks", b)
        if message.chat_id == 5522271758 and "Ты нашел(ла) Мифический Кейс!" in message.raw_text:
            a = self.get("mifs")
            a += 1
            self.set("mifs", a)
            b = self.get("allks")
            b += 1
            self.set("allks", b)
        if message.chat_id == 5522271758 and "Ты нашел(ла) Кристальный Кейс!" in message.raw_text:
            a = self.get("krs")
            a += 1
            self.set("krs", a)
            b = self.get("allks")
            b += 1
            self.set("allks", b)
        if message.chat_id == 5522271758 and "Ты нашел(ла) Звёздный Кейс!" in message.raw_text:
            a = self.get("zvs")
            a += 1
            self.set("zvs", a)
            b = self.get("allks")
            b += 1
            self.set("allks", b)
        if message.chat_id == 5522271758 and "Ты нашел(ла) 1 плазму." in message.raw_text:
            a = self.get("pls")
            a += 1
            self.set("pls", a)
        if message.chat_id == 5522271758 and "Ты нашел(ла) 2 плазмы." in message.raw_text:
            a = self.get("pls")
            a += 2
            self.set("pls", a)
        if message.chat_id == 5522271758 and "ты нашел(ла) редкий бустер:" in message.raw_text or "ты нашел(ла) обычный бустер:" in message.raw_text or "ты нашел(ла) ЭПИЧЕСКИЙ бустер:" in message.raw_text:
            a = self.get("busts")
            a += 1
            self.set("busts", a)
        if message.chat_id == 5522271758 and "ты поблагодарил(а) игрока" in message.raw_text and "🎆" in message.raw_text:
            plebc = message.text.index("<b>+") + len("<b>+")
            plebcc = message.text.index("</b>", plebc)
            plebcr = message.text[plebc:plebcc]
            plebcr = plebcr.replace(",","")
            plebcr = int(plebcr)
            pleb = self.get("plthx")
            pleb += plebcr
            self.set("plthx",pleb)
        if message.chat_id == 5522271758 and "Руды до след. ур.:" in message.raw_text:
            a = self.get("clicks")
            a += 1
            self.set("clicks", a)
        if message.chat_id == 5522271758 and "ежедневный бонус получен:" in message.raw_text and "Кейс" in message.raw_text:
            plebc = message.text.index("📦 | <b>Кейс  +") + len("📦 | <b>Кейс  +")
            plebc = message.text.strip().index("📦 | <b>Кейс  +") + len("📦 | <b>Кейс  +")
            plebcc = message.text.index("</b>", plebc)
            plebcr = message.text[plebc:plebcc]
            plebcr = int(plebcr)
            pleb = self.get("keb")
            pleb += plebcr
            self.set("keb",pleb)
        if message.chat_id == 5522271758 and "ежедневный бонус получен:" in message.raw_text and "Плазма" in message.raw_text:
            plebc = message.text.index("🎆 | <b>Плазма  +") + len("🎆 | <b>Плазма  +")
            plebcc = message.text.index("</b>", plebc)
            plebcr = message.text[plebc:plebcc]
            plebcr = int(plebcr)
            pleb = self.get("pleb")
            pleb += plebcr
            self.set("pleb",pleb)
        if message.chat_id == 5522271758 and "ежедневный бонус получен:" in message.raw_text and "Редкий Кейс" in message.raw_text:
            plebc = message.text.index("🗳 | <b>Редкий Кейс  +") + len("🗳 | <b>Редкий Кейс  +")
            plebcc = message.text.index("</b>", plebc)
            plebcr = message.text[plebc:plebcc]
            plebcr = int(plebcr)
            pleb = self.get("rkeb")
            pleb += plebcr
            self.set("rkeb",pleb)
        if message.chat_id == 5522271758 and "ежедневный бонус получен:" in message.raw_text and "Мифический Кейс" in message.raw_text:
            plebc = message.text.index("🕋 | <b>Мифический Кейс  +") + len("🕋 | <b>Мифический Кейс  +")
            plebcc = message.text.index("</b>", plebc)
            plebcr = message.text[plebc:plebcc]
            plebcr = int(plebcr)
            pleb = self.get("mefeb")
            pleb += plebcr
            self.set("mefeb",pleb)
        if message.chat_id == 5522271758 and "ежедневный бонус получен:" in message.raw_text and "Кристальный Кейс" in message.raw_text:
            plebc = message.text.index("💎 | <b>Кристальный Кейс  +") + len("💎 | <b>Кристальный Кейс  +")
            plebcc = message.text.index("</b>", plebc)
            plebcr = message.text[plebc:plebcc]
            plebcr = int(plebcr)
            pleb = self.get("kreb")
            pleb += plebcr
            self.set("kreb",pleb)

    async def sbros(self, call: InlineCall):
        self.set("clicks", 0)
        self.set("kts", 0)
        self.set("rkts", 0)
        self.set("ks", 0)
        self.set("rks", 0)
        self.set("mifs", 0)
        self.set("krs", 0)
        self.set("zvs", 0)
        self.set("allks", 0)
        self.set("pls", 0)
        self.set("busts", 0)
        self.set("plthx", 0)
        self.set("pleb", 0)
        self.set("keb", 0)
        self.set("rkeb", 0)
        self.set("mefeb", 0)
        self.set("kreb", 0)
        await call.answer("Вы обнулили статистику!")
        kts=self.get("kts")
        rkts=self.get("rkts")
        ks=self.get("ks")
        rks=self.get("rks")
        mifs=self.get("mifs")
        krs=self.get("krs")
        zvs=self.get("zvs")
        clicks=self.get("clicks")
        allks=self.get("allks")
        pls=self.get("pls")
        busts=self.get("busts")
        plthx=self.get("plthx")
        pleb=self.get("pleb")
        keb=self.get("keb")
        rkeb=self.get("rkeb")
        mefeb=self.get("mefeb")
        kreb=self.get("kreb")
        await call.edit(
                text=f"🎮 <b>Статистика модуля</b> <b>AutoEvo</b>\n\n<i><b>🧱  | В шахте :\n\n</b></i><emoji document_id=5469718869536940860>👆</emoji> <i>| За {clicks} <b>клика\n\n✉️ | Конверт : {kts}\n</b>🧧 | Редкий Конверт : {rkts}\n📦 | Кейс : {ks}</i>\n<emoji document_id=5359741159566484212>🗳</emoji> <i>| <b>Редкий Кейс : {rks}</b> \n<b>🕋 | Мифический Кейс : {mifs}</b> </i>\n<emoji document_id=5471952986970267163>💎</emoji> <i><b>| Кристальный Кейс : {krs}</b> \n<b>🌌 | Звёздный Кейс : {zvs}</b>\nВсего кейсов с шахты : {allks}</i> \n\n<emoji document_id=5431783411981228752>🎆</emoji><b> | Плазма : {pls}</b> \n<emoji document_id=5431449001532594346>⚡️</emoji> | <b>Бусты : {busts}</b>\n\n<b>Ежедневный бонус :\n🎆 | Плазма : </b>{pleb}\n<i>📦 | <b>Кейс</b> : </i>{keb}\n🗳 <i>| <b>Редкий Кейс : </b></i>{rkeb}\n<b><i>🕋 | Мифический Кейс : </i></b>{mefeb}\n💎 <b><i>| Кристальный Кейс : </i></b>{kreb}\n\n<b>Thx :</b>\n<emoji document_id=5821388137443626414>🌐</emoji> <b>| Плазмы с 'thx' когда благодаришь ты : {plthx}</b>",
                reply_markup=[
                        [
                            {
                                "text": "Назад",
                                "callback": self.autoevob,
                            },
                            {
                                "text": "Обнулить статистику",
                                "callback": self.sbros,
                            }
                        ]
                    ]
            )
