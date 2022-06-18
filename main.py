from discord.ext import commands
import discord
from scoreboard_pilna import ScoreBoard
import os

bot = commands.Bot(command_prefix='/')
DISCORD_BOT_TOKEN = os.environ['DISCORD_BOT_TOKEN']


def get_embed(data: dict, time_range="") -> discord.Embed:
    ad = ""

    if time_range != "":
        ad += " | {}".format(time_range)

    names = ""
    values = ""

    for key, val in data.items():
        if key != "":
            names += "{}\n".format(key)
            values += "{}\n".format(val)

    result = discord.Embed(
        title=f"Pilna Scoreboard{ad}",
        color=discord.Color.purple()
    )

    result.add_field(
        name="Name",
        value=names
    )

    result.add_field(
        name="Incidents Count",
        value=values
    )

    return result


@bot.command()
async def pilna_d(ctx, date):
    result = ScoreBoard().get_stats_from_date(date)
    if type(result) == str:
        await ctx.channel.send(result)
    else:
        result = get_embed(result, date)
        await ctx.channel.send(embed=result)


@bot.command()
async def pilna_m(ctx, month):
    month = int(month)
    result = ScoreBoard().get_month_stats(month)

    if month == 1:
        name = "January"
    elif month == 2:
        name = "February"
    elif month == 3:
        name = "March"
    elif month == 4:
        name = "April"
    elif month == 5:
        name = "May"
    elif month == 6:
        name = "June"
    elif month == 7:
        name = "July"
    elif month == 8:
        name = "August"
    elif month == 9:
        name = "September"
    elif month == 10:
        name = "October"
    elif month == 11:
        name = "November"
    elif month == 12:
        name = "December"

    if type(result) == str:
        await ctx.channel.send(result)
    else:
        result = get_embed(result, name)
        await ctx.channel.send(embed=result)


@bot.command()
async def pilna_t(ctx):
    result = ScoreBoard().get_today_stats()
    result = get_embed(result, "Today")
    await ctx.channel.send(embed=result)


@bot.command()
async def pilna(ctx):
    result = ScoreBoard().get_stats()
    result = get_embed(result)
    await ctx.channel.send(embed=result)


@bot.command()
async def t_help(ctx):
    result = """
        Available Commands:\t
        /t_help\t
        /pilna \t\t[t -> today / date e.g. '2022-06-17']
    """
    await ctx.channel.send(result)


bot.run(DISCORD_BOT_TOKEN)
