import requests

# URL vašeho webhooku
webhook_url = "https://ssinfis.webhook.office.com/webhookb2/e61733c4-95f6-4a89-8e83-a583344b2b64@1543f07f-30f9-407a-9eb5-8a7aec418fff/IncomingWebhook/7f269c78c2304a378376fa694a5665a3/151b2689-cd81-496b-be0b-090a31ae6b56/V2SXoRlyw0-IVvB-QQKtcMdZgWKRVOiQzq5TTuZ_8YW7M1"

# Zpráva, kterou chcete poslat
data = {
    "text": "Ahoj, toto je zpráva odeslaná z Pythonu do Teams!"
}

# Odeslání zprávy pomocí POST požadavku
response = requests.post(webhook_url, json=data)

# Kontrola, zda se zpráva úspěšně odeslala
if response.status_code == 200:
    print("Zpráva úspěšně odeslána do Teams!")
else:
    print(f"Nastala chyba: {response.status_code}, {response.text}")
