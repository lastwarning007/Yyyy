import telebot
import requests
import os

# Replace 'YOUR_BOT_TOKEN' with your actual bot token
API_TOKEN = '7638693006:AAFjVagjyPq_SwVHVltBafehJhlNvs1ViYc'
bot = telebot.TeleBot(API_TOKEN)

# Function to handle incoming messages
@bot.message_handler(func=lambda message: True)
def handle_message(message):
    user_input = message.text
    print(f"Received message: {user_input}")

    # Prepare the request to the external API
    h = {'Host': 'baithek.com', 'Content-Type': 'application/json', 'User -Agent': 'okhttp/4.9.2'}
    d = {'name': 'Usama', 'messages': [{'role': 'user', 'content': user_input}]}
    
    try:
        r = requests.post('https://baithek.com/chatbee/health_ai/new_health.php', headers=h, json=d)
        r.raise_for_status()  # Raise an error for bad responses
        response_content = r.json()['choices'][0]['message']['content']
        
        # Send the response back to the user
        bot.reply_to(message, response_content)
    except requests.exceptions.RequestException as e:
        bot.reply_to(message, "An error occurred while processing your request.")

# Start polling for new messages
if __name__ == '__main__':
    print("Bot starting by LAST WARNING..")
    bot.polling()