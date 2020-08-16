import flask, os, sys, json, requests
app = flask.Flask('QUOTE')
app.config.from_object('settings')
cfg = app.config

def msg_receive_(msg, cmd, ln):
	params = dict(
			method ='sendMessage',
			chat_id = msg['chat']['id'],		
			parse_mode =  "HTML"
			)
	print(cmd)
 
	if ('help' in cmd) is True: 
		params['text'] = 'Random Quotes Generator. \n \nReply with : \n<code>/quote</code> \n \nReply with <code>/about</code> for detail and Source code of this Bot.'
	elif ('about' in cmd) is True:
		params['text'] = 'This bot is Made by Tuhin: \nWebsite : https://tu.hin.life \nGithub : https://github.com/cachecleanerjeet \nYouTube : https://iamtuhin.page.link/YouTube \n \nQuotes API by: \nhttps://api.kanye.rest/ \n \nSouce code available here: \nhttps://github.com/cachecleanerjeet/QuotesTeleBot'
	elif ('ping' in cmd) is True: 
		params['text'] = 'Everything is alright'
	elif ('quote' in cmd) is True: 
		url = requests.get('https://api.kanye.rest/')
		params['text'] = '{}'.format(url.json()["quote"] )

	return flask.Response(response=json.dumps(params), headers={'Content-Type':'application/json'},status=200)

import handler
