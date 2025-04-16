# eChad Discord Bot

![Discord Bot](https://img.shields.io/badge/Discord-Bot-blue?style=for-the-badge&logo=discord)

eChad is a feature-rich Discord bot designed to bring entertainment, moderation, and utility to your Discord server. With a variety of commands and automated responses, eChad enhances your server's interaction experience.

## Features

- **Automated Responses**: Reacts to specific phrases and triggers with custom messages, GIFs, and images
- **Rizz Tracking**: Keeps track of "rizz" levels for users in designated channels
- **Message Monitoring**: Logs deleted and edited messages with user attribution
- **Custom Reactions**: Responds to certain users with personalized reactions and messages
- **Ngrok Integration**: Provides API URL retrieval functionality for authorized users
- **Member Join/Leave Notifications**: Welcomes new members and bids farewell to departing ones with custom messages

## Commands

- `/do_nothing` - The bot literally does nothing
- `/getapi` - Retrieves the current ngrok API URL (admin only)

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/eChad.git
   ```

2. Install the required dependencies:
   ```bash
   pip install -r requirements.txt
   ```

3. Create a `TOKEN.txt` file in the project directory containing your Discord bot token.

4. Configure the bot by modifying the `data.py` file with your specific channel IDs and user IDs.

5. Run the bot:
   ```bash
   python bot.py
   ```

## Configuration

The bot requires several configuration files and environment settings:

- `TOKEN.txt` - Contains the Discord bot token
- `data.py` - Contains server-specific configuration (channel IDs, user IDs, etc.)
- `unspoken.txt` - Tracks user rizz levels
- Various media files (GIFs, images, videos) for responses

## Dependencies

- Python 3.8+
- discord.py
- Other standard Python libraries

## Contributing

Contributions are welcome! Please fork the repository and create a pull request with your changes.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Disclaimer

This bot is designed for entertainment purposes. Some features may include humorous or sarcastic responses that are not intended to be taken seriously.
