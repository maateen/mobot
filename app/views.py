import requests, aiml, os
from app import app
from flask import abort, Flask, request, render_template

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/webhook/<string:secret_key>/', methods=['GET', 'POST'])
def webhook(secret_key):
    if secret_key == app.config['SECRET_KEY']:
        if request.method == 'GET':
            if request.args['hub.verify_token'] == app.config['FB_VERIFY_TOKEN']:
                return request.args['hub.challenge']
            else:
                abort(401)
        elif request.method == 'POST':
            data = request.json
            try:
                checker = data['entry'][0]['messaging'][0]['message']['is_echo']
                return 'reply triggered'
            except KeyError:
                try:
                    message = data['entry'][0]['messaging'][0]['message']['text']
                    sender = data['entry'][0]['messaging'][0]['sender']['id']
                    # Create the kernel and learn
                    kernel = aiml.Kernel()
                    kernel.learn('data/std-startup.xml')
                    if os.path.isfile("mobot_brain.brn"):
                        kernel.bootstrap(brainFile = "mobot_brain.brn")
                    else:
                        kernel.bootstrap(learnFiles = 'data/std-startup.xml', commands = "load aiml b")
                        kernel.saveBrain("mobot_brain.brn")
                    reply = kernel.respond(message, sender)
                    data = {"recipient": {"id": sender}, "message": {"text": reply}}
                    response = requests.post("https://graph.facebook.com/v2.6/me/messages?access_token=" + app.config['FB_ACCESS_TOKEN'], json=data)
                    print(response.content)
                except KeyError:
                    pass
                return "ok"
    else:
        abort(401)