from flask import Flask,render_template,send_from_directory,url_for,request
import os,re
from werkzeug.utils import secure_filename
from werkzeug.datastructures import  FileStorage


app = Flask(__name__)

app.config['UPLOAD_FOLDER'] = "C:\\Users\\ankit\\Desktop\\IIITD\\DPM\\DPM_Project1\\Input_Images"


@app.route('/')
def index():
    return render_template('index.html')

@app.route("/uploader" , methods=['GET', 'POST'])
def uploader():
    # os.remove('/Users/ankit/Desktop/IIITD/DPM/DPM_Project1/Input_Images/')
    contentImagePath = ""
    styleImagePath = ""
    if request.method=='POST':
        contentFile = request.files['contentImg']
        styleFile = request.files['styleImg']
        if contentFile and styleFile:
            contentFile.save(os.path.join(app.config['UPLOAD_FOLDER'], secure_filename(contentFile.filename)))
            contentImagePath = "http://127.0.0.1:8080/"+contentFile.filename
            styleFile.save(os.path.join(app.config['UPLOAD_FOLDER'], secure_filename(styleFile.filename)))
            styleImagePath = "http://127.0.0.1:8080/"+styleFile.filename    
            print(contentImagePath,styleImagePath)
            return render_template('index.html',contentImagePath = contentImagePath, styleImagePath=styleImagePath,status="Uploaded Successfully..",style=styleFile.filename,content=contentFile.filename)

@app.route("/imageGenerator",methods=['GET','POST'])
def imageGenerator():
    generatedImgPath = "http://127.0.0.1:8080/"+"coinput2.png"
    inputData = dict(request.form)
    print(inputData)
    print(generatedImgPath)
    if request.method=='POST':
        print(generatedImgPath)
        return render_template('index.html',generatedImagePath=generatedImgPath)

if __name__ == '__main__':
    app.run(debug=True)