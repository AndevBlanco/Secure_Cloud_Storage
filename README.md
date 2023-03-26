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
`gcloud auth application-default set-quota-project security-lab-kms`

#### **5. Make sure you have a `.env` file with the credentials stored locally**

Now you should be able to access the Google Cloud key management service!
