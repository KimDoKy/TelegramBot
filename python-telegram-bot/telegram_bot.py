import telegram # 텔레그램 모듈을 임포트합니다.
import telegram_token

my_token = telegram_token.telegram_token # 토큰을 변수에 저장합니다.

bot = telegram.Bot(token = my_token) # bot을 선언합니다.

updates = bot.getUpdates() # 업데이트 내역을 받아옵니다.

for u in updates:
    print(u.message)
