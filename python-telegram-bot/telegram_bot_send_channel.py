import telegram
import telegram_token

my_token = telegram_token.telegram_token

bot = telegram.Bot(token = my_token)

bot.sendMessage(chat_id = '@fourss', text="저는 봇입니다.")
