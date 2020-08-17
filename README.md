## Quotes Telegram Bot

**This Project has Two Parts :**<br>
*i. [Frontend](#Frontend "Frontend")*<br>
*ii. [Backend](#Backend "Backend")* <br><br>
###  Backend
**Brief:**<br>
*We need a server for API  Request. So I prefere Cloudflare Workers.*<br>
**Installation:**<br>
*Go to  <tt>backend</tt>  Branch*<br>
*Or,*<br>
*[Tap Here](https://github.com/cachecleanerjeet/QuotesTeleBot/tree/backend "Tap Here")*<br><br>

### Frontend<br>
**Brief:**<br>
*We will get the Content from API when get a Quote Request from Telegram. I use Python Flask,  Request and Webhook.*<br>
**Installation:**<br>
##### *i. Deploy to Heroku:*<br>
[![Deploy](https://www.herokucdn.com/deploy/button.svg)](https://heroku.com/deploy?template=https://github.com/cachecleanerjeet/QuotesTeleBot/tree/heroku)<br>
##### *ii. [Manually Deploy to Heroku](https://github.com/cachecleanerjeet/QuotesTeleBot/tree/heroku "Manually Deploy to Heroku")*<br>
##### *iii. Deploy to VPS or for Development:*<br>
*a. Clone the Repo*<br>
*b Go to <tt>QuotesTeleBot</tt> Directory*<br>
*c. Install the Dependencies:*<br>
    pip3 install -r requirements.txt
<br>
*d. Open <tt>settings.py</tt> and  replace <tt>YOUR-API-KEY</tt> in  <tt>Bot_API_KEY</tt> Section (Telegram Bot API KEY).*<br>
*e. Open <tt>main.py</tt> and  change <tt>QUOTE_API_URL</tt> if You want that Bot works with your own Backend Server (Backend Server Url).*<br>
*f. Run the BOT:*<br>
    python3 run.py 
<br><br>
**Start Frontend: **<br>

*[Your Application Url]/start*

    ## example
    http://0.0.0.0:3000/start
    

