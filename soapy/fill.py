import json
from util import expand

class html_attr:
    def __init__(self, cfg_file):
        self.attr = {}
        json_obj = json.loads(open(cfg_file).read())
        self.attr['title'] = json_obj['title'] if json_obj.__contains__('title') else 'welcome to soapy'
        if json_obj.__contains__('source_files'):
            self.attr['source_files'] = expand(json_obj['source_files'])
        else:
            print 'You need to specify source files with "source_files" attr.'
            sys.exit(0)
        self.attr['description'] = json_obj['description'] if json_obj.__contains__('description') else 'description'
        self.attr['entry'] = json_obj['entry'] if json_obj.__contains__('entry') else 'entry'
        self.attr['subtitle1'] = json_obj['subtitle1'] if json_obj.__contains__('subtitle1') else 'subtitle1'
        self.attr['subtitle2'] = json_obj['subtitle2'] if json_obj.__contains__('subtitle2') else 'subtitle2'

    def get_attr(self):
        return self.attr

    def reload(self):
        pass

class html(html_attr):
    pass

class filler:
    def __init__(self, page):
        pass

    def fill_header(self):
        pass

    def fill_body(self):
        pass

    def fill_footer(self):
        pass

    def fill(self):
        fill_header()
        fill_body()
        fill_footer()
