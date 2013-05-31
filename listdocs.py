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
    spread_needs = {}
    spread_keys = []
    spread_ids = []
    group = []
    out = []
    for spreadsheet in spreadsheet_feed.entry:
        spread_keys.append(spreadsheet.id.text.rsplit('/', 1)[1])
    for i in range(len(spreadsheet_feed.entry)):
        curkey = spread_keys[i]
        worksheet_feed = spreadclient.GetWorksheetsFeed(curkey)
        for worksheet in worksheet_feed.entry:
            group.append(worksheet.id.text.rsplit('/', 1)[1])
        spread_ids.append(group)
        group = []
        spread_needs[spread_keys[i]] = spread_ids[i]
    spread_list = []
    for spreadsheet in spreadsheet_feed.entry:
        spread_list.append(spreadsheet)
    for i in range(len(spread_list)):
        for key, value in spread_needs.items():
            out.append(' ' + str(key) + ' ' + str(value))
        print spread_list[i].title.text + out[i]

def sheet_select():
    feed = spreadclient.GetListFeed(spread_code, worksheet_id)
    for row in feed.entry:
        print "%s| %s\n" % (row.title.text, row.content.text)

command = ''
while command != 'q':
    print '\nCommands:'
    print 'q = quit'
    print 'g = get'
    print 's = spreadsheet ids'
    print 'select [spreadsheet id] [worksheet id] = read worksheet'
    command = raw_input('Command: ')
    print '------------------------'
    if command == 'g':
        get_list()
    elif command == 's':
        get_spreadsheet_ids()
    elif 'select' in command.split():
        selected = command.split()
        spread_code = selected[1]
        worksheet_id = selected[2]
        sheet_select()
    elif command == 'q':
        break
    else:
        print "invalid command"
