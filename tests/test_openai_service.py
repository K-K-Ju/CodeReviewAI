from codereviewai.config import settings
import openai
from unittest import mock

def test_valid_api_key():
    openai.api_key = settings.openai_api_key
    mock_response = {
        'choices': [
            {'message': {'content': 'Hello, world!'}}
        ]
    }

    with mock.patch('openai.chat.completions.create', return_value=mock_response) as mock_create:
        result = openai.chat.completions.create(model='gpt-3.5-turbo',
                                                messages=[{'role':'user', 'content':{'type':'text', 'text':'Say "Helo World!"'}}])

        mock_create.assert_called_once_with(
            model="gpt-3.5-turbo",
            messages=[
                {"role": 'user', 'content': {'type':'text', 'text':'Say "Helo World!"'}}
            ]
        )

        assert result == mock_response
