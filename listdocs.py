import gdata.docs.service as docserv
import gdata.spreadsheet.service as spreadserv
import getpass

#username = raw_input('username: ')
username = 'christopher.m.hedrick'
password = getpass.getpass('password: ')
client = docserv.DocsService()
client.ClientLogin(username, password)
spreadclient = spreadserv.SpreadsheetsService()
spreadclient.email = username
spreadclient.password = password
spreadclient.ProgrammaticLogin()
spreadsheet_feed = spreadclient.GetSpreadsheetsFeed()
documents_feed = client.GetDocumentListFeed()

def get_list():
    for document_entry in documents_feed.entry:
        print document_entry.title.text

def get_spreadsheet_ids():
    for spreadsheet in spreadsheet_feed.entry:
        print spreadsheet.id.text.rsplit('/', 1)[1]
    
command = ''
while command != 'q':
    print '\nCommands:'
    print 'q = quit'
    print 'g = get'
    print 's = spreadsheet ids'
    command = raw_input('Command: ')
    print '------------------------'
    if command == 'g':
        get_list()
    elif command == 's':
        get_spreadsheet_ids()
    elif command == 'q':
        break
    else:
        print "invalid command"
