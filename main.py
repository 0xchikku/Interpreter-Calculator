import discord
import os
from discord.ext import commands
from keep_alive import keep_alive

client = discord.Client()

@client.event
async def on_message(message):
  if message.author == client.user:
    return
  
  msg = message.content

  if msg.startswith("$ic"):
    result = 0
    ldic=locals()
    
    try:
      exec("result+=" + msg.split("$ic ", 1)[1], globals(),ldic)
      result=ldic["result"]
      print(result)
      await message.channel.send("Result is " + str(result))
    except:
      await message.channel.send("Invalid Expression")


keep_alive()
client.run(os.getenv("TOKEN"))