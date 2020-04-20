

def pretty_save(element, file_path:str):
    with open(file_path, 'w') as xml_file:
        xml_file.write(element.toDOM().toprettyxml())