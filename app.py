from flask import Flask,render_template,send_from_directory,url_for,request
import os,re
from werkzeug.utils import secure_filename
from werkzeug.datastructures import  FileStorage
# from flask_share import Share



app = Flask(__name__)
# share = Share(app)
app.config['UPLOAD_FOLDER'] = "C:\\Users\\ankit\\Desktop\\IIITD\\DPM\\DPM_Project1\\Input_Images"

@app.route('/')
def index():
    return render_template('index.html')

@app.route("/uploader" , methods=['GET', 'POST'])
def uploader():
    contentImagePath = ""
    global content_Image_Path
    global contentImageName 
    if request.method=='POST':
        contentFile = request.files['contentImg']
        if contentFile :
            contentFile.save(os.path.join(app.config['UPLOAD_FOLDER'], secure_filename(contentFile.filename)))
            contentImagePath = "static/"+contentFile.filename
            content_Image_Path = "static/"+contentFile.filename
            contentImageName = contentFile.filename
            # print("url for content image path = ",url_for(contentImageName))
            print(url_for('static', filename = 'contentImageName'))
            return render_template('index.html',contentImagePath = contentImagePath,status="Uploaded Successfully..",content=contentFile.filename) #, styleImagePath=styleImagePath ,style=styleFile.filename

@app.route("/imageGenerator",methods=['GET','POST'])
def imageGenerator():
    generatedImgPath = "static/"+"coinput2.png"
    inputData = dict(request.form)
    if request.method=='POST':
        return render_template('index.html',generatedImagePath=generatedImgPath, contentImagePath = content_Image_Path,content=contentImageName)

if __name__ == '__main__':
    app.run(debug=True)