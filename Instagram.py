from instabot import Bot

def instas(username2, password2,caption2, instaimage):
    bot = Bot()
    bot.login(username=username2,password=password2)
    bot.upload_photo(instaimage, caption=caption2)
