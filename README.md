# Almight Bot

## 실행 방법

1. `pipenv install`

2. 프로젝트 루트에 .env 파일을 만들고 다음 정보를 채워넣는다. ([참고](https://api.slack.com/start/building/bolt-python#credentials))

    ```
    SLACK_BOT_TOKEN=...
    SLACK_SIGNING_SECRET=...
    ```

3. `pipenv run dev`

## 개발

- 패키지 설치는 pipenv를 사용한다.
- 비밀 키, 개인정보 등 공개되면 안 되는 정보는 .env 파일에 저장하고 dotenv 라이브러리로 불러온다.

## 레퍼런스

- [Slack Bolt 사용법](https://api.slack.com/start/building/bolt-python)
- [Slack Bolt 레퍼런스](https://slack.dev/bolt-python/concepts)
