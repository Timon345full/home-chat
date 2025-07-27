from flask import Flask, render_template, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)  # если фронтенд и бэкенд на одном сервере, можно убрать

# Храним сообщения в памяти (список словарей)
messages = [
    # {'id': 1, 'fromMe': False, 'text': 'Привет всем! Как дела?'},
    # {'id': 2, 'fromMe': False, 'text': 'Всё отлично, спасибо! А у вас?'},
    # {'id': 3, 'fromMe': False, 'text': 'Тоже хорошо, рад быть здесь!'},
    
]
next_id = 4

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/api/messages', methods=['GET'])
def get_messages():
    return jsonify(messages)

@app.route('/api/messages', methods=['POST'])
def post_message():
    global next_id
    data = request.get_json()
    text = data.get('text', '').strip()
    if not text:
        return jsonify({'error': 'Пустое сообщение'}), 400
    # Для простоты считаем, что все POST — от "вас" (fromMe=True)
    msg = {'id': next_id, 'fromMe': True, 'text': text}
    messages.append(msg)
    next_id += 1
    return jsonify(msg), 201

if __name__ == '__main__':
    app.run(host='ip adress', port=5000, debug=True)


