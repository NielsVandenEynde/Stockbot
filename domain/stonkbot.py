import os, discord
import user
import userRepo
from discord.ext import commands
import stock
import helperFunctions
from decouple import config



bot = commands.Bot(command_prefix='$')
TOKEN=config("KEY")
repo=userRepo.userRepo()

@bot.event
async def on_ready():
    print('{bot.user} has connected to Discord!')

@bot.command(name="price", help="gives the price of the ticker")
async def prijs(ctx, ticker):
    response = get_stock_price(ticker)
    await ctx.send(response)

@bot.command(name="buy", help="adds a stock to your account. args= ticker and amount")
async def addstock(ctx, ticker, amount,price=None):
    if price==None:
        price=helperFunctions.get_stock_price(ticker)
    if str(ctx.message.author.id) in repo.users:
        repo.users[str(ctx.message.author.id)].addStock(ticker, int(amount),price)
        repo.save_users()
        await ctx.send('added '+str(amount)+ ' of ' +ticker)
        

@bot.command(name="portfolio",aliases=['pf'], help="gives portfolio overview")
async def portfolio(ctx):
    embed = discord.Embed(title=f"__**Portfolio overview:**__", color=0x03f8fc)
    
    for stock in repo.users[str(ctx.message.author.id)].stocks:
        price=helperFunctions.get_stock_price(stock.ticker)
        euroPrice=helperFunctions.convertToEuro(price)
        embed.add_field(name=f'**{stock.ticker.upper()}**', value=f'> Amount: {stock.amount}\n> Cost base: ${stock.costbase}\n> Current price: ${price}\n> Current value: €{round(euroPrice*stock.amount,2)}',inline=False)
    embed.set_footer(text=f'**Total value: €{repo.users[str(ctx.message.author.id)].getTotalValue()}**')
    await ctx.send(embed=embed)

@bot.command(name="sell", help="sells some of the stock")
async def sell(ctx, ticker, amount):
    if str(ctx.message.author.id) in repo.users:
        code=repo.users[str(ctx.message.author.id)].sellStock(ticker, int(amount))
        repo.save_users()
        await ctx.send('sold {} of {} shares'.format(amount,ticker) if code==0 else "you don't have any shares to sell!")
        

@bot.command(name="register", help="makes a new stonk account")
async def register(ctx):
    print(ctx.message.author.name)
    code=repo.add_user(ctx.message.author.id)
    print('exit code ' + str(code))
    if code == 0:
        await ctx.send('You are registered '+ctx.message.author.name+'!')
    elif code == 1:
        await ctx.send('You are already registered')

@bot.command(name="exit", help="exits the bot")
async def exit(ctx):
    await bot.logout()



bot.run(TOKEN)