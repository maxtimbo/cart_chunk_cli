import struct

def read_chunk_header(file):
    # Read 8 bytes for chunk ID and size
    header = file.read(8)
    if len(header) < 8:
        return None, None
    chunk_id, chunk_size = struct.unpack('4sI', header)
    return chunk_id, chunk_size

def read_xml_data(file):
    with open(file, 'rb') as f:
        # Read the entire file
        file_data = f.read()

    # Find the start of the XML section
    xml_start = file_data.find(b'_PMX')
    if xml_start == -1:
        raise ValueError("No XML data found in the file")

    # Extract XML data
    xml_data = file_data[xml_start:]
    xml_str = xml_data.decode('utf-8', errors='ignore')
    return xml_str

# Example usage
file_path = 'working.wav'
xml_content = read_xml_data(file_path)
print(xml_content)
