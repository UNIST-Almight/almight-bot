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

- 의존성 관리는 pipenv를 사용한다.
- VS Code가 pipenv 환경을 감지하지 못하는 경우, 커맨드 팔레트(Ctrl/Cmd + Shift + P)에서 "Python: Select Interpreter" 명령을 실행한다. almight-bot 이름으로 된 pipenv 환경을 선택한다.
- 비밀 키, 개인정보 등 공개되면 안 되는 정보는 .env 파일에 저장하고 dotenv 라이브러리로 불러온다.

## 레퍼런스

- [Slack Bolt 사용법](https://api.slack.com/start/building/bolt-python)
- [Slack Bolt 레퍼런스](https://slack.dev/bolt-python/concepts)
