from convertme import WriterInterface, Dataset
import xml.etree.ElementTree as ET


class CexWriter(WriterInterface):

    def write(self, dataset, output):
        # basic cex structure
        root = ET.Element("ConceptualSystem")

        version = ET.SubElement(root, "Version")
        version.set("MajorNumber", "1")
        version.set("MinorNumber", "0")

        contexts = ET.SubElement(root, "Contexts")
        context = ET.SubElement(contexts, "Context")
        context.set("Identifier", "0")
        context.set("Type", "Binary")

        attributes = ET.SubElement(context, "Attributes")
        objects = ET.SubElement(context, "Objects")

        ET.SubElement(root, "Lattices")

        # write attributes
        for idx, attr in enumerate(dataset.attributes):
            xml_attr = ET.SubElement(attributes, "Attribute")
            xml_attr.set("Identifier", str(idx))

            attr_name = ET.SubElement(xml_attr, "Name")
            attr_name.text = str(attr)

        # wrtie objects
        for idx, obj in enumerate(dataset.objects):
            xml_obj = ET.SubElement(objects, "Object")

            obj_name = ET.SubElement(xml_obj, "Name")
            obj_name.text = str(obj)

            intent = ET.SubElement(xml_obj, "Intent")

            # write incidency
            for attr_index, attr in enumerate(dataset.bools[idx]):
                if attr:
                    xml_attr = ET.SubElement(intent, "HasAttribute")
                    xml_attr.set("AttributeIdentifier", str(attr_index))

        xml_header = "<?xml version=\"1.0\" encoding=\"UTF-8\"?>"

        xml_str = ET.tostring(root, encoding='unicode',
                              method='xml', short_empty_elements=False)

        output.write(xml_header + xml_str)
