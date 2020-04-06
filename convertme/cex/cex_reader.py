from convertme import ReaderInterface, Dataset
from xml.etree.ElementTree import parse


class CexReader(ReaderInterface):

    def read(self, file):
        tree = parse(file)
        root = tree.getroot()

        # presume only one context per file
        context = root.find('Contexts').find('Context')

        # read attributes
        xml_attributes = context.find('Attributes')
        attributes = []

        # identifer-name dictionary for attributes
        attrib_dict = {}

        for attr in xml_attributes.findall('Attribute'):
            name = attr.find('Name').text
            attributes.append(name)
            identifier = attr.get('Identifier')
            attrib_dict.update({identifier: name})

        # incidency
        bools = []

        # read objects
        xml_objects = context.find('Objects')

        objects = []

        for obj in xml_objects.findall('Object'):
            name = obj.find('Name').text
            objects.append(name)

            intent = []

            # read intent
            for attr in obj.find('Intent'):
                intent.append(attrib_dict[attr.get('AttributeIdentifier')])

            bools.append([attrib in intent for attrib in attributes])

        return Dataset(objects, attributes, bools)
