import discord
from discord.ext import commands
from discord.ext.commands import has_permissions
from functions import *
from utils import *

intents = discord.Intents(messages=True, guilds=True, reactions=True, members=True, presences=True)
Bot = commands.Bot(command_prefix='.', intents=intents)
game = Game()
bot = discord.ext.commands.Bot(command_prefix="your_prefix");


@Bot.event
async def on_ready():
    print("Let's Go ")


@Bot.event
async def on_member_join(member):
    channel = discord.utils.get(member.guild.text_channels, name="gelenler")
    await channel.send(f"{member} Sunucuya Katıldı.")
    print(f"{member} Sunucuya Katıldı.")


@Bot.event
async def on_member_remove(member):
    channel = discord.utils.get(member.guild.text_channels, name="gelenler")
    await channel.send(f"{member} Sunucudan Ayrıldı.")
    print(f"{member} Sunucudan Ayrıldı.")


@Bot.command()
# @has_permissions(administrator=True)
async def sil(ctx, amount=5):
    await ctx.channel.purge(limit=amount)
    print(f"Başarı ile temizlendi.")

    # @Bot.command()
    # async def join(ctx):
    #    channel = message.author.voice.channel
    #    await channel.connect()

    # @Bot.command(pass_content=True)
    # async def join(ctx):
    #    channel = ctx.author.voice.channel
    #    await channel.connect()


@Bot.command()
async def join(ctx):
    if (ctx.author.voice):
        channel = ctx.author.voice.channel
        await channel.connect()
        await ctx.send('Bot joined')
    else:
        await ctx.send("You must be in a voice channel first so I can join it.")


@Bot.command()
async def leave(
        ctx):
    if (ctx.voice_client):
        await ctx.guild.voice_client.disconnect()
        await ctx.send('Bot left')
    else:
        await ctx.send("I'm not in a voice channel, use the join command to make me join")


# @Bot.command(pass_content=True)
# async def leave(ctx):
#   channel = ctx.message.author


# await ctx.send(f'Bot Herhangi Bir Odada Değil')py
# return


@Bot.command(aliases=["kopyala"])
@has_permissions(administrator=True)
async def clone_channel(ctx, amount=1):
    for i in range(amount):
        await ctx.channel.clone()


@Bot.command(pass_context=True)
@has_permissions(administrator=True)
async def kick(ctx, user: discord.Member):
    await ctx.send(f'The Kicking Hammer Has Awoken! {user.name} Has Been Banished', )
    await ctx.guild.kick(user)


@Bot.command(pass_context=True)
@has_permissions(administrator=True)
async def ban(ctx, user: discord.Member):
    await ctx.send(
        f'Ban Çekicini Kafasına Yedi! {user.name} Artık Uzaklarda!' 'https://media1.giphy.com/media/fe4dDMD2cAU5RfEaCU/giphy.gif?cid=ecf05e47kie7ltgktey7bkzrng32arpvxbfuk6fyd3niq0da&rid=giphy.gif')
    await ctx.guild.ban(user)
    return


@Bot.command()
@has_permissions(administrator=True)
async def unban(ctx, *, member):
    banned_users = await ctx.guild.bans()
    member_name, member_discriminator = member.split('#')

    for bans in banned_users:
        user = bans.user

        if (user.name, member_discriminator) == (member_name, member_discriminator):
            await ctx.guild.unban(user)
            await ctx.send(
                f'Geri Getirme Büyüsü Yapıldı! {user.name} Artık Aramıza Gelebilir!' 'https://media0.giphy.com/media/MB6OMCu3uQQrgVIsSu/giphy.gif')
            return


@Bot.command()
async def komutlar(ctx):
    await ctx.send('amcıemre1 amcıemre2 join leave zar at')


@Bot.command()
async def amciemre1(ctx, *args):
    await ctx.send('https://tenor.com/view/polis-emre-amcık-görüyor-gif-19133767')


@Bot.command()
async def amciemre2(ctx, *args):
    await ctx.send('https://tenor.com/view/seemih-fidan-emre-amcıemre-31-gif-19753463')


@Bot.command()
async def yarra(ctx):
    await ctx.send('https://tenor.com/view/yarra-yarra-beni-yarra-aşkına-beter-beter-ali-gif-16749214')


@Bot.command()
async def fcukyou(ctx):
    await ctx.send('https://media.discordapp.net/attachments/763053037332725790/805519690617192518/image0-34.gif')


@Bot.command()
@has_permissions(administrator=True)
async def aktif(ctx):
    await ctx.send('https://cdn.discordapp.com/attachments/814893842469617665/817484594706251776/giphy.gif')


@Bot.command(aliases=["zar"])
async def lafıkoyunca(ctx, *args):
    if "at" in args:
        await ctx.send(game.at_dice())
    else:
        await ctx.send(
            '@everyone,https://tenor.com/view/kerpeten-ali-kerpeten-ali-kerpeten-dans-hip-hop-dans-gif-19947997')

@Bot.command()
async def lspd(ctx,):
        await ctx.send(
            'https://media.giphy.com/media/QUY2pzDAKVpX3QacCg/giphy.gif')

@Bot.command()
async def ip(ctx, ):
        await ctx.send(
            'F8 connect 185.88.174.226 TS3 IP : navyts3')

@Bot.command()
async def woul(ctx, ):
        await ctx.send(
            'connect 185.126.178.26 TeamSpeak: woulroleplay')

Bot.run(TOKEN)
