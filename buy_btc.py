import ccxt
from dotenv import load_dotenv
import os
import random
import time

load_dotenv()

def buy_btc_market():
    """빗썸에서 7000~12000원 사이 금액으로 랜덤 매수/매도 반복"""

    bithumb = ccxt.bithumb({
        'apiKey': os.getenv('pubkey'),
        'secret': os.getenv('pk'),
    })

    while True:
        try:
            # 시세 조회 및 현재가 확인
            ticker = bithumb.fetch_ticker('BTC/KRW')
            current_price = ticker['last']

            # 매수/매도 랜덤 결정
            side = 'buy' if random.random() < 0.5 else 'sell'

            # 금액 결정 (7,000원 ~ 12,000원)
            target_krw_amount = random.randint(7000, 12000)

            # 목표 수량 계산: (금액) / (현재가)
            target_volume = target_krw_amount / current_price

            # 거래소 규격에 맞게 가격/수량 문자열 포맷 지정
            formatted_price = bithumb.price_to_precision('BTC/KRW', current_price)
            formatted_volume = bithumb.amount_to_precision('BTC/KRW', target_volume)

            # 주문 실행
            print(f"\n[주문 시도] {side.upper()} / 현재가: {formatted_price}원 / 주문 금액: 약 {target_krw_amount}원")

            if side == 'buy':
                # KRW 잔고 확인
                balance = bithumb.fetch_balance()
                if balance['KRW']['free'] < float(formatted_price) * float(formatted_volume):
                    print("  -> [SKIP] 원화 잔고 부족")
                else:
                    order = bithumb.create_limit_buy_order('BTC/KRW', formatted_volume, formatted_price)
                    print(f"  -> 매수 주문 완료: {order['id']}")
            else:
                # BTC 잔고 확인
                balance = bithumb.fetch_balance()
                if balance['BTC']['free'] < float(formatted_volume):
                    print("  -> [SKIP] BTC 잔고 부족")
                else:
                    order = bithumb.create_limit_sell_order('BTC/KRW', formatted_volume, formatted_price)
                    print(f"  -> 매도 주문 완료: {order['id']}")

        except Exception as e:
            print(f"  -> [오류 발생] 한 턴을 건너뜁니다: {e}")

        # 대기: 30초 ~ 30분 랜덤
        wait_time = random.randint(30, 180)
        print(f"  -> {wait_time}초 대기 중...")
        time.sleep(wait_time)

if __name__ == "__main__":
    buy_btc_market()
