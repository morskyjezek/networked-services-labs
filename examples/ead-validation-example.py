## validate XML with python lxml

# import lxml & os.path for file handling
from lxml import etree
from os import getcwd
import os.path

# write a function that will do the validation
def validateEAD(ead_path):
    '''This function parses an ElementTree object and validates it against the EAD 3 schema.
    The response will tell you if the object is valid, and will show the error message if it is not.

    Usage:
    takes an ElementTree object (parsed xml) and a path object
    '''
    # load the XSD for validation - this uses the parse method, 
    # then pass the parsed structure to the special .XMLSchema method
    cwd = getcwd()
    parent_dir = os.path.split(cwd)[0]
    ead_xsd_schema_doc = os.path.join(parent_dir,'networked-services-labs-2022','data','xml','ead3.xsd')

    if os.path.isfile(ead_xsd_schema_doc):
        ead_schema_parsed = etree.parse(ead_xsd_schema_doc)
        ead_schema = etree.XMLSchema(ead_schema_parsed)
        print(f'Found the XSD for validation: { ead_xsd_schema_doc }\n')
    else:
        print('ERROR: Could not find the XSD for validation.')
        print(ead_xsd_schema_doc)
        
    # load and parse the selected XML doc
    ead_to_validate = etree.parse(ead_path)
    print(f'Evluating { ead_path }')

    # then validate the document and output a response
    if ead_schema.validate(ead_to_validate) == True:
        print(f'The document ({ ead_path }) is a valid EAD XML document.')
    elif ead_schema.validate(ead_to_validate) == False:
        print(f'The document ({ ead_path }) is INVALID.\n')
        print(ead_schema.assertValid(ead_to_validate))


## specify a document to validate (for the test, you should know if it is well formed or not . . . )
# try with an invalid file: what is the problem?
cwd = getcwd()
parent_dir = os.path.split(cwd)[0]
ead1_to_validate = os.path.join(parent_dir,'networked-services-labs-2022','data','xml','superior-papers.xml')

validateEAD(ead1_to_validate)

print('\n---- #### ----\n')

#ead2_to_validate = 'superior-papers-auto-generated.xml'
#validateEAD(ead2_to_validate)