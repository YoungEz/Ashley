import discord

from discord.ext import commands
from resources.check import check_it
from resources.db import Database


class ReceptionClass(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @check_it(no_pm=True)
    @commands.cooldown(1, 5.0, commands.BucketType.user)
    @commands.check(lambda ctx: Database.is_registered(ctx, ctx))
    @commands.command(name='reception', aliases=['recepção', 'rp'])
    async def reception(self, ctx):

        def check(m):
            return m.author == ctx.author

        lista = ['welcome', 'leaving', 'ban', 'private']
        for c in lista:
            data = {}
            embed = discord.Embed(
                title='PlaceHolders',
                color=0x456332,
                description='.{user}\n'
                            '.{@user}\n'
                            '.{nickname}\n'
                            '.{user-discriminator}\n'
                            '.{user-id}\n'
                            '.{user-avatar-url}\n'
                            '.{guild}\n'
                            '.{guild-size}')
            await ctx.send(embed=embed)
            msg = await ctx.send('Deseja ativar uma mensagem pra {}? s/n'.format(c))
            resp = await self.bot.wait_for('message', check=check)
            while resp.content.lower() not in ['s', 'n']:
                resp = await self.bot.wait_for('message', check=check)
            if resp.content.lower() == 's':
                data['status'] = True
            else:
                data['status'] = False
            await msg.delete()
            if data['status'] is True:
                if c != 'private':
                    msg = await ctx.send('Marque um canal para {}.'.format(c))
                    resp = await self.bot.wait_for('message', check=check)
                    data['channelid'] = int(str(resp.content).replace('<#', '').replace('>', ''))
                    await msg.delete()
                data['embed'] = {}
                msg = await ctx.send('Deseja usar um embed pra {}? s/n'.format(c))
                resp = await self.bot.wait_for('message', check=check)
                while resp.content.lower() not in ['s', 'n']:
                    resp = await self.bot.wait_for('message', check=check)
                if resp.content.lower() == 's':
                    data['embed']['status'] = True
                else:
                    data['embed']['status'] = False
                await msg.delete()
                if data['embed']['status'] is False:
                    msg = await ctx.send('Defina uma mensagem pra {}.'.format(c))
                    resp = await self.bot.wait_for('message', check=check)
                    resp = resp.content
                    while len(resp) > 1900:
                        ctx.send('Mensagem muito longa, favor usar {} caracteres a menos.'.format(len(resp)-1900))
                        resp = await self.bot.wait_for('message', check=check)
                        resp = resp.content
                    data['message'] = resp
                    await msg.delete()
                else:
                    total = 0
                    msg = await  ctx.send('Defina um titulo pro embed de {}.'.format(c))
                    resp = await self.bot.wait_for('message', check=check)
                    resp = resp.content
                    data['embed']['title'] = resp
                    total += len(data['embed']['title'])
                    await msg.delete()
                    msg = await  ctx.send('Defina uma cor pro embed de {}.(em hexadecimal)'.format(c))
                    resp = await self.bot.wait_for('message', check=check)
                    resp = resp.content
                    while True:
                        try:
                            color = int(resp, 16)
                            if color is not None:
                                break
                        except TypeError:
                            await ctx.send('Isso não é uma cor, tente denovo.')
                            resp = await self.bot.wait_for('message', check=check)
                            resp = resp.content
                    data['embed']['color'] = resp
                    await msg.delete()
                    msg = await  ctx.send('Defina uma cor pro embed de {}.(em hexadecimal)'.format(c))
                    resp = await self.bot.wait_for('message', check=check)
                    resp = resp.content
                    total += len(resp)
                    data['embed']['description'] = resp
                    await msg.delete()
                    msg = await  ctx.send('Defina uma imagem pro embed de {}.'
                                          '(use um url, placeholder user-avatar-url é usavel aqui. '
                                          'Se não quiser coloque 0.)'.format(c))
                    resp = await self.bot.wait_for('message', check=check)
                    resp = resp.content
                    data['embed']['image'] = resp
                    await msg.delete()
                    msg = await  ctx.send('Defina uma thumbnail pro embed de {}.(use um url, '
                                          'placeholder user-avatar-url é usavel aqui. '
                                          'Se não quiser coloque 0.)'.format(c))
                    resp = await self.bot.wait_for('message', check=check)
                    resp = resp.content
                    data['embed']['thumbnail'] = resp
                    await msg.delete()
                    data['embed']['fields'] = {}
                    limitedecampos = 3
                    listalimite = []
                    for c2 in range(0, limitedecampos+1):
                        listalimite.append(str(c2))
                    msg = await  ctx.send('Defina um numero de campos pro embed de {}.'
                                          '(0 caso não queira usar, até 3.)'.format(c))
                    resp = await self.bot.wait_for('message', check=check)
                    resp = resp.content
                    while resp not in listalimite:
                        msg = await  ctx.send('Numero invalido ou fora de limite.')
                        resp = await self.bot.wait_for('message', check=check)
                        resp = resp.content
                    data['embed']['fields']['numero'] = int(resp)
                    await msg.delete()
                    data['embed']['fields']['fields'] = []
                    for c2 in range(0, data['embed']['fields']['numero']):
                        templist = []
                        msg = await  ctx.send('Defina o titulo {}º campo.'.format(c2))
                        resp = await self.bot.wait_for('message', check=check)
                        resp = resp.content
                        templist.append(resp)
                        await msg.delete()
                        msg = await  ctx.send('Defina o conteudo {}º campo.'.format(c2))
                        resp = await self.bot.wait_for('message', check=check)
                        resp = resp.content
                        templist.append(resp)
                        await msg.delete()
                        data['embed']['fields']['fields'].append(templist)
        await ctx.send('configuração feita com sucesso')


def setup(bot):
    bot.add_cog(ReceptionClass(bot))
    print('\033[1;32m( 🔶 ) | O comando \033[1;34mRECEPTION_SYSTEM\033[1;32m foi carregado com sucesso!\33[m')