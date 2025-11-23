# Bithumb Event - BTC 자동 거래

빗썸에서 자동 거래하는 프로그램

15,000원 ~ 18,000원 사이의 금액으로 BTC를 랜덤 매수/매도 합니다.
잔고가 부족하다면 거래를 스킵하며, 각 거래 사이 대기 시간은 30초 ~ 3분 사이로 랜덤 적용됩니다.

## 이벤트 참여

[빗썸 이벤트 페이지](https://www.bithumb.com/react/feed/event/143) - 제발 이벤트 신청 누르세요

## 사용 방법

### 0. uv 설치

이 프로젝트는 의존성 관리를 **uv**로만 수행합니다. uv가 없다면 [설치 가이드](https://docs.astral.sh/uv/#installation)를 참고하거나 다음 중 하나를 사용하세요.

```bash
# macOS / Linux
curl -LsSf https://astral.sh/uv/install.sh | sh

# Windows (PowerShell)
powershell -ExecutionPolicy Bypass -c "irm https://astral.sh/uv/install.ps1 | iex"
```

### 1. API 키 발급

**중요: API 1.0에서 키를 발급받아야 합니다. API 2.0은 지원하지 않습니다.**

1. [빗썸](https://www.bithumb.com) 로그인
2. 마이페이지 > API 관리 > **API 1.0** 선택
3. API 키 발급
   - 자산조회 권한 체크
   - 거래 권한 체크
   - IP 화이트리스트 설정 (현재 IP 추가)
4. Connect Key, Secret Key 복사
5. API 키 활성화 버튼 클릭

### 2. 설정

```bash
# .env 파일 생성
cp .env.example .env

# .env 파일 열어서 API 키 입력
# pk=YOUR_SECRET_KEY
# pubkey=YOUR_PUBLIC_KEY
```

### 3. 실행

```bash
# 의존성 설치 (첫 실행 또는 의존성 변경 시)
uv sync

# 프로그램 실행
uv run python buy_btc.py
```

## 주의사항

- **API 1.0 필수**: API 2.0 키는 작동하지 않습니다
- **API 키 활성화**: 발급 후 반드시 활성화 버튼을 눌러야 합니다
- 실제 거래가 실행됩니다
- API 키는 절대 공유하지 마세요
