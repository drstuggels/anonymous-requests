# anonymous-requests

## setup

***Tor setup:***
```bash
# install tor
brew install tor
brew services start tor

# create and copy a hash for your tor password
tor --hash-password Password1234
```

```bash
# change tor settings
nano /usr/local/etc/tor/torrc

# put this into the file (modify the_password_hash_you_copied):
ControlPort 9051
HashedControlPassword the_password_hash_you_copied
CookieAuthentication 1
```

***Python setup:***
```bash
virtualenv venv
source venv/bin/activate
pip install -r requirements.txt
```
Create `.env` and make it look like this:
```
TOR_PASSWORD=Password1234
```

## running
```
python main.py
```