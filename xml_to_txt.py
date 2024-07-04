import xml.etree.cElementTree as ET
import os

def xml_to_txt(xml_file, output_dir):
    
    tree=ET.parse(xml_file)
    root=tree.getroot()
    
    base_name = os.path.splitext(os.path.basename(xml_file))[0]
    txt_name = f"{base_name}.txt"
    txt_filepath = os.path.join(output_dir, txt_name)
    
    with open(txt_filepath, 'w') as txt_file:
        for obj in root.findall('object'):
            obj_name = obj.find('name').text
            bndbox = obj.find('bndbox')
            x1 = bndbox.find('xmin').text
            y1 = bndbox.find('ymin').text
            x2 = bndbox.find('xmax').text
            y2 = bndbox.find('ymax').text
            
            line = f"{obj_name} {x1} {y1} {x2} {y2}\n"
            txt_file.write(line)
            
            
xml_dir = 'data/annotations'
output_dir = 'data/labels'

for xml_file in os.listdir(xml_dir):
    if xml_file.endswith('.xml'):
        xml_to_txt(os.path.join(xml_dir, xml_file), output_dir)
        
print("всё гуд")

