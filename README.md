#### **Create the virtual environment**
`py -m venv env`

#### **Install libraries**
`pip install -r requirements.txt`

---
### Google Cloud Key Management Service
#### **1. Install Google Cloud CLI**
https://cloud.google.com/sdk/docs/install?hl=en

#### **2. If not already done, run this to sign it to initialize `gcloud`**
`gcloud init`

#### **3. Run this to save the credentials locally**
`gcloud auth application-default login`

#### **4. Run this to set the quota project** (not sure if necessary)
`gcloud auth application-default set-quota-project uma-security-lab-kms`

#### **5. Make sure you have a `.env` file with the credentials stored locally**

Now you should be able to access the Google Cloud key management service!
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
### Install OpenSSL
#### Download OpenSSL from here: https://slproweb.com/products/Win32OpenSSL.html
#### Create SSL certificate: openssl req -x509 -newkey rsa:4096 -nodes -out cert.pem -keyout key.pem -days 365