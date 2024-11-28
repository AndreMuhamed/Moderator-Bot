<div align="center">  
  <h1>🚀 Start of Moderator-Bot</h1>   </div>  
  
<div align="center">
  <a href="https://github.com/AndreMuhamed/Muhamed_OneDrive/blob/main/README.md" target="_blank"><img src="https://github.com/AndreMuhamed/Muhamed_OneDrive/blob/main/Language/298489_ukraine_ukraine.png?raw=true" alt="ua" width="25" height="25"></a>
  <a href="https://github.com/AndreMuhamed/Muhamed_OneDrive/blob/main/README_Russia.md" target="_blank"><img src="https://github.com/AndreMuhamed/Muhamed_OneDrive/blob/main/Language/298434_russia_russia.png?raw=true" alt="ru" width="25" height="25"></a>
  <a href="https://github.com/AndreMuhamed/Muhamed_OneDrive/blob/main/README_English.md" target="_blank"><img src="https://github.com/AndreMuhamed/Muhamed_Pro-Suite/blob/main/Language/298478_kingdom_united_kingdom_united.png?raw=true" alt="en" width="25" height="25"></a>
  <a href="https://github.com/AndreMuhamed/Muhamed_OneDrive/blob/main/README_Canadian.md" target="_blank"><img src="https://github.com/AndreMuhamed/Muhamed_Pro-Suite/blob/main/Language/298562_canada_canada.png?raw=true" alt="cn" width="25" height="25"></a>
  <a href="https://github.com/AndreMuhamed/Muhamed_OneDrive/blob/main/README_Polish.md" target="_blank"><img src="https://github.com/AndreMuhamed/Muhamed_Pro-Suite/blob/main/Language/298479_poland_poland.png?raw=true" alt="pl" width="25" height="25"></a>
</div>

## Опис

**Moderator-Bot** — це бот для Discord, створений за допомогою мови програмування Python та бібліотеки Discord.py. Він має функціонал для модерації серверів та покращення взаємодії між учасниками.

### Можливості бота:
- Відповіді на команди користувачів.
- Моніторинг чату на порушення правил.
- Попередження користувачів про їх поведінку.
- Заборона або виключення користувачів, які порушують правила.

---

## Приклад коду

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
    await ctx.send(f"{member} був виключений за причиною: {reason}")

@bot.command()
@has_permissions(ban_members=True)
async def ban(ctx, member: discord.Member, *, reason=None):
    await member.ban(reason=reason)
    await ctx.send(f"{member} був заблокований за причиною: {reason}")

@bot.event
async def on_message(message):
    if message.content.startswith("!rules"):
        await message.channel.send("Будь ласка, дотримуйтесь правил чату!")
    await bot.process_commands(message)

bot.run("YOUR_TOKEN")
```


## Налаштування

1. Замініть `YOUR_TOKEN` у коді на ваш унікальний `token`, отриманий у [Discord Developer Portal](https://discord.com/developers/applications).
2. Додайте бота на ваш сервер, використовуючи згенероване посилання OAuth2.

---

## Примітки

- Команди `!kick` та `!ban` доступні лише для користувачів із відповідними дозволами.
- Ви можете адаптувати функціонал бота під ваші потреби.

---

## Відмова від відповідальності

Автор не несе відповідальності за працездатність цього бота. Перевірте код і налаштування перед використанням.
```

### Особливості:
- Заголовки розбиті на логічні секції.
- Додано горизонтальні лінії для візуального розмежування.
- Код відформатований у блоки з підсвіченням синтаксису Python.
- Інструкції налаштування подані зрозуміло.
