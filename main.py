import urllib.parse

def banner():
    print('''
           ___                  _      _  _           ___                  _      _  _  
          |   \   ___     _ _  | |__  | || |   o O O |   \   ___     _ _  | |__  | || | 
          | |) | / _ \   | '_| | / /   \_, |  o      | |) | / _ \   | '_| | / /   \_, | 
          |___/  \___/  _|_|_  |_\_\  _|__/  TS__[O] |___/  \___/  _|_|_  |_\_\  _|__/  
        _|"""""_|"""""_|"""""_|"""""_| """"|{======_|"""""_|"""""_|"""""_|"""""_| """"| 
        "`-0-0-"`-0-0-"`-0-0-"`-0-0-"`-0-0-./o--000"`-0-0-"`-0-0-"`-0-0-"`-0-0-"`-0-0-' 
                                        by: @h3lium
    ''')

banner()


gg_url = 'https://www.google.com/search?num=100&q='

gdorks = ['site:__SITE__ filetype:php',
	    'site:__SITE__ filetype:swf',
	    'site:__SITE__ inurl:swf',
        'site:__SITE__ inurl:config',
    	'site:__SITE__ filetype:wsdl',
    	'site:__SITE__ inurl:&',
    	'site:__SITE__ inurl:redirect',
    	'site:__SITE__ intitle:"index of"',
    	'site:__SITE__ intext:"/uploads/"',
    	'site:__SITE__ inurl:wp-content',
    	'site:__SITE__ inurl:jira',
    	'site:__SITE__ "Notice"',
    	'site:__SITE__ "Warning"',
    	'site:__SITE__ "Fatal error"',
    	'site:__SITE__ "PHP Error"',
    	'site:__SITE__ "Call Stack"',
    	'site:__SITE__ "mysql"',
    	'site:__SITE__ "A problem occured in"',
    	'site:__SITE__ "not found on this server"',
    	'site:__SITE__ inurl:url=',
    	'site:__SITE__ inurl:file=',
    	'site:__SITE__ inurl:login,register',
    	'site:__SITE__ inurl:token',
    	'site:__SITE__ inurl:apikey',
    	'site:__SITE__ inurl:password',
    	'site:__SITE__ allinurl:@__SITE__',
    	'site:__SITE__ intitle:"about atlassian bitbucket"',
    	'site:trello.com __SITE__',
    	'site:asana.com __SITE__'
]

URL = input("Please enter URL to dork: ")

for x in gdorks:
    query = x.replace('__SITE__', URL)
    print(gg_url+urllib.parse.quote(query))
    
