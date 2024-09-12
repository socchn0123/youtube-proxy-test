from flask import Flask, render_template_string, request
from pytube import YouTube

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    video_url = None
    if request.method == 'POST':
        video_id = request.form['video_id']
        video_url = f'https://www.youtube.com/embed/{video_id}'
    return render_template_string('''
        <!doctype html>
        <html lang="en">
          <head>
            <meta charset="utf-8">
            <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">
            <title>YouTube Video Embed</title>
          </head>
          <body>
            <div class="container">
              <h1 class="mt-5">YouTube Video Embed</h1>
              <form method="post">
                <div class="form-group">
                  <label for="video_id">YouTube Video ID</label>
                  <input type="text" class="form-control" id="video_id" name="video_id" placeholder="Enter YouTube Video ID">
                </div>
                <button type="submit" class="btn btn-primary">Embed Video</button>
              </form>
              {% if video_url %}
              <div class="mt-5">
                <iframe width="720" height="405" src="{{ video_url }}" frameborder="0" allowfullscreen></iframe>
              </div>
              {% endif %}
            </div>
          </body>
        </html>
    ''', video_url=video_url)

if __name__ == '__main__':
    app.run(debug=True)
