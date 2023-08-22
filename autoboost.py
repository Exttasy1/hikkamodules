import asyncio
from telethon.tl.types import Message, ChatAdminRights
from telethon import functions
from .. import loader, utils
from ..inline.types import InlineCall

# idea: @exttasy1
# meta developer: @mineevor

@loader.tds
class AutoBoost(loader.Module):
    """Модуль на автоматическое использование вами указанного бустера"""
    strings = {
        "name": "AutoBoost"
    }

    def __init__(self):
        self.config = loader.ModuleConfig(
                loader.ConfigValue(
                    "status",
                    False,
                    lambda: "НЕ ТРОГАТЬ!!",
                    validator=loader.validators.Boolean()
                ),
                loader.ConfigValue(
                    "type",
                    None,
                    lambda: "Тут напишите тип бустера, Р/Д",
                    validator=loader.validators.String()
                ),
                loader.ConfigValue(
                    "mnoz",
                    None,
                    lambda: "Тут напишите множитель бустера, 1.5, 2, 2.5, 3",
                    validator=loader.validators.Float()
                )
            )
    
    async def client_ready(self):
        self._backup_channel, _ = await utils.asset_channel(
            self._client,
            "AutoBoostChat",
            "Группа для работы модуля AutoBoost от @exttasy1\nНе добавляйте сюда других людей или ботов!",
            silent=True,
            archive=True,
            _folder="hikka",
        )
        await self.client(functions.channels.InviteToChannelRequest(self._backup_channel, ['@mine_evo_bot']))
        await self.client(functions.channels.EditAdminRequest(
                channel=self._backup_channel,
                user_id="@mine_evo_bot",
                admin_rights=ChatAdminRights(ban_users=True, post_messages=True, edit_messages=True),
                rank="EVO",
            )
        )
    
    @loader.watcher(only_message=True, chat_id=5522271758)
    async def watcher(self, message):
        if self.config["status"]:
            type = self.config["type"]
            mnoz = self.config["mnoz"]
            if "закончил свое действие." in message.raw_text:
                await self.client.send_message(self._backup_channel, f"Буст {type} {mnoz}")
                
    @loader.command()
    async def ab(self, message):
        """Управление модулем кнопками"""
        type = self.config["type"]
        mnoz = self.config["mnoz"]
        if self.config["status"]:
            status = "Включен"
        else:
            status = "Выключен"
        if self.config["type"] == "Р":
            typea = "Руда"
        elif self.config["type"] == "Д":
            typea = "Деньги"
        else:
            typea = ""
        await self.inline.form(
                text=f"🎮 <b>Упраление модулем</b> <b>AutoBoost</b>\n\n▫️<b>Статус:</b> {status}\n▫️<b>Текущий бустер:</b> {typea} {mnoz}",
                message=message,
                reply_markup=[
                        {
                            "text": "Вкл/Выкл",
                            "callback": self.inline_but_one,
                        },
                        {
                            "text": "Настройки",
                            "callback": self.inline_but_two,
                        }
                    ]
            )
            
    async def inline_but_one(self, call: InlineCall):
        self.config["status"] = not self.config["status"]
        status = self.config["status"]
        await call.answer(f"AutoBoost {status}")
        if self.config["status"]:
            type = self.config["type"]
            mnoz = self.config["mnoz"]
            await self.client.send_message(self._backup_channel, f"Буст {type} {mnoz}")
        type = self.config["type"]
        mnoz = self.config["mnoz"]
        if self.config["status"]:
            status = "Включен"
        else:
            status = "Выключен"
        if self.config["type"] == "Р":
            typea = "Руда"
        elif self.config["type"] == "Д":
            typea = "Деньги"
        else:
            typea = ""
        await call.edit(
                text=f"🎮 <b>Упраление модулем</b> <b>AutoBoost</b>\n\n▫️<b>Статус:</b> {status}\n▫️<b>Текущий бустер:</b> {typea} {mnoz}",
                reply_markup=[
                        {
                            "text": "Вкл/Выкл",
                            "callback": self.inline_but_one,
                        },
                        {
                            "text": "Настройки",
                            "callback": self.inline_but_two,
                        }
                    ]
            )
    
    async def inline_but_two(self, call: InlineCall):
        if self.config["type"] == "Р":
            typea = "Руда"
        elif self.config["type"] == "Д":
            typea = "Деньги"
        else:
            typea = ""
        type = self.config["type"]
        mnoz = self.config["mnoz"]
        await call.edit(
                text=f"⚙️ <b>Настройки</b>\n\n▫️<b>Тип:</b> {typea}\n▫️<b>Множитель: </b>{mnoz}",
                reply_markup=[
                        [
                            {
                                "text": "Тип",
                                "callback": self.inline_but_four,
                            },
                            {
                                "text": "Множитель",
                                "callback": self.inline_but_five,
                            }
                        ],
                        [
                            {
                                "text": "Назад",
                                "callback": self.inline_but_three,
                            }
                        ]
                    ]
            )
            
    async def inline_but_three(self, call: InlineCall):
        type = self.config["type"]
        mnoz = self.config["mnoz"]
        if self.config["status"]:
            status = "Включен"
        else:
            status = "Выключен"
            
        if self.config["type"] == "Р":
            typea = "Руда"
        elif self.config["type"] == "Д":
            typea = "Деньги"
        else:
            typea = ""
        await call.edit(
                text=f"🎮 <b>Упраление модулем</b> <b>AutoBoost</b>\n\n▫️<b>Статус:</b> {status}\n▫️<b>Текущий бустер:</b> {typea} {mnoz}",
                reply_markup=[
                        {
                            "text": "Вкл/Выкл",
                            "callback": self.inline_but_one,
                        },
                        {
                            "text": "Настройки",
                            "callback": self.inline_but_two,
                        }
                    ]
            )
            
        
            
    async def inline_but_four(self, call: InlineCall):
        await call.edit(
                text=f"🗒️ <b>Выберите тип бустера:</b>",
                reply_markup=[
                        [
                            {
                                "text": "Руда",
                                "callback": self.abobaone,
                            },
                            {
                                "text": "Деньги",
                                "callback": self.abobatwo,
                            }
                        ],
                        [
                            {
                                "text": "Назад",
                                "callback": self.inline_but_twoa,
                            }
                        ]
                    ]
            )
            
    async def inline_but_twoa(self, call: InlineCall):
        type = self.config["type"]
        mnoz = self.config["mnoz"]
        if self.config["type"] == "Р":
            typea = "Руда"
        elif self.config["type"] == "Д":
            typea = "Деньги"
        else:
            typea = ""
        await call.edit(
                text=f"⚙️ <b>Настройки</b>\n\n▫️<b>Тип:</b> {typea}\n▫️<b>Множитель: </b>{mnoz}",
                reply_markup=[
                        [
                            {
                                "text": "Тип",
                                "callback": self.inline_but_four,
                            },
                            {
                                "text": "Множитель",
                                "callback": self.inline_but_five,
                            }
                        ],
                        [
                            {
                                "text": "Назад",
                                "callback": self.inline_but_three,
                            }
                        ]
                    ]
            )
        
    async def inline_but_five(self, call: InlineCall):
        await call.edit(
                text=f"🗒️ <b>Выберите множитель бустера:</b>",
                reply_markup=[
                        [
                            {
                                "text": "1.5",
                                "callback": self.abobathree,
                            },
                            {
                                "text": "2.0",
                                "callback": self.abobafour,
                            },
                            {
                                "text": "2.5",
                                "callback": self.abobafive,
                            },
                            {
                                "text": "3.0",
                                "callback": self.abobasix,
                            }

                        ],
                        [
                            {
                                "text": "Назад",
                                "callback": self.inline_but_twoa,
                            }
                        ]
                    ]
            )
            
    async def abobaone(self, call: InlineCall):
        await call.edit(
                text=f"<b>📝 Вы изменили тип бустера на:</b> \"Руда\"",
                reply_markup=[
                        {
                            "text": "Назад",
                            "callback": self.inline_but_twoa,
                        }
                    ]
            )
        self.config["type"] = "Р"
        
    async def abobatwo(self, call: InlineCall):
        await call.edit(
                text=f"<b>📝 Вы изменили тип бустера на:</b> \"Деньги\"",
                reply_markup=[
                        {
                            "text": "Назад",
                            "callback": self.inline_but_twoa,
                        }
                    ]
            )
        self.config["type"] = "Д"
        
    async def abobathree(self, call: InlineCall):
        await call.edit(
                text=f"<b>📝 Вы изменили множитель бустера на:</b> \"1.5\"",
                reply_markup=[
                        {
                            "text": "Назад",
                            "callback": self.inline_but_twoa,
                        }
                    ]
            )
        self.config["mnoz"] = 1.5
        
    async def abobafour(self, call: InlineCall):
        await call.edit(
                text=f"<b>📝 Вы изменили множитель бустера на:</b> \"2.0\"",
                reply_markup=[
                        {
                            "text": "Назад",
                            "callback": self.inline_but_twoa,
                        }
                    ]
            )
        self.config["mnoz"] = 2.0
        
    async def abobafive(self, call: InlineCall):
        await call.edit(
                text=f"<b>📝 Вы изменили множитель бустера на:</b> \"2.5\"",
                reply_markup=[
                        {
                            "text": "Назад",
                            "callback": self.inline_but_twoa,
                        }
                    ]
            )
        self.config["mnoz"] = 2.5
        
    async def abobasix(self, call: InlineCall):
        await call.edit(
                text=f"<b>📝 Вы изменили множитель бустера на:</b> \"3.0\"",
                reply_markup=[
                        {
                            "text": "Назад",
                            "callback": self.inline_but_twoa,
                        }
                    ]
            )
        self.config["mnoz"] = 3.0
