import json
from util import expand


class html_attr:
    def __init__(self, cfg_file):
        self.attr = {}
        self.load(cfg_file)

    def load(self, cfg_file):
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

    def reload(self, cfg_file):
        self.load(cfg_file)

    def get_attr(self):
        return self.attr

    def set(self, key, val):
        if key in self.attr.keys():
            self.attr[key] = val
            return True
        else:
            return False


class html(html_attr):
    def __init__(self, cfg_file):
        from var import LANGUAGE_SUFFIX_DICT, PREFIX_FMT
        html_attr.__init__(self, cfg_file)
        self.lang = LANGUAGE_SUFFIX_DICT.get(self.attr.get('source_files')[0].split('.')[-1])
        files = ''
        for k, fn in enumerate(self.attr.get('source_files')):
            if k == 0:
                files += '<td>%s</td>' % fn
            else:
                files += '</tr><tr><td></td><td>%s</td></tr>' % fn
            if k != len(self.attr.get('source_files')) - 1:
                files += '\n'
        self.prefix = PREFIX_FMT % (self.attr.get('title'),
                                    '%s_style.css' % self.lang,
                                    self.attr.get('subtitle1'),
                                    files,
                                    self.attr.get('entry'),
                                    self.attr.get('description'),
                                    self.attr.get('subtitle2'))
        self.suffix = '</body></html>'

    def get_attr(self):
        return self.attr

    def get_lang(self):
        return self.lang

    def get_prefix(self):
        return self.prefix

    def get_suffix(self):
        return self.suffix


class filler:
    def __init__(self, output, cfg_file):
        self.html_info = html(cfg_file)
        self.output = output

    def fill_header(self):
        self.f.write(self.html_info.get_prefix())

    def fill_body(self):
        pass

    def fill_footer(self):
        self.f.write(self.html_info.get_suffix())

    def fill(self):
        self.f = file(self.output, 'w')
        self.fill_header()
        self.fill_body()
        self.fill_footer()
        self.f.close()
