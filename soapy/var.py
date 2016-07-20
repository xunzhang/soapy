PREFIX_FMT = '''<!doctype html>\n\
<html>\n\
<head>\n\
<title>%s</title>\n\
<style type="text/css">%s</style>\n\
</head>\n\
<body>\n\
<h3>%s</h3>\n\
<table class="simpletable">\n\
<tr><td class="rowname">Files:</td>%s\n\
<tr><td class="rowname">Entry:</td><td><a href="#Path1">%s</a></td></tr>\n\
<tr><td class="rowname">Description:</td><td>%s</td></tr>\n\
</table>\n \
<h3>%s</h3>\n'''

CODEWORD_FMT = '''%s<span class='%s'>%s </span>%s'''

CODELINE_FMT = '''<tr><td class="num" id="LN%s">%s</td><td class="line">%s</td></tr>\n'''

INVOKE_PATH_FMT = '''TODO'''

LANGUAGE_SUFFIX_DICT = {'c': 'c', 'h': 'cpp', 'hpp': 'cpp', 'cpp': 'cpp', 'cc': 'cpp'}

SYMBOL_TABLE = {}

HTML_SHIFT_DICT = {'<': "&lt;", '>': "&gt;", '&': "&amp;"}

CPP_KEYWORDS = {'alignas', 'alignof', 'and', 'and_eq', 'asm', 'atomic_cancel', 'atomic_commit', 'atomic_noexcept', 'auto',
                'bitand', 'bitor', 'bool', 'break', 'case', 'catch', 'char', 'char16_t', 'char32_t', 'class', 'compl', 'concept', 'const', 'const_cast', 'continue',
                'decltype', 'default', 'delete', 'do', 'double', 'dynamic_cast', 'else', 'enum', 'explicit', 'explore', 'extern', 'false', 'float', 'for', 'frient',
                'goto', 'if', 'inline', 'int', 'import', 'long', 'module', 'mutable', 'namespace', 'new', 'noexcept', 'not', 'not_eq', 'nullptr',
                'operator', 'or', 'or_eq', 'private', 'protected', 'public', 'register', 'reinterpret_cast', 'requires', 'return',
                'short', 'signed', 'sizeof', 'static', 'static_assert', 'static_cast', 'struct', 'switch', 'synchronized',
                'template', 'this', 'thread_local', 'throw', 'true', 'try', 'typedef', 'typeid', 'typename', 'union', 'unsigned', 'using',
                'virtual', 'void', 'volatile', 'wchar_t', 'while', 'xor', 'xor_eq'}
