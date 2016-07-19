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

LANGUAGE_SUFFIX_DICT = {'c': 'c', 'h': 'cpp', 'hpp': 'cpp', 'cpp': 'cpp', 'cc': 'cpp'}
