from flask import Flask, render_template, request, redirect

app = Flask(__name__)

@app.route('/')
def index():
 # return render_template('index.html')
 return render_template('NYS2.html')

@app.route('/about')
def about():
  return render_template('about.html')

if __name__ == '__main__':
  app.run(port=33507)


# NYS data https://health.data.ny.gov/resource/xdss-u53e.json