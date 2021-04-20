from flask import Flask, request, jsonify, render_template, \
    make_response
from paster import paste, get_content
import requests as req

app = Flask(__name__)
errors = {'405': 'Get method is not allowed !'}

@app.route('/api/documents')
def newdocument():
    method = request.method
    if method == 'POST':
        content = request.form['content']
        result = paste(content)
        url = '127.0.0.1:5000/'+result
        key = result
        return jsonify({'ok': True, 'result': [{'key': key, 'url': url}]})
    else:
        return jsonify({'ok': False, 'result': [{'err_code': 405, 'error': errors['405']}]})

    
@app.route('/raw/<key>')
def viewraw(key):
    if '.' in key:
        ext = key.split('.')[1]
        key = key.split('.')[0]
    else:
        ext = 'txt'
    response = make_response(get_content(key), 200)
    response.mimetype = "text/plain"
    return response

@app.route('/<key>')
def view(key):
    if '.' in key:
        ext = key.split('.')[1]
        key = key.split('.')[0]
    else:
        ext = 'txt'
    return render_template('viewer.html', row=False, code=get_content(key), extension=ext)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80)
