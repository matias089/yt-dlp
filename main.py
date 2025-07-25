from flask import Flask, render_template, request
import subprocess

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/download', methods=['POST'])
def download():
    url = request.form['url']
    args = ['yt-dlp', url]

    if request.form['playlist_items']:
        args += ['--playlist-items', request.form['playlist_items']]
    if request.form['dateafter']:
        args += ['--dateafter', request.form['dateafter']]
    if request.form['datebefore']:
        args += ['--datebefore', request.form['datebefore']]
    if request.form['min_filesize']:
        args += ['--min-filesize', request.form['min_filesize']]
    if request.form['max_filesize']:
        args += ['--max-filesize', request.form['max_filesize']]
    if request.form['max_downloads']:
        args += ['--max-downloads', request.form['max_downloads']]
    if 'playlist_random' in request.form:
        args += ['--playlist-random']
    if 'yes_playlist' in request.form:
        args += ['--yes-playlist']
    if 'no_playlist' in request.form:
        args += ['--no-playlist']

    print("Ejecutando:", args)
    result = subprocess.run(args, capture_output=True, text=True)

    return f"<pre>{result.stdout}</pre><pre>{result.stderr}</pre>"

if __name__ == '__main__':
    app.run(debug=True)
