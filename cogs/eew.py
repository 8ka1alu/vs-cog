from discord.ext import commands, tasks # Bot Commands Frameworkのインポート
import discord
import asyncio
import json
import urllib.request

great_owner_id = 459936557432963103

# コグとして用いるクラスを定義。
class eew(commands.Cog):
    # testクラスのコンストラクタ。Botを受取り、インスタンス変数として保持。
    def __init__(self, bot):
        self.bot = bot
        self.code = 0
        self.loop.start()

    def cog_unload(self, bot):
        self.loop.cancel() 

    @commands.command()
    async def eew(self, ctx):
        """地震情報(最新)"""
        resp = urllib.request.urlopen('http://svir.jp/eew/data.json')
        eew = json.loads(resp.read().decode('utf-8'))
        embed=discord.Embed(title="**地震情報**", description=eew['Head']['Title'])
        embed.add_field(name="発表時刻", value=eew['Body']['Earthquake']['OriginTime'], inline=False)
        embed.add_field(name="震源地", value=eew['Body']['Earthquake']['Hypocenter']['Name'], inline=False)
        embed.add_field(name="マグニチュード", value=eew['Body']['Earthquake']['Magnitude'], inline=False) 
        embed.add_field(name="深さ", value=eew['Body']['Earthquake']['Hypocenter']['Depth'] + "km" , inline=False)
        embed.add_field(name="予想震度[震源地付近の推定です]", value=eew['Body']['Intensity']['TextInt'], inline=False)
        await ctx.send(embed=embed)

    @commands.command()
    async def eewop1(self, ctx):
        """地震情報(確認用)"""
        resp = urllib.request.urlopen('http://svir.jp/eew/data.json')
        eew = json.loads(resp.read().decode('utf-8'))
        name = open('eewname.json', 'r')
        name = json.load(name)
        embed=discord.Embed(title="**Head情報**", description=None)
        embed.add_field(name=f"**{name['Head']['Title']}**", value=eew['Head']['Title'], inline=False)
        embed.add_field(name=f"**{name['Head']['DateTime']}**", value=eew['Head']['DateTime'], inline=False)
        embed.add_field(name=f"**{name['Head']['EditorialOffice']}**", value=eew['Head']['EditorialOffice'], inline=False)
        embed.add_field(name=f"**{name['Head']['PublishingOffice']}**", value=eew['Head']['PublishingOffice'], inline=False) 
        embed.add_field(name=f"**{name['Head']['EventID']}**", value=eew['Head']['EventID'], inline=False)
        embed.add_field(name=f"**{name['Head']['Status']}**", value=eew['Head']['Status'], inline=False)
        embed.add_field(name=f"**{name['Head']['Serial']}**", value=eew['Head']['Serial'], inline=False)
        embed.add_field(name=f"**{name['Head']['Version']}**", value=eew['Head']['Version'], inline=False)
        await ctx.send(embed=embed)
 
    @commands.command()
    async def eewop2(self, ctx):
        """地震情報(確認用)"""
        resp = urllib.request.urlopen('http://svir.jp/eew/data.json')
        eew = json.loads(resp.read().decode('utf-8'))
        name = open('eewname.json', 'r')
        name = json.load(name)       
        embed=discord.Embed(title="**Body情報**", description=None)
        embed.add_field(name=f"**{name['Body']['Earthquake']['OriginTime']}**", value=eew['Body']['Earthquake']['OriginTime'])
        embed.add_field(name=f"**{name['Body']['Earthquake']['Hypocenter']['Name']}**", value=eew['Body']['Earthquake']['Hypocenter']['Name'], inline=False) 
        embed.add_field(name=f"**{name['Body']['Earthquake']['Hypocenter']['Code']}**", value=eew['Body']['Earthquake']['Hypocenter']['Code'], inline=False)
        embed.add_field(name=f"**{name['Body']['Earthquake']['Hypocenter']['Lat']}**", value=eew['Body']['Earthquake']['Hypocenter']['Lat'], inline=False)
        embed.add_field(name=f"**{name['Body']['Earthquake']['Hypocenter']['Lon']}**", value=eew['Body']['Earthquake']['Hypocenter']['Lon'], inline=False)
        embed.add_field(name=f"**{name['Body']['Earthquake']['Hypocenter']['Depth']}**", value=eew['Body']['Earthquake']['Hypocenter']['Depth'], inline=False)
        embed.add_field(name=f"**{name['Body']['Earthquake']['Hypocenter']['LandOrSea']}**", value=eew['Body']['Earthquake']['Hypocenter']['LandOrSea'], inline=False)
        embed.add_field(name=f"**{name['Body']['Earthquake']['Accuracy']['Epicenter']}**", value=eew['Body']['Earthquake']['Accuracy']['Epicenter'])
        embed.add_field(name=f"**{name['Body']['Earthquake']['Accuracy']['Depth']}**", value=eew['Body']['Earthquake']['Accuracy']['Depth'], inline=False) 
        embed.add_field(name=f"**{name['Body']['Earthquake']['Accuracy']['MagnitudeCalculation']}**", value=eew['Body']['Earthquake']['Accuracy']['MagnitudeCalculation'], inline=False)
        embed.add_field(name=f"**{name['Body']['Earthquake']['Accuracy']['NumberOfMagnitudeCalculation']}**", value=eew['Body']['Earthquake']['Accuracy']['NumberOfMagnitudeCalculation'], inline=False)
        embed.add_field(name=f"**{name['Body']['Earthquake']['Magnitude']}**", value=eew['Body']['Earthquake']['Magnitude'], inline=False)
        embed.add_field(name=f"**{name['Body']['Intensity']['MaxInt']}**", value=eew['Body']['Intensity']['MaxInt'], inline=False)
        embed.add_field(name=f"**{name['Body']['Intensity']['TextInt']}**", value=eew['Body']['Intensity']['TextInt'], inline=False)
        embed.add_field(name=f"**{name['Body']['Intensity']['ForecastInt']['From']}**", value=eew['Body']['Intensity']['ForecastInt']['From'])
        embed.add_field(name=f"**{name['Body']['Intensity']['ForecastInt']['To']}**", value=eew['Body']['Intensity']['ForecastInt']['To'], inline=False) 
        embed.add_field(name=f"**{name['Body']['Intensity']['Appendix']['MaxIntChange']}**", value=eew['Body']['Intensity']['Appendix']['MaxIntChange'], inline=False)
        embed.add_field(name=f"**{name['Body']['Intensity']['Appendix']['MaxIntChangeReason']}**", value=eew['Body']['Intensity']['Appendix']['MaxIntChangeReason'], inline=False)
        embed.add_field(name=f"**{name['Body']['PLUMFlag']}**", value=eew['Body']['PLUMFlag'], inline=False)
        embed.add_field(name=f"**{name['Body']['WarningFlag']}**", value=eew['Body']['WarningFlag'], inline=False)
        embed.add_field(name=f"**{name['Body']['EndFlag']}**", value=eew['Body']['EndFlag'], inline=False)
        await ctx.send(embed=embed)

    @tasks.loop(seconds=30)
    async def loop(self):
        channels=self.bot.get_all_channels()
        chw=[ch for ch in channels if ch.name == "eew"]
        resp = urllib.request.urlopen('http://svir.jp/eew/data.json')
        eew = json.loads(resp.read().decode('utf-8'))
        eew_code = eew['Head']['EventID']
        if eew_code != self.code:
            embed=discord.Embed(title="**地震情報**", description=eew['Head']['Title'])
            embed.add_field(name="発表時刻", value=eew['Body']['Earthquake']['OriginTime'], inline=False)
            embed.add_field(name="震源地", value=eew['Body']['Earthquake']['Hypocenter']['Name'], inline=False)
            embed.add_field(name="マグニチュード", value=eew['Body']['Earthquake']['Magnitude'], inline=False) 
            embed.add_field(name="深さ", value=eew['Body']['Earthquake']['Hypocenter']['Depth'] + "km" , inline=False)
            embed.add_field(name="予想震度[震源地付近の推定です]", value=eew['Body']['Intensity']['TextInt'], inline=False)
            for chj in chw:   
                await chj.send(embed=embed)
            self.code = eew_code
    

# Bot本体側からコグを読み込む際に呼び出される関数。
def setup(bot):
    bot.add_cog(eew(bot))
