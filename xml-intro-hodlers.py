import xml.etree.ElementTree as ET

tree = ET.parse('hodlers.xml')
root = tree.getroot()

# check out the .tostring() method
#print(ET.tostring(root))

# how to get an attribute
coin = root.get('coin')
#print('Crpto name = {val}'.format(val=coin))

# set an attribute: use .set()
root.set('launched', '20210101')
#print(root.attrib)

# to save the change, use the .write() method
#tree.write('hodlers.xml')

### second part
# add an 'id' element to each investor, using findall & set
'''
id = 1
for investor in tree.findall('investor'):
    investor.set('id', str(id))
    id += 1
# save to file
tree.write('hodlers.xml')
'''
'''
# delete/modify attributes
for investor in tree.findall('investor'):
    del(investor.attrib['id'])
# save to file
tree.write('hodlers.xml')
'''
'''
# add new investors #1 - from a literal string
investor1 = ET.fromstring('<investor>Allen Duffy</investor>')
root.append(investor1)
#save
tree.write('hodlers.xml')
'''
'''
# add new investors # 2 - use element constructor 
investor2 = ET.Element('investor')
investor2.text = 'Karl Amber'
root.append(investor2)

#s save to file
tree.write('hodlers.xml')'''

'''# demo selecting nodes by paths
# add ids again, but this time with iterator
for (id, investor) in enumerate(root.findall('investor')):
    investor.set('id', str(id))

# save
tree.write('hodlers.xml')
'''
'''# select first investor element with id=4
investor = root.find('.//investor[@id="4"]')
print(investor.text)
'''
# to select multiple elements, use findall:
for investor in root.findall('.//investor'):
    for i in range(1,10, 2):
        print(str(i))
        if investor.get('id') == i:
            print('Take 2:',investor.text)
for i in range()