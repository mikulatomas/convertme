from convertme import WriterInterface, Dataset
import xml.etree.ElementTree as ET

class CexWriter(WriterInterface):

    def write(self, dataset: Dataset, output):
        # basic cex structure
        root = ET.Element("ConceptualSystem")
        version = ET.SubElement(root, "Version")
        version.set("MajorNumber", "1")
        version.set("MinorNumber", "0")
        contexts = ET.SubElement(root, "Contexts")
        context = ET.SubElement(contexts, "Context")
        context.set("Type", "Binary")
        context.set("Identifier", "0")    
        attributes = ET.SubElement(context, "Attributes")
        objects = ET.SubElement(context, "Objects")
        ET.SubElement(root, "Lattice")

        # write attributes
        for index, attr in enumerate(dataset.attributes):
            xml_attr = ET.SubElement(attributes, "Attribute")
            xml_attr.set("Identifier", str(index))
            attr_name = ET.SubElement(xml_attr, "Name")
            attr_name.text = str(attr)

        # wrtie objects
        for index, obj in enumerate(dataset.objects):
            xml_obj = ET.SubElement(objects, "Object")
            obj_name = ET.SubElement(xml_obj, "Name")
            obj_name.text = str(obj) 
            intent = ET.SubElement(xml_obj, "Intent")
            # write incidency
            for attr_index, attr in enumerate(dataset.bools[index]):
                if attr:
                    xml_attr = ET.SubElement(intent, "HasAttribute")
                    xml_attr.set("AttributeIdentifier", str(attr_index))

        xml_str = ET.tostring(root, encoding='unicode', method='xml')
        output.write(xml_str)