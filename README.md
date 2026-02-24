# openfortivpn password + otp

## Install 
### ssl - https://github.com/adrienverge/openfortivpn
### ipsec - https://strongswan.org/
    ~ pip install - r requirements.txt
## Create
    ~ touch config.json

```json
{
    "ssl": {
        "host": ""
        "port": "",
        "user": "",
        "password": "",
        "otp": "otpauth://",
        "trusted-cert": ""
    },
    "ipsec": {
        "host": "",
        "user": "",
        "psk": "",
        "password": "",
        "otp": "otpauth://"
    }
}
```
## Run
    ~ python main.py
