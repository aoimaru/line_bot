from flask import Flask, request, abort

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

line_bot_api = LineBotApi('IAN+zETmf4zuIq43WMlnzjNapYo26WWMLt1yxljuZLt389l9uOSZ9Wd0tmj9gINMmNqm3J+ea/n11vJbGZ94akuFCeDH0qmMGNJtT524pGDnk/tjokXBmuhr0rCMgqKvjVTxR8zdReWh6Y1rNZRFpgdB04t89/1O/w1cDnyilFU=')
handler = WebhookHandler('19969dde5768eaa81318843ac8b62ade')


@app.route("/")
def test() -> str:
    return "OK"



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
        print("Invalid signature. Please check your channel access token/channel secret.")
        abort(400)

    return 'OK'


@handler.add(MessageEvent, message=TextMessage)
def handle_message(event):
    line_bot_api.reply_message(
        event.reply_token,
        TextSendMessage(text=f"碧海さんは,{event.message.text}と言いました."))


if __name__ == "__main__":
    app.run()