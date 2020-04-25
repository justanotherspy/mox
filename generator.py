#!/usr/bin/env python3

# import qrcode
# import requests
# import boto3
# import urllib.parse
import uuid
import json
import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import pyqtSlot

access_key = ""
secret_key = ""
api_key = ""
with open('creds.json') as creds_file:
    data = json.load(creds_file)
    access_key = data['aws_access_key_id']
    secret_key = data['aws_secret_access_key']
    api_key = data['api_key']

def main():

    id = str(uuid.uuid4())[:8]

    app = QApplication(sys.argv)
    widget = QWidget()

    textLabel = QLabel(widget)
    textLabel.setText("Hello World!")
    textLabel.move(110,85)

    widget.setGeometry(50,50,320,200)
    widget.setWindowTitle("PyQt5 Example")
    widget.show()
    sys.exit(app.exec_())

    # name = input("Name of doll: ")
    # encoded_name = urllib.parse.quote_plus(name)
    # description = input("Enter a description (not long): ")
    # encoded_description = urllib.parse.quote_plus(description)

    # try:
    #     r = requests.get("https://y5p8e6kmgf.execute-api.us-east-1.amazonaws.com/prod/generate?id=" + id + "&name=" + encoded_name + "&description=" + encoded_description)
    #     img = qrcode.make('https://verify.moxandlouise.com/#'+id)
    #     img.save("./qrcodes/" + name + '.png')
    #     bucketName = "verify.moxandlouise.com"
    #     s3 = boto3.client('s3', aws_access_key_id=access_key, aws_secret_access_key=secret_key)
    #     key = "./images/" + name + ".jpeg"
    #     output = "images/" + name + ".jpeg"
    #     s3.upload_file(key, bucketName, output, ExtraArgs={'ACL':'public-read'})
    # except Exception as e:
    #     print(e)
        
if __name__ == '__main__':
    main()