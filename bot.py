from discord.ext import commands
import discord

import config

bot = commands.Bot(command_prefix="s!")

@bot.event
async def on_ready():
    print(f"{bot.user} is ready! | {len(bot.guilds)} guilds | {len(bot.users)} users")

@bot.command(hidden=True)
@commands.is_owner()
async def die(ctx):
    await ctx.send("Bye!")
    await bot.logout()

if __name__ == "__main__":
    bot.config = config
    bot.run(config.token)
