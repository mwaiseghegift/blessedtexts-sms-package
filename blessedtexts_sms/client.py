import requests

class BlessedTextsClient:
    BASE_URL = "https://sms.blessedtexts.com/api/sms/v1"

    def __init__(self, api_key):
        """
        Initialize the API client with the API key.
        """
        if not api_key:
            raise ValueError("API key is required.")
        self.api_key = api_key

    def send_sms(self, sender_id, message, phone, attachment=None):
        """
        Send an SMS using the BlessedTexts API.

        :param sender_id: Sender ID assigned to you.
        :param message: Message content.
        :param phone: Recipient phone number(s) (comma-separated if multiple).
        :param attachment: Optional file attachment.
        :return: API response as a dictionary.
        """
        url = f"{self.BASE_URL}/sendsms"
        data = {
            "api_key": self.api_key,
            "sender_id": sender_id,
            "message": message,
            "phone": phone
        }
        files = {"attachment": open(attachment, "rb")} if attachment else None

        try:
            response = requests.post(url, data=data, files=files)
            response.raise_for_status()  # Raises an error for HTTP failure
            return response.json()
        except requests.exceptions.RequestException as e:
            return {"error": str(e)}

    def get_credit_balance(self):
        """
        Fetch account credit balance.

        :return: Account balance as a dictionary.
        """
        url = f"{self.BASE_URL}/credit-balance"
        params = {"api_key": self.api_key}

        try:
            response = requests.get(url, params=params)
            response.raise_for_status()
            return response.json()
        except requests.exceptions.RequestException as e:
            return {"error": str(e)}
