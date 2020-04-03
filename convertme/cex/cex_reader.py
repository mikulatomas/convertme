from convertme import ReaderInterface, Dataset
from xml.etree.ElementTree import parse

class CexReader(ReaderInterface):

    # TODO add file validation ?
    def read(self, file) -> Dataset:
        tree = parse(file)
        root = tree.getroot()
        # presume only one context per file
        context = root.find('Contexts').find('Context')
        
        # TODO if we are going to us only order of attributes (ie not their identifiers),
        # then simple list can be used instead of dict (filled in order,
        #  indexed by object's hasAttribute identifiers)

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
        
        # TODO can contain more contexts?
        # TODO reads in order from xml file, but order can be changed
        # should attributes order be given by identifiers or by order in file?
        # concept-explorer ignores the identifiers and uses order in file instead
        # therefore use order for both objects and attributes?

        # Moreover cex does not have to contain 
        # <Lattices /> and identifiers for contexts and attributes
        # or might contain some other elements (ie <RecalculationPolicy Value="Clear" />)
        
        # should put them in the writer in this empty form ?
        # at least conexp 1.5 notices if <Lattices /> is missing.

        # It seems that only important part for us is content of <attributes> and <objects> 
        # I am still not sure how (or even if) identifiers are used.
        return Dataset(objects,attributes,bools,"")