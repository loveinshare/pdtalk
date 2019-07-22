
import time
import os
from threading import Lock
from flask import Flask, render_template
from flask_socketio import SocketIO, emit, join_room
from flask import Flask, jsonify, request
from wxpy import *
from queue import Queue
import threading
from flask_cors import CORS
import traceback
async_mode = None
app = Flask(__name__, static_folder='../dist',
            static_url_path='', template_folder='../dist')
app.config['SECRET_KEY'] = 'secret!'
socketio = SocketIO(app, async_mode=async_mode)
thread = None
thread_lock = Lock()
CORS(app)



@app.route('/')
def index():
    return render_template('index.html', async_mode=socketio.async_mode)



@socketio.on('connect')  # , namespace='/test')
def Onconnect():
    room = request.sid
    print("connected sid================================", room)
    if room in User:
        User.remove(room)
        time.sleep(2)
    User.append(room)
    join_room(room)
#     print("data:",data.get("user"))
    user[room] = {"queue": Queue()}
    print(user)
#     socketio.start_background_task(startBot,{"QRcallback":QRcallback,"workPath":data.get("user")})
    socketio.start_background_task(
        startBot, QRcallback=QRcallback, workPath=room, inputQ=user[room]["queue"], room=room)



@socketio.on('disconnect')
def test_disconnect():
    User.remove(request.sid)
    print('Client disconnected')




if __name__ == '__main__':
    socketio.run(app, debug=True, host="0.0.0.0", port=80)
