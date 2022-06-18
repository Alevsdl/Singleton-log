import firebase_admin
from firebase_admin import credentials
from firebase_admin import storage
from cloud import Cloud
from datetime import datetime


class Firebase(Cloud):

    def connection(self):
        cred = credentials.Certificate('serviceAccountKey.json')
        firebase_admin.initialize_app(cred, {
            'storageBucket': 'laboratorio3-f27ed.appspot.com'
        })

    def write(self, filename: str, text: str):
        f = open(filename, 'a')
        f.write('\n' + datetime.today().strftime('%Y-%m-%d %H:%M') + ' ' + text)
        f.close()
        return

    def upload(self, filename: str):
        bucket = storage.bucket()
        blob = bucket.blob(filename)
        blob.upload_from_filename(filename)
        blob.make_public()
        print('Link: ', blob.public_url)
