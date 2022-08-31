from flask import Flask, render_template,url_for,redirect

app = Flask(__name__)
  
file_dict = {"Brisbane Flood":"https://storage.googleapis.com/s2141737_cw1/brisbane_flood.jpg", 
"De San Juan":"https://storage.googleapis.com/s2141737_cw1/de_san_juan.jpg",
"Pasha":"https://storage.googleapis.com/s2141737_cw1/pasha.jpg"}

all_keys = list(file_dict.keys())

@app.route("/")
def index():
    return redirect(url_for('hello'))


@app.route('/ancientimage/')
def hello():
    return render_template('index.html' , result= file_dict)


@app.route('/ancientimage/<int:img_no>')
def getFirstFile(img_no):
    if(1 <= img_no <= 3):
        img_no -= 1
        random_pix= file_dict[all_keys[img_no]]
        return render_template('singleImage.html', random_pix=random_pix, alt_name =all_keys[img_no])
    else:
        return '<h2>Please enter the right url</h2>'
    

if __name__ == '__main__':
    app.run(host='127.0.0.1', port=8080, debug=True)