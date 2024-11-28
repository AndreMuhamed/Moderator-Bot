<div align="center">  
  <h1>🚀 Старт Moderator Bot</h1>  
</div>  
  
<div align="center">
  <a href="https://github.com/AndreMuhamed/Muhamed_OneDrive/blob/main/README.md" target="_blank"><img src="https://github.com/AndreMuhamed/Muhamed_OneDrive/blob/main/Language/298489_ukraine_ukraine.png?raw=true" alt="ua" width="25" height="25"></a>
  <a href="https://github.com/AndreMuhamed/Muhamed_OneDrive/blob/main/README_Russia.md" target="_blank"><img src="https://github.com/AndreMuhamed/Muhamed_OneDrive/blob/main/Language/298434_russia_russia.png?raw=true" alt="ru" width="25" height="25"></a>
  <a href="https://github.com/AndreMuhamed/Muhamed_OneDrive/blob/main/README_English.md" target="_blank"><img src="https://github.com/AndreMuhamed/Muhamed_Pro-Suite/blob/main/Language/298478_kingdom_united_kingdom_united.png?raw=true" alt="en" width="25" height="25"></a>
  <a href="https://github.com/AndreMuhamed/Muhamed_OneDrive/blob/main/README_Canadian.md" target="_blank"><img src="https://github.com/AndreMuhamed/Muhamed_Pro-Suite/blob/main/Language/298562_canada_canada.png?raw=true" alt="cn" width="25" height="25"></a>
  <a href="https://github.com/AndreMuhamed/Muhamed_OneDrive/blob/main/README_Polish.md" target="_blank"><img src="https://github.com/AndreMuhamed/Muhamed_Pro-Suite/blob/main/Language/298479_poland_poland.png?raw=true" alt="pl" width="25" height="25"></a>
</div>

![Muhamed](https://github.com/AndreMuhamed/Muhamed_Pro-Suite/blob/main/Plug-photo/%D0%A8%D0%B0%D0%B1%D0%BA%D0%B0%D0%9C%D1%83%D1%85%D0%B0%D0%BC%D0%B5%D0%B4%D0%B0copyUA.jpg?raw=true)

## Описание

**Moderator Bot** — это бот для Discord, разработанный с использованием языка программирования Python и библиотеки Discord.py. Он предоставляет функционал для модерации серверов и улучшения взаимодействия участников.

### Возможности бота:
- Ответы на команды пользователей.
- Мониторинг чата на нарушения правил.
- Предупреждение пользователей о поведении.
- Исключение или блокировка пользователей, нарушающих правила.

---

## Пример кода

Файл: `disty.py`

```python
import discord
from discord.ext import commands
from discord.ext.commands import has_permissions

intents = discord.Intents.default()
bot = commands.Bot(command_prefix="!", intents=intents)

@bot.event
async def on_ready():
    print(f'Logged in as {bot.user}')

@bot.command()
async def ping(ctx):
    await ctx.send("Pong!")

@bot.command()
@has_permissions(kick_members=True)
async def kick(ctx, member: discord.Member, *, reason=None):
    await member.kick(reason=reason)
    await ctx.send(f"{member} был исключён по причине: {reason}")

@bot.command()
@has_permissions(ban_members=True)
async def ban(ctx, member: discord.Member, *, reason=None):
    await member.ban(reason=reason)
    await ctx.send(f"{member} был заблокирован по причине: {reason}")

@bot.event
async def on_message(message):
    if message.content.startswith("!rules"):
        await message.channel.send("Пожалуйста, следуйте правилам чата!")
    await bot.process_commands(message)

bot.run("YOUR_TOKEN")
```

---

## Настройка

1. Замените `YOUR_TOKEN` в коде на ваш уникальный `token`, полученный в [Discord Developer Portal](https://discord.com/developers/applications).
2. Добавьте бота на ваш сервер, используя сгенерированную ссылку OAuth2.

---

## Примечания

- Команды `!kick` и `!ban` доступны только для пользователей с соответствующими правами.
- Вы можете адаптировать функционал бота под ваши нужды.

---

## Отказ от ответственности

Автор не несёт ответственности за работоспособность данного бота. Проверьте код и настройки перед использованием.
