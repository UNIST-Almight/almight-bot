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

#print(app.client.auth_test())

# when bot mentioned, activate
@app.event("app_mention")
def event_test(body, say, message, logger, client, token):
    user = body["event"]["user"]
    # payload = {'token': token, 'user': user}
    # r = requests.get('https://slack.com/api/users.info', params=payload)
    # print(r)
    # print(client.users_identity(token))
    
    #user = message['user']
    say(f"안녕하세요, <@{user}>!")

# when someone chat in slack channel, ativate
@app.event("message")
def handle_message_events(body, say, message, logger):
    logger.info(body)
    # print(type(body))
    # print(body.keys())
    #print(message)
    say("This is a message")

# ? why cannot avtivate..
@app.message(":wave:")
def say_hello(message, say):
    user = message['user']
    say(f"Hi there, <@{user}>!")

# this part reset previous event
# if this isn't, bot eternally repeat last event until get new event
@app.event("app_home_opened")
def update_home_tab(client, event, logger):
    try:
        # views.publish is the method that your app uses to push a view to the Home tab
        client.views_publish(
            # the user that opened your app's app home
            user_id=event["user"],
            # the view object that appears in the app home
        )

    except Exception as e:
        logger.error(f"Error publishing home tab: {e}")

if __name__ == "__main__":
    app.start(port=int(os.environ.get("PORT", 5000)))

# this is embed(like?) message format
# text = {
# 	"blocks": [
# 		{
# 			"type": "section",
# 			"text": {
# 				"type": "mrkdwn",
# 				"text": "Danny Torrence left the following review for your property:"
# 			}
# 		},
# 		{
# 			"type": "section",
# 			"block_id": "section567",
# 			"text": {
# 				"type": "mrkdwn",
# 				"text": "<https://example.com|Overlook Hotel> \n :star: \n Doors had too many axe holes, guest in room 237 was far too rowdy, whole place felt stuck in the 1920s."
# 			},
# 			"accessory": {
# 				"type": "image",
# 				"image_url": "https://is5-ssl.mzstatic.com/image/thumb/Purple3/v4/d3/72/5c/d3725c8f-c642-5d69-1904-aa36e4297885/source/256x256bb.jpg",
# 				"alt_text": "Haunted hotel image"
# 			}
# 		},
# 		{
# 			"type": "section",
# 			"block_id": "section789",
# 			"fields": [
# 				{
# 					"type": "mrkdwn",
# 					"text": "*Average Rating*\n1.0"
# 				}
# 			]
# 		}
# 	]
# }