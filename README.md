#### **Create the virtual environment**
`py -m venv env`

#### **Install libraries**
`pip install -r requirements.txt`

---

#### **1. If not already done, create a key in Amazon KMS. Create credentials to use the service.
Set the credentials information in a file called `credentials.json` and fill this information:
```json
{
    "ACCESS_KEY_ID": "your_access_key_id",
    "SECRET_ACCESS_KEY": "your_secret_access_key",
    "REGION_NAME": "your_region_name",
    "KEY_ID":"your_key_id"
}
```

Now you should be able to access the Amazon KMS service!
### **Run client**
##### **Encrypt all files with Master Key**
`python app.py -em *`

##### **Encrypt a file with Master Key**
`python app.py -em [path]`

##### **Encrypt all files using Data Encryption Key and Master Key and password**
`python app.py -ed *`

##### **Encrypt a file using Data Encryption Key and Master Key and password**
`python app.py -ed [path]`

##### **Decrypt a file**
`python app.py -d [path]`

---

### **Run server**
### Install OpenSSL
#### Download OpenSSL from here: https://slproweb.com/products/Win32OpenSSL.html
#### Create SSL certificate: openssl req -x509 -newkey rsa:4096 -nodes -out cert.pem -keyout key.pem -days 365

### **Run server:**
`python pyfiledrop.py --chunk-size [chunk-size]`