import os
from dotenv import load_dotenv
from slack_bolt import App

load_dotenv()

app = App(
    token=os.environ.get("SLACK_BOT_TOKEN"),
    signing_secret=os.environ.get("SLACK_SIGNING_SECRET")
)

# Add functionality here
# @app.event("app_home_opened") etc

if __name__ == "__main__":
    app.start(port=int(os.environ.get("PORT", 3000)))
