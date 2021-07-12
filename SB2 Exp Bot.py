import discord
import os

client = discord.Client()

@client.event
async def on_ready():
    print("봇이 실행되었습니다.")
    await client.change_presence(status=discord.Status.online, activity=discord.Game("SwordBurst II 플레이 중"))

@client.event
async def on_message(message):
    str = message.content.split(' ', maxsplit=2)
    print(message.content)
    print(str)
    print(type(message.content))
    if len(str) == 2:
        print("message's length = 2")
        if str[0] == '-Lv':
            print("message has -Lv")
            if str[1].isdigit():
                print("can [str->int]")
                Lv = int(str[1])
                if Lv <= 250:
                    if Lv > 0:
                        if Lv % 1 == 0:
                            HP = Lv*55 + 100
                            EXP = 3*Lv * (Lv+1) + 1
                            TotalExp = 1
                            for i in range(Lv):
                                if i > 0:
                                    TotalExp = TotalExp + (3*i * (i+1) + 1)
                                    print(TotalExp)
                            
                            TotalExp = TotalExp - 1

                        await message.channel.send ("[Lv {}]\nHP : {}\nNeed Exp : {}\nTotal Exp : {}".format(Lv, HP, EXP, TotalExp))
                       
    
          
        
        
        



access_token = os.environ["BOT_TOKEN"]
client.run(access_token)
