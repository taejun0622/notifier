#!/usr/bin/env python3
"""
Discord Notification Tool
A simple tool to send notifications to Discord channels via webhooks.
"""

from notifier.discord_notifier import DiscordNotifier

def main():
    """Main entry point of the application."""
    try:
        notifier = DiscordNotifier()
        
        # Send a test message
        message = "Hello! This is a test message."
        title = "Test Notification"
        
        if notifier.send_message(message, title):
            print("Message sent successfully!")
        else:
            print("Failed to send message.")
            
    except ValueError as e:
        print(f"Configuration error: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

if __name__ == "__main__":
    main()
