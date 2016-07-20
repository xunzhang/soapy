import os
import json
from util import expand, fmt_html


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
                                    open(os.path.dirname(__file__) + '/../stylesheets/%s_style.css' % self.lang).read() ,
                                    self.attr.get('subtitle1'),
                                    files,
                                    self.attr.get('entry'),
                                    self.attr.get('description'),
                                    self.attr.get('subtitle2'))
        self.suffix = '</body></html>'

    def get_attr(self):
        return self.attr

    def get_source_files(self):
        return self.attr.get('source_files')

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
        if self.html_info.get_lang() == 'cpp':
            self.f.write('<table class="code">')
            for fn in self.html_info.get_source_files():
                self.cpp_filler(fn)
            self.f.write('</table>')

    def fill_footer(self):
        self.f.write(self.html_info.get_suffix())

    def fill(self):
        self.f = file(self.output, 'w')
        self.fill_header()
        self.fill_body()
        self.fill_footer()
        self.f.close()

    def cpp_filler(self, src_file):
        def cpp_html_span_fmt(s):
            from var import CODEWORD_FMT, CPP_KEYWORDS
            words = s.strip('\n').split(' ')
            # empty line
            if len(words) == 0:
                return ' '
            # comment line
            elif words[0].startswith('/') or words[0].startswith('*'):
                return CODEWORD_FMT % ('', 'comment', fmt_html(s), '')
            # macro line
            elif words[0].startswith('#'):
                return CODEWORD_FMT % ('', 'directive', fmt_html(s), '')
            else:
                result = ''
                for word in words:
                    if word in CPP_KEYWORDS:
                        result += CODEWORD_FMT % ('', 'keyword', fmt_html(word), '')
                    elif not len(word):
                        result += ' '
                    else:
                        result += fmt_html(word) + ' '
                return result

        from var import CODELINE_FMT
        f_in = file(src_file)
        for line_cnt, line in enumerate(f_in):
            html_rep = cpp_html_span_fmt(line)
            self.f.write(CODELINE_FMT % (line_cnt + 1, line_cnt + 1, html_rep))
        f_in.close()
