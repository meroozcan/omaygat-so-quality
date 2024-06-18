import discord
from discord.ext import commands

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='$', intents=intents)

@bot.event
async def on_ready():
    print(f'We have logged in as {bot.user}')

@bot.command()
async def nasıl_çevre_kirliliğini_engellerim(ctx):
    await ctx.send("Öncelikle çevre kirliliğini engelleyemeyiz fakat çöpleri çöpe atmalı sonrada insanlara bunu söylemelisiniz. Deodorant gibi ürünleri azaltabilir, benzinli araba yerine elektrikli araba kullanabilirsiniz. Ağaçları kesmemeli hatta dikmelisiniz. Denizlere çöp atmamalıyız eğer denizlere çöp atar isek denizdeki canlıların hayatını kötü etkileyebilir. Hava kirliliği için fabrikaların filtre takması lazım filtre takmazlar ise çevreyi çok fazla kirletirler böylece çevre kirliliğini durduramayız fakat çevre kirliliğini yavaşlatabiliriz.")

@bot.command()
async def nasıl_ışık_kirliliğini_engellerim(ctx):
    await ctx.send("Öncelikle işik kirliliğini engelleyemeyiz fakat onun için önlemler alabiliriz mesela: Kullanmadiğimiz odalarin işiğini kapatmaliyiz araba farlarını daha az uzunlukta kullanmak. Sokaklarda kullanılan ışıkları azaltabiliriz. Gökdelenleri daha az kullanmalıyız. LED aydınlatmalar kullanabiliriz. Sensörler kullanabiliriz. İnsanları ışık kirliliği konusunda bilinçlendirebiliriz. Aydınlatma seviyelerini en aza indirebiliriz veya Işığın istenmeyen yönlere dağılmaması engellemek için yön kontrolü sağlayabiliriz.")


