import gdata.docs.service as docserv
import getpass

#username = raw_input('username: ')
username = 'christopher.m.hedrick'
password = getpass.getpass('password: ')
client = docserv.DocsService()
client.ClientLogin(username, password)
documents_feed = client.GetDocumentListFeed()

def get_list():
    for document_entry in documents_feed.entry:
        print document_entry.title.text
    
command = ''
while command != 'q':
    print '\n'
    print 'Commands:'
    print 'q = quit'
    print 'g = get'
    command = raw_input('Command: ')
    print '\n'
    if command == 'g':
        get_list()
    elif command == 'q':
        break
    else:
        print "invalid command"
