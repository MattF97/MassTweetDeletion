# MassTweetDeletion
A simple script and instructions of how to mass delete your tweets

Tutorial for those who want to delete all of your tweets for free!

First, you’ll need to install Python in your computer, and then install VScode (setting this as a pattern because was the software I used) to run the script.

**1.1 Install Python**
You can download Python here
https://www.python.org/downloads
During installation, make sure to check “Add python to Path” before clicking “Install now”.

**1.2 Install VSCode**
Go to: https://code.visualstudio.com
Download and Install Visual Studio Code

**1.3 Install Tweepy (Twitter API library)**
Once Python is installed, open VSCode, and do this:
Open the Terminal by pressing Ctrl + `` or go to Terminal > New Terminal

Instal Tweepy by typing this:
Pip install tweepy

**2 – Request and Download Your Twitter Archive**
1.	Go to https://twitter.com/settings/download_your_data
2.	Request your full account archive
3.	Wait for Twitter to notify you when it’s ready
4.	Download and extract the .zip file

Inside the archive, look for:
tweets.js or data/tweets.js (It is in your data file that comes with twitter archive)

**3 – Get Twitter API credentials**
3.1 Create Developer Account
1. Go to https://developer.x.com/en/portal/dashboard
2. Log in with your Twitter account
3. Create a Developer App
3.2 Set App permissions
App type: Web app, Automated App or Bot
Permissions: Read and Write
Callback URL: http://localhost
Website: https://example.com
Save settings

**3. 3 Generate Keys and Tokens**
Go to Keys and Tokens section:
Regenerate/copy these 4 values:
API Key
API Key Secret
Access Token
Access Token Secret

You’ll need them to your script.

**4 – Build and run the Python Script**
Save this script as delete_tweets.py in VSCode

(For practicity, I uploaded the code as delete_tweets.py instead of copy and pasting here)

Important: Place the tweets.js file in the same folder as your script.


**4.2	Run the script**
In the terminal inside VSCode:
Py delete_tweets.py

IF everything is set correctly, it will begin deleting tweets one by one.
The time of deletion depends on how many tweets you have. I deleted around 14k of mine and it took almost 6 hours.
