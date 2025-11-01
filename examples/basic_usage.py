from pygram_bot import Bot

bot = Bot("TOKEN")
response = bot.send_message(123456789, "Salom, dunyo!")
print(response)
