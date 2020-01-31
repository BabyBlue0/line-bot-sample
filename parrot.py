from flask import Flask, request, abort
import os
from random import randint

from linebot import (
    LineBotApi, WebhookHandler
)
from linebot.exceptions import (
    InvalidSignatureError
)
from linebot.models import (
    MessageEvent, TextMessage, TextSendMessage, ImageSendMessage
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

    texts = []
    files = []
    recv_messeges = []
    #text message
    
    
    #image message
    if( event.message.text in  )
    image_url_dir = 'https://arcane-sea-27299.herokuapp.com/static/images/'
    image_url_file = 'haiyoru1.jpg'
    if event.message.text in recv_messeges:
        files = os.listdir( image_url_dir )
        image_url_file = files[ randint( len(files) ) ]
    image_url = image_url_dir + image_url_file
    image_message = ImageSendMessage(
        original_content_url = image_url,
        preview_image_url = image_url
    )

    messages = [
        #TextSendMessage( text=event.message.text ),
        image_message
    ]
    
    line_bot_api.reply_message(
        event.reply_token,
        messages
    )
    

if __name__ == "__main__":
    port = int(os.getenv("PORT"))
    app.run(host="0.0.0.0", port=port)
