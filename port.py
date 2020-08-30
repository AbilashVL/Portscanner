import argparse

import time

green = "\033[32m"
bold = "\033[1m"
blue = "\033[94m"
red = "\033[91m"
end = "\033[0m"

start = time.time()

print '              CREATED BY ABILASH.V.L              '
  
print '#################################################'                    
print '================================================='
print '               ++++++++++++++++++++              '
print '\n                                               '
print '  _,.      #hacked!!              ###                        '
print '                                 #######'
print '                                     ###            '
print '           Whitehat                               '
print '       _,.                   '
print '     ,` -.)                  '
print '    ( _/-\\-._               '
print '   /,|`--._,-^|            , '
print '   \_| |`-._/||          , | '
print '     |  `-, / |         /  / '
print '     |     || |        /  /  '
print '      `r-._||/   __   /  /   '
print '  __,-<_     )`-/  `./  /    '
print '  \   `---    \   / /  /     '
print '     |           |./  /      '
print '     /           //  /       '
print ' \_/  \         |/  /        '
print '  |    |   _,^- /  /         '
print '  |    , ``  (\/  /_         '
print '   \,.->._    \X-=/^         '
print '   (  /   `-._//^`           '
print '    `Y-.____(__}             '
print '     |     {__)              ' 
print '           ()   V.1.0        '
print(blue + """
 ____            _   ____                  
|  _ \ ___  _ __| |_/ ___|  ___ __ _ _ __  
| |_) / _ \| '__| __\___ \ / __/ _` | '_ \ 
|  __/ (_) | |  | |_ ___) | (_| (_| | | | |
|_|   \___/|_|   \__|____/ \___\__,_|_| |_|
                By: Abilash.v.l
""" + end)

import socket

t_host = str(raw_input("Enter the host to be scanned: "))   
t_ip = socket.gethostbyname(t_host)     

print t_ip      

while 1:
	t_port = int(raw_input("Enter the port: "))	   
	
	try:
		sock = socket.socket()			
		res = sock.connect((t_ip, t_port))
		print "Port {}: Open" .format(t_port)
		sock.close()
	except:
		print "Port {}: Closed" .format(t_port)
	
print "Port Scanning complete"

