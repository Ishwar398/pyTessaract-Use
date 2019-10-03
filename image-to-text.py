import pytesseract
from PIL import Image
from flask import Flask, request, render_template 
import json 
from werkzeug.utils import secure_filename 
import os 
import flask 
import io 


UPLOAD_FOLDER = 'E:/Projects/Image-Reader/uploads' 
ALLOWED_EXTENSIONS = set(['png', 'jpg', 'jpeg']) 
data={}
pytesseract.pytesseract.tesseract_cmd = 'C:/Program Files (x86)/Tesseract-OCR/tesseract.exe'

app = Flask(__name__) 
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER 


@app.route("/",methods=["GET"]) 
def Home(): 
    return render_template('ImageUpload.html') 


@app.route("/ExtractText",methods=["POST"]) 
def ExtractText(): 
    if(request.method == "POST"):    
        file = request.files["image"] 
        if file and allowed_file(file.filename): 
            filename = secure_filename(file.filename) 
            pathToSave = os.path.join(app.config['UPLOAD_FOLDER'], filename) 
            file.save(pathToSave) 

            image_text = pytesseract.image_to_string(Image.open(pathToSave))
            data["text"] = image_text 
            json_data=json.dumps(data) 
            return json_data




def allowed_file(filename): 
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS 
 
 
app.run() 
