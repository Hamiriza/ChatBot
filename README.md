# Chatbot Application

This is a simple chatbot application that responds to user inputs based on predefined responses stored in a JSON file. If the user input does not match any predefined responses, the chatbot provides a random response from a predefined list. The application also terminates when the user says goodbye.

## Features

- Responds to user inputs with predefined responses.
- Provides random responses for unrecognized inputs.
- Terminates the conversation on farewell phrases like "goodbye" or "see you later".

## Files

- `main.py`: The main script to run the chatbot.
- `responses.json`: A JSON file containing predefined user inputs and corresponding bot responses.
- `random_responses.py`: A module providing random responses for unrecognized user inputs.

## Prerequisites

- Python 3.x

## Installation

1. Clone the repository:

    ```bash
    git clone https://github.com/hamiriza/chatbot.git
    cd chatbot
    ```

2. (Optional) Create and activate a virtual environment:

    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
    ```

3. Install any required dependencies:

    ```bash
    pip install -r requirements.txt  # If you have a requirements.txt file
    ```

## Usage

1. Ensure you are in the project directory.
2. Run the chatbot:

    ```bash
    python main.py
    ```

3. Start chatting with the bot. Type your messages and press Enter.
4. To terminate the conversation, type a farewell phrase like "goodbye", "bye bye", or "see you later".

## Example

You: Hello

Bot: Hey there!

You: How are you?

Bot: I'm great! Thanks for asking.

You: See you later

Bot: Goodbye! Have a great day!

## Customization

- **Add/Modify Responses:** Edit the `responses.json` file to add or modify the predefined responses.
- **Change Random Responses:** Edit the `random_responses.py` file to add or modify the random responses.

## Contributing

Feel free to submit issues or pull requests if you find bugs or want to contribute to the project.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.