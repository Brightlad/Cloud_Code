from flask import Flask, render_template, request
from werkzeug import secure_filename
import os
import subprocess

app = Flask(__name__) 


@app.route('/upload')
def upload_page():
   print("Starting program...")
   return render_template('upload.html')
   
@app.route('/uploader', methods = ['GET', 'POST'])
def upload_file():
   if request.method == 'POST':
      f = request.files['file']
      f.save(secure_filename(f.filename))
      
      subprocess.call(['chmod', '755', 'walk.cc'])
      subprocess.call("rm -f ./a.out", shell=True)
      retcode = subprocess.call("/usr/bin/g++ walk.cc", shell = True)
      if retcode:
         print("Failed to compile walk.cc")
         exit

      subprocess.call("rm -f ./output",shell=True)
      retcode = subprocess.call("./walk_test.sh", shell = True)

      print ("Score: " + str(retcode) + " out of 2 correct.")

      print ("*************Original submission*************")

      with open(f.filename,'r') as fs:
         print(fs.read())
      return ("Score: " + str(retcode) + " out of 2 correct." )
    
if __name__ == '__main__':
   print("starting...")
   app.run(host="0.0.0.0")
