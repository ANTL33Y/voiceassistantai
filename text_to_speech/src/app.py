from main import convert_text_to_speech
from flask import Flask, request

app = Flask(__name__)

@app.route('/text-to-speech', methods=['POST'])
def text_to_speech():
    text = request.json['text']
    convert_text_to_speech(text)
    return 'Text converted to speech'

if __name__ == '__main__':
    app.run()
