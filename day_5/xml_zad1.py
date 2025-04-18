#  xml
# xml używa tagów

from xml.dom import minidom

root = minidom.Document()
xml = root.createElement('root')
root.appendChild(xml)

productChild = root.createElement("product")
productChild.setAttribute("name", 'RAJ')
xml.appendChild(productChild)

xml_str = root.toprettyxml(indent="\t")
print(xml_str)
# <?xml version="1.0" ?>
# <root>
# 	<product name="RAJ"/>
# </root>

save_path = 'raj.xml'
with open(save_path, "w") as f:
    f.write(xml_str)
