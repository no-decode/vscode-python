import html
def make_htmlElement(name,value,**attrs):
    print('<{name}{attrs}>{value}</{name}>'.format(name=name,value=html.escape(value),attrs=''.join([' %s="%s"' % item for item in attrs.items()])))
make_htmlElement('item','Albatross',size="large",weight=10)
