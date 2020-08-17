## Quotes Telegram Bot <br>

 [![Send Message](https://firebasestorage.googleapis.com/v0/b/webtuhin.appspot.com/o/githubstatic%2Fbutton.png?alt=media&token=844f23bf-e6c9-48c6-84c6-8c50a7e922a2)](https://t.me/QuotesTeleBot) <br><br>
**This Project has Two Parts :**<br>
*i. Frontend*<br>
*ii. Backend* <br><br>
###  Backend
**Brief:**<br>
*We need a server for API  Request. So I prefere Cloudflare Workers.*<br>
**Installation:**<br>
*Go to [Here](https://github.com/cachecleanerjeet/QuotesTeleBot/tree/backend "Here")*<br><br>

### Frontend<br>
**Brief:**<br>
*We will get the Content from API when get a Quote Request from Telegram. I use Python Flask,  Request and Webhook.*<br><br>
**Installation:**
#### *i. Deploy to Heroku:*<br>
[![Deploy](https://www.herokucdn.com/deploy/button.svg)](https://heroku.com/deploy?template=https://github.com/cachecleanerjeet/QuotesTeleBot/tree/heroku)<br>
**Open the following url in Browser to Start your Application (Unless won't work):**<br>
*[Your Application Url]/start*<br>
   
    ## example
    http://yourbot.herokuapp.com/start
    
#### *ii. [Manually Deploy to Heroku](https://github.com/cachecleanerjeet/QuotesTeleBot/tree/heroku "Manually Deploy to Heroku")*<br>
#### *iii. Deploy to VPS or Local Machine for Development:*<br>
a. Clone the Repo<br>

    git clone https://github.com/cachecleanerjeet/QuotesTeleBot.git

b. Go to <tt>QuotesTeleBot</tt> Directory<br>

    cd QuotesTeleBot

c. Install the Dependencies:<br>

    pip3 install -r requirements.txt

d. Open <tt>settings.py</tt> and replace <tt>YOUR-API-KEY</tt> in <tt>Bot_API_KEY</tt> Section<br>
    
    ## Previously
    Bot_API_KEY = "YOUR-API-KEY"
    ## After Enter your own Key
    Bot_API_KEY = "123456:abcdefghijklmnopqrstuvwxyz"

e. Open <tt>main.py</tt> and change <tt>QUOTE_API_URL</tt> if You want that Bot works with your own Backend Server<br>

    ## Previously
    QUOTE_API_URL = "https://quotesapi.tuhinwin.workers.dev/"
    ## After enter your own API url
    QUOTE_API_URL = "http://api.yourdomain.com/"

f. Run the BOT:<br>

    python3 run.py 

**Start Frontend (Unless won't work):**<br>

*[Your Application Url]/start*

    ## examples
    http://0.0.0.0:3000/start
    http://70.74.251.42/start
    http://yourbot.herokuapp.com/start
    http://server.hin.life:3000/start
    
<br><br>
**[Apache License 2.0](https://github.com/cachecleanerjeet/QuotesTeleBot/blob/master/LICENSE "Apache License 2.0")** <br><br>

>Website `https://tu.hin.life`.<br>
>My Social:<br><br>

https://fb.me/jeeetpaul<br>
https://www.instagram.com/jeeetpaul<br>
https://www.youtube.com/channel/UCa4FMtLpYcOBtjKOZgzTFNA<br>
https://github.com/cachecleanerjeet<br>
https://blog.iamtuhin.ga<br><br>

![Quote Telegram Bot](https://firebasestorage.googleapis.com/v0/b/webtuhin.appspot.com/o/githubstatic%2Fqtbotcirhq.png?alt=media&token=033bcdd7-4fde-4337-a76f-89f18ee4d53d)
