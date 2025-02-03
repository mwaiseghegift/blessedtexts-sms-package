# BlessedTexts SMS Python SDK

This is a Python package to interact with the BlessedTexts SMS API.

## Installation

```sh
pip install blessedtexts_sms
```

## Usage

```python
from blessedtexts_sms import BlessedTextsClient

# Initialize client
api_key = "YOUR_API_KEY"
client = BlessedTextsClient(api_key)

# Send SMS
response = client.send_sms(sender_id="23107", message="Hello!", phone="254721XXXXXX")
print(response)

# Check credit balance
balance = client.get_credit_balance()
print(balance)
```

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
