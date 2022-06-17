# A simple python script for making an STK-Push using MPESA Daraja API

## Prerequisities
1. Python 3.x
2. Python-dotenv
3. [Daraja account](https://developer.safaricom.co.ke/)

## Steps
1. Setup virtual environment using venv and activate virtualenv. Clone repository to local machine:
    ```
    python -m venv virtualenv_name
    cd virtualenv_name
    source bin/activate
    git clone https://github.com/mugane-dj/mpesa-daraja-stk.git
    ```
2. Install requirements:
    ```
    pip install -r requirements.txt
    ```
3. Register app in MPESA Daraja API and retrieve consumer key and secret. Base64 encode using format below:
    ```
    consumer_key:consumer_secret
    ```
    Link to [Base64 encoder](https://www.base64encode.org/)

4. Add the encoded base64 string, phone number, business short_code, pass_key in `.env` file. Don't space values, variable names or operators in `.env` file. 
    ```
    BASE64=
    BUSINESS_CODE=
    PHONE_NUMBER=
    PASSKEY=bfb279f9aa9bdbcf158e97dd71a467cd2e0c893059b10f78e6b72ada1ed2c919
    ```
    Use the public passkey provided above or password provided in [sandbox](https://developer.safaricom.co.ke/). 
    ### Sample output on success
    ```
    {
        "MerchantRequestID":"3188-42096613-2",
        "CheckoutRequestID":"ws_CO_12052022162913230799334972",
        "ResponseCode": "0",
        "ResponseDescription":"Success. Request accepted for processing",
        "CustomerMessage":"Success. Request accepted for processing"
    }
    ```
   ## API Listener
   URL:https://darajambili.herokuapp.com/
   
   Github Repo:https://github.com/martinmogusu/django-daraja.git
