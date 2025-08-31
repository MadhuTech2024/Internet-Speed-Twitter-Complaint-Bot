🚀 Internet Speed Test & Twitter Bot

This project automates:

Running an internet speed test on Speedtest.net
.

Extracting download and upload speeds.

Logging into Twitter automatically.

Posting a tweet complaining (or bragging) about the internet speed.

It’s inspired by the popular “Twitter Bot” automation project.

📌 Features

Runs an internet speed test using Selenium.

Extracts download/upload speed values.

Logs into Twitter with credentials from a .env file.

Tweets your internet speed automatically.

Simple and configurable.

🛠️ Requirements

Python 3.8+

Google Chrome installed

The following Python packages:

pip install selenium python-dotenv webdriver-manager

⚙️ Setup

Clone the repo or copy the script.

git clone https://github.com/MadhuTech2024/Internet-Speed-Twitter-Complaint-Bot.git
cd speedtest-twitter-bot


Create a .env file in the project root:

TWITTER_EMAIL=your_twitter_email
TWITTER_PASSWORD=your_twitter_password


Run the script:

python speedtest_twitter_bot.py

📸 How it Works

Script opens Chrome → navigates to Speedtest.net.

Clicks “Go” → waits for test to complete.

Extracts download & upload speeds.

Logs into Twitter → posts a tweet with results.

Example Tweet:

Hey Internet Provider, why is my internet 45.7down/12.3up when I pay for much more? 😡 #SpeedTest

🔧 Customization

Change complaint thresholds (e.g., expected speeds) before tweeting.

Save results into a log file (CSV or TXT).

Take screenshots of speed test results.

Run script in headless mode (no browser popup).

Schedule with Task Scheduler (Windows) or cron (Linux/Mac).