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
set_spreadid = ''

def get_list():
    for document_entry in documents_feed.entry:
        print document_entry.title.text

def get_spreadsheet_ids():
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
        spread_needs = zip(spread_keys, spread_ids)
    for key, value in spread_needs:
        out.append(' ' + str(key) + ' ' + str(value))
    return out

def print_spreadsheets_ids(processed_ids):
    for i in range(len(spreadsheet_feed.entry)):
        print spreadsheet_feed.entry[i].title.text + processed_ids[i]

def sheet_read():
    feed = spreadclient.GetListFeed(set_spreadid, set_workid)
    for row in feed.entry:
        print "%s| %s\n" % (row.title.text, row.content.text)

def set_spreadsheet(command):
    working_sheet = command.split()
    global set_spreadid
    set_spreadid = working_sheet[1]
    global set_workid
    set_workid = working_sheet[2]

def make_columns():
    feed = spreadclient.GetListFeed(set_spreadid, set_workid)
    splitted_columns = feed.entry[0].custom.items()
    col = []
    for i in range(len(splitted_columns)):
        col.append(splitted_columns[i][0])
    return col

def enter_columns(cols):
    new_row = {}
    for col in cols:
        new_row[col] = raw_input(col + ' ')
    return new_row

def insert_row(row):
    spreadclient.InsertRow(row, set_spreadid, set_workid)

def test():
    import pdb; pdb.set_trace()

command = ''
while command != 'q':
    print '\nCommands:'
    print 'q = quit'
    print 'g = get'
    print 's = spreadsheet ids'
    print 'set [spreadsheet id] [worksheet id] = set a worksheet to work on'
    print 'read = read worksheet'
    print 'insert = insert row'
    command = raw_input('Command: ')
    print '------------------------'
    if command == 'g':
        get_list()
    elif command == 's':
        processed_ids = get_spreadsheet_ids()
        print_spreadsheets_ids(processed_ids)
    elif command == 't':
        test()
    elif 'read' in command.split():
        sheet_read()
    elif 'insert' in command:
        cols = make_columns()
        row = enter_columns(cols)
        insert_row(row)

    elif 'set' in command:
        set_spreadsheet(command)
    elif command == 'q':
        break
    else:
        print "invalid command"
