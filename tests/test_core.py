from pygram_bot import Bot

def test_bot_init():
    bot = Bot("123TOKEN")
    assert bot.token == "123TOKEN"
