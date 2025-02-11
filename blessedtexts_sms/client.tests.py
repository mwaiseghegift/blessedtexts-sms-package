import unittest
from unittest.mock import patch, mock_open
from blessedtexts_sms.client import BlessedTextsClient
import requests

class TestBlessedTextsClient(unittest.TestCase):

    def setUp(self):
        self.api_key = "test_api_key"
        self.client = BlessedTextsClient(self.api_key)

    @patch("requests.post")
    def test_send_sms_success(self, mock_post):
        mock_response = unittest.mock.Mock()
        mock_response.json.return_value = {"status": "success"}
        mock_response.raise_for_status = unittest.mock.Mock()
        mock_post.return_value = mock_response

        response = self.client.send_sms("sender_id", "Hello", "1234567890")
        self.assertEqual(response, {"status": "success"})
        mock_post.assert_called_once()

    @patch("requests.post")
    def test_send_sms_failure(self, mock_post):
        mock_response = unittest.mock.Mock()
        mock_response.raise_for_status.side_effect = requests.exceptions.HTTPError("Error")
        mock_post.return_value = mock_response

        response = self.client.send_sms("sender_id", "Hello", "1234567890")
        self.assertIn("error", response)
        mock_post.assert_called_once()

    @patch("requests.post")
    @patch("builtins.open", new_callable=mock_open, read_data="file_content")
    def test_send_sms_with_attachment(self, mock_open, mock_post):
        mock_response = unittest.mock.Mock()
        mock_response.json.return_value = {"status": "success"}
        mock_response.raise_for_status = unittest.mock.Mock()
        mock_post.return_value = mock_response

        response = self.client.send_sms("sender_id", "Hello", "1234567890", "path/to/file")
        self.assertEqual(response, {"status": "success"})
        mock_post.assert_called_once()
        mock_open.assert_called_once_with("path/to/file", "rb")

    @patch("requests.get")
    def test_get_credit_balance_success(self, mock_get):
        mock_response = unittest.mock.Mock()
        mock_response.json.return_value = {"balance": 100}
        mock_response.raise_for_status = unittest.mock.Mock()
        mock_get.return_value = mock_response

        response = self.client.get_credit_balance()
        self.assertEqual(response, {"balance": 100})
        mock_get.assert_called_once()

    @patch("requests.get")
    def test_get_credit_balance_failure(self, mock_get):
        mock_response = unittest.mock.Mock()
        mock_response.raise_for_status.side_effect = requests.exceptions.HTTPError("Error")
        mock_get.return_value = mock_response

        response = self.client.get_credit_balance()
        self.assertIn("error", response)
        mock_get.assert_called_once()

if __name__ == "__main__":
    unittest.main()
