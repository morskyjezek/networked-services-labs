import xml.etree.ElementTree as ET

# basic load
tree = ET.parse('data/xml/superior-papers.xml')

# define XML object with root element
root = tree.getroot()

# identify element information: tag, attrib, text
#print(root.tag, root.attrib, root.text)

# find elements using find
control = root.find('{http://ead3.archivists.org/schema/}control')

print(control.tag, control.attrib)

# find attributes using get
langCode = control.get('langencoding')

print(langCode)

# modify attributes with set
control.set('language', 'en-US')

# record any changes with write
#tree.write('data/xml/superior-papers.xml')

# modify elements with append() from string
newstuff = ET.fromstring('<did>A new did</did>')

root.append(newstuff)

#tree.write('data/xml/superior-papers.xml')

# modify creating new elements with Element constructor
newDid = ET.Element('ead:did', attrib={'isNew':'true'})
newDid.text = 'A new did'

root.append(newDid)

tree.write('data/xml/superior-papers.xml')

# looping through sublements using iter --> iterators
for element in root.iter(control):
    print(element.tag, element.text)