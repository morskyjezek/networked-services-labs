import xml.etree.ElementTree as ET
import xml.dom.minidom as minidom
import codecs

def readableXML(elem): #rewrites xml output to more easily readable, see http://www.doughellmann.com/PyMOTW/xml/etree/ElementTree/create.html
  rough_string = ET.tostring(elem, 'UTF-8')
  reparsed = minidom.parseString(rough_string)
  return reparsed.toprettyxml(indent='  ')

print '''\n
This program will generate a TEI-compliant document from 
a TXT file. Plain text versions of Nohoavica's lyrics were 
extracted from nohavica.cz\n'''

fslug = raw_input('Enter the file name slug (no spaces or file extensions): ')
fhand = codecs.open(fslug+'.txt','r','UTF-8') #opening file this way seems to fix the xml output that does not appear in UTF-8 otherwise (?)
fout = fslug+'TEI.xml'

select = raw_input('''Choose from the following to select an album
 1 - Mikymauzoleum
 2 - Divne stoleti
 3 - Tri cunici
 4 - Darmodej
 5 - Other

Enter choice: ''')

if select == '1':
  albumTitle = 'Mikymauzoleum'
  albumLabel = 'Monitor'
  albumYear = 1993
if select == '2':
  albumTitle = 'Divn&#233; stolet&#237;'
  albumLabel = 'Monitor'
  albumYear = 1996
if select == '3':
  albumTitle = 'T&#345;i &#269;un&#237;ci'
  albumLabel = 'Monitor'
  albumYear = 1994
if select == '4':
  albumTitle = 'Darmod\&amp;#283;j'
  albumLabel = 'Panton'
  albumYear = 1988
if select == '5':
  albumTitle = None
  albumLabel = None
  albumYear = None
print 'Album select is',albumTitle

autor = 'Jarom&#237;r Nohavica'
coder = 'Jesse Johnston'

#register namespace, helper function for python 2.5 ET backward compatibility, since later versions need to use .register_naespace('tei','http://www.tei-c.org/ns/1.0'), see http://effbot.org/zone/element-namespaces.htm (Sep 2012)
try:
    register_namespace = ET.register_namespace
except AttributeError:
    def register_namespace(prefix, uri):
        ET._namespace_map[uri] = prefix
register_namespace('tei', 'http://www.tei-c.org/ns/1.0')
register_namespace('xml', 'http://www.w3.org/XML/1998/namespace')

###----------------------------------------------build TEI though currently this mistakenly applies tei: to the root element, which can be removed by hand to default the namespace
tei = ET.Element('{http://www.tei-c.org/ns/1.0}TEI')


teiHeader = ET.SubElement(tei, 'teiHeader')
teiHeader.attrib['xml:lang'] = 'en' #alternatively: teiHeader.attrib['{http://www.w3.org/XML/Schema.html}lang'] = 'en'

###----------------------------------------------fileDesc Element
fileDesc = ET.SubElement(teiHeader, 'fileDesc')

titleStmt = ET.SubElement(fileDesc, 'titleStmt')
title = ET.SubElement(titleStmt, 'title').text = fslug
author = ET.SubElement(titleStmt, 'author').text = autor
respStmt = ET.SubElement(titleStmt, 'respStmt')
resp = ET.SubElement(respStmt, 'resp')
resp.text = 'Coding, proofing, and conversion to TEI-conformant markup'
resp.tail = 'by'
name = ET.SubElement(respStmt, 'name').text = coder

publicationStmt = ET.SubElement(fileDesc, 'publicationStmt')
p = ET.SubElement(publicationStmt, 'p').text = 'Source Czech texts were written and published online by Jarom&#237;r Nohavica at http://www.nohavica.cz/. Songs were originally sung, recorded, and released in the Czech Republic by Jarom&#237;r Nohavica.'

sourceDesc = ET.SubElement(fileDesc, 'sourceDesc')
p = ET.SubElement(sourceDesc, 'p')
p.text = 'This song was made available on an audio recording released in the Czech Republic:'
#Source Album bibliographic element
bibl = ET.SubElement(p, 'bibl')
author = ET.SubElement(bibl, 'author').text = autor
title = ET.SubElement(bibl, 'title').text = albumTitle
publisher = ET.SubElement(bibl, 'publisher').text = albumLabel
pubPlace = ET.SubElement(bibl, 'pubPlace')
if albumYear > 1900 or albumYear != None:
  date = ET.SubElement(bibl, 'date')
  date.text = str(albumYear)
  date.attrib['when'] = str(albumYear)
  date.attrib['type'] = 'year'
else:
  date = ET.SubElement(bibl, 'date')


###------------------------------------------------text Element
text = ET.SubElement(tei, 'text')
text.attrib['xml:lang'] = 'cs'
front = ET.SubElement(text, 'front')
byline = ET.SubElement(front, 'byline').text = autor

body = ET.SubElement(text, 'body')
lg = ET.SubElement(body, 'lg')

###------------------------------------------------now let's insert the text
lCount = 1
for line in fhand:
  words = line.rstrip()
  print words
  if line == '\n' or line == None:
    lg = ET.SubElement(body, 'lg')
  else:
    l = ET.SubElement(lg, 'l')
    l.text = words
    l.attrib['n'] = str(lCount)
    lCount = lCount + 1

###------------------------------------------------output nice XML
newXml = readableXML(tei)
redux = newXml.replace('&amp;', '&') #re-encodes escaped characters (there's probably a way to do this in the previous line)
redux = redux.replace('tei:TEI', 'TEI')
#redux = redux.replace('xmlns:tei', 'xmlns') #interesting: this deletes the namespace map and prepends 'tei:' to all tags
print redux 

#testing output
#ET.ElementTree(tei).write('output2.xml',encoding='UTF-8')
#print 'wrote output2.xml\n'

###-------------------------------------------------write the file
#tree = ET.fromstring(newXml.encode('UTF-8'))
tree = ET.fromstring(redux.encode('UTF-8'))
#ET.ElementTree(tree).write('outputPretty.xml',encoding='UTF-8')
ET.ElementTree(tree).write(fout,encoding='UTF-8')
print 'wrote '+fout+'\n\nPlease note, the file may require further human editing, including the replacement of incorrectly escaped characters, the removal of incorrect namespace identifiers, or the addition of namespace identifiers, eg xmlns="http://www.tei-c.org/ns/1.0".'