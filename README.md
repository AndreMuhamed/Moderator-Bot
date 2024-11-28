
# Moderator-Bot

![Discord Bot](https://user-images.githubusercontent.com/128980327/232897633-92ca2eaa-42e3-4b1b-8378-eb8487806f67.jpg)

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
