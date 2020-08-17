import  os, random
Bot_API_KEY = "YOUR-API-KEY"
IDBOT =  Bot_API_KEY[:9]
TELEGRAM_API = 'https://api.telegram.org/bot{token}/'.format(token=Bot_API_KEY)
FIX = [{
	'quotes': 'quote', 
	'quote': 'quote',
	'help': 'help', 
	'start': 'help', 
	'about': 'about',
	'ping': 'ping',
	}]
