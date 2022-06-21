# set the namespace of XML file



MY_NAMESPACES = {'settings': 'http://example.com/url-for-settings-namespace',
    None: 'http://harris-fraser.com/url-for-default-namespace'}

r = etree.Element('my-root', nsmap = MY_NAMESPACES)
d = etree.Element('{%s}some-element' % MY_NAMESPACES[None])
e = etree.Element('{%s}current' % MY_NAMESPACES['settings'])
d.append(e)
r.append(d)
etree.toString(r)


"""
<my-root xmlns:settings = "http://example.com/url-for-settings-namespace"
         xmlns = "http://harris-fraser.com/url-for-default-namespace">

         <some-element>
            <settings:current/>
         </some-element>
</my-root>
"""

MY_NAMESPACES = {'settings': 'http://example.com/url-for-settings-namespace'}
e = etree.Element('{%s}current' % MY_NAMESPACES['settings'], nsmap=MY_NAMESPACES)
etree.toString(e)

"""
<settings:current xmlns:settings="http://example.com/url-for-settings-namespace"/>
"""