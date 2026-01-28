<<<<<<< Updated upstream
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
=======
# eChad Discord Bot

eChad is a versatile Discord bot built using the Discord.py library. It offers a range of features and functionalities to enhance your Discord server experience.

## Features

- **Message Handling**: The bot intelligently handles messages, performs actions, and responds based on various conditions.
- **Nickname Tracking**: eChad tracks nickname changes and sends notifications when a user's nickname is modified.
- **Reactions**: The bot adds reactions to messages based on specific triggers and conditions.
- **Insult Detection**: eChad detects insults in messages and provides appropriate responses.
- **File Sending**: The bot can send files and images in response to specific triggers or commands.
- **Member Join/Leave**: eChad sends welcome and farewell messages when a member joins or leaves the server.
- **Message Delete/Edit Tracking**: The bot tracks deleted and edited messages, sending notifications and preserving the original and edited content.

## Usage

To use the eChad Discord bot, follow these steps:

1. Invite the bot by asking me for an invite link on discord or here.
2. OR if you want to customize this bot you will have to create your own token and make alterations to the code in order for it to wokr. Contact me for further details

## Customization

The eChad bot's code is highly customizable to suit your specific needs. You can modify the commands, conditions, and responses according to your preferences. Additionally, you can extend the bot's functionality by adding new features and commands.

## Dependencies

The eChad Discord bot has the following dependencies:

- Discord.py
- Python 3.7 or higher

Make sure to install the necessary dependencies before running the bot.

## Contributing

Contributions to the eChad Discord bot are welcome! If you have any enhancements, bug fixes, or new features to suggest, please feel free to submit a pull request or open an issue on the GitHub repository.

---

**Note**: This documentation provides an overview of the eChad Discord bot. For more detailed information, refer to the code comments and the official Discord.py documentation.

>>>>>>> Stashed changes
