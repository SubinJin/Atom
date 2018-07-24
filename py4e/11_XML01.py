import xml.etree.ElementTree as ET

data = '''
<person>
    <name>Subin</name>
    <phone type = 'intl'>
        +82 5674 7829
    </phone>
    <email hide = 'yes'/>
</person>'''

tree = ET.fromstring(data)
print('Name', tree.find('name').text)
print('Attr', tree.find('email').get('hide'))
