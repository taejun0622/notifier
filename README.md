# Discord Notifier

A simple Python package for sending notifications to Discord channels using webhooks.

## Installation

```bash
pip install dugudugu-discord-notifier
```

## Configuration

1. Create a `.env` file in your project root directory
2. Add your Discord webhook URL to the `.env` file:
   ```env
   WEBHOOK_URL=your_discord_webhook_url_here
   ```

### How to get Discord Webhook URL:
1. Go to your Discord server
2. Right-click on the channel you want to send messages to
3. Click 'Edit Channel'
4. Click 'Integrations'
5. Click 'Create Webhook' (or 'View Webhooks' if you already have one)
6. Click 'New Webhook'
7. Copy the Webhook URL
8. Paste it in your `.env` file

## Usage

```python
from notifier.discord_notifier import DiscordNotifier

# Initialize the notifier
notifier = DiscordNotifier()

# Send a simple message
notifier.send_message("Hello, World!")

# Send a message with a title
notifier.send_message("This is the message content", "This is the title")
```

## Features

- Simple and easy to use
- Supports markdown formatting
- Environment-based configuration
- Timeout handling
- Error reporting

## Requirements

- Python 3.7+
- requests
- python-dotenv
