from flask import Flask, request, abort
import os

from linebot import (
    LineBotApi, WebhookHandler
)
from linebot.exceptions import (
    InvalidSignatureError
)
from linebot.models import (
    MessageEvent, TextMessage, TextSendMessage,
)

app = Flask(__name__)

YOUR_CHANNEL_ACCESS_TOKEN = os.environ["YOUR_CHANNEL_ACCESS_TOKEN"]
YOUR_CHANNEL_SECRET = os.environ["YOUR_CHANNEL_SECRET"]

line_bot_api = LineBotApi(YOUR_CHANNEL_ACCESS_TOKEN)
handler = WebhookHandler(YOUR_CHANNEL_SECRET)

@app.route("/")
def hello_world():
    return "hello world!"

@app.route("/callback", methods=['POST'])
def callback():
    # get X-Line-Signature header value
    signature = request.headers['X-Line-Signature']

    # get request body as text
    body = request.get_data(as_text=True)
    app.logger.info("Request body: " + body)

    # handle webhook body
    try:
        handler.handle(body, signature)
    except InvalidSignatureError:
        abort(400)

    return 'OK'

@handler.add(MessageEvent, message=TextMessage)
def handle_message(event):

    image_url = 'https://arcane-sea-27299.herokuapp.com/static/images/sample1.jpg'
    image_message = ImageSendMessage(
            original_content_url=image_url,
            preview_image_url=image_url
    )

    #text message
    messages = [
            #TextSendMessage( text=event.message.text ),
            TextSendMessage( text="大事なことなので繰り返すぴょん\n" + event.message.text + "ぴょん" ),
            image_message
    ]
    
    line_bot_api.reply_message(
        event.reply_token,
        messages
    )
"""
    image_url = 'https://arcane-sea-27299.herokuapp.com/static/images/sample1.jpg'
    image_message = ImageSendMessage(
            original_content_url=image_url,
            preview_image_url=image_url
    )

    line_bot_api.reply_message( event.reply_token, image_message )
"""


if __name__ == "__main__":
    port = int(os.getenv("PORT"))
    app.run(host="0.0.0.0", port=port)
