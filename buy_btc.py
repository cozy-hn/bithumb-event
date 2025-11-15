import ccxt
from dotenv import load_dotenv
import os

load_dotenv()

def buy_btc_market():
    """빗썸에서 BTC 0.0001개 시장가 매수"""

    bithumb = ccxt.bithumb({
        'apiKey': os.getenv('pubkey'),
        'secret': os.getenv('pk'),
    })

    try:
        order = bithumb.create_market_buy_order('BTC/KRW', 0.0001)
        print("매수 주문 완료!")
        print(f"응답: {order}")

    except Exception as e:
        print(f"오류 발생: {e}")
        raise

    finally:
        print("\n프로그램을 종료합니다.")

if __name__ == "__main__":
    buy_btc_market()
