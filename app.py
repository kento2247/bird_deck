from flask import Flask, render_template, request
import json
import os


json_path = "deck_data.json"
json_data = json.load(open(json_path, 'r')) 
app = Flask(__name__)

@app.route('/')
def index():
    # クエリパラメータからnumを取得
    num = (request.args.get('num'))
    if num is None:
        num = 0
    num=str(num)
    data= json_data[num]
    num_str3 = str(num).zfill(3)
    description = data['description']
    height = data['height']
    weight = data['weight']
    name= data['name']
    img_path = data['img_path']
    img_path=os.path.join('static',"images",img_path+".jpg")
    return render_template('deck.html', 
                           no="No." + num_str3,
                            name=name,
                            description=description,
                            height=height,
                            weight=weight,
                           image_src=img_path)

if __name__ == '__main__':
    app.run(debug=True)
