from flask import Flask, jsonify
import handler

app = Flask(__name__)

driver = {'driver': 0}
musicList = ['meditation', 'work', 'high', 'sleep', 'relaxing', 'focus', 'study', 'dream']
@app.route("/music/<musicType>")
def hello(musicType):
    if musicType not in musicList:
        return jsonify({'status': '404 not found'})

    if driver['driver'] != 0:
        try:
            driver['driver'].close()
        except:
            print("already stopped")
    baseUrl = 'https://mubert.com/channels'
    url = '{baseUrl}/{musicType}-music'.format(baseUrl = baseUrl, musicType = musicType)
    print url
    driver['driver'] = handler.openurl_function(url = url)
    return jsonify({'status': 'playing...'})


if __name__ == "__main__":
    app.run(host = '0.0.0.0', port = 7001)
