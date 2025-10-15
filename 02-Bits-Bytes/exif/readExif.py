import constants

def decode_metadata(metadata):
    tag_number = int.from_bytes(metadata[:2], endianess)
    tag_name = constants.TAG_NUMBER.get(tag_number, "Não ident.")
    
    tag_type  = int.from_bytes(metadata[2:4], endianess)
    tag_type_name = constants.TAG_TYPE.get(tag_type, "Não ident.")
    
    tag_reps = int.from_bytes(metadata[4:8], endianess)
    tag_value  = metadata[8:]
    print (f"{tag_name} (0x{tag_number:x}) "+
           f"{tag_type_name} ({tag_type}) " +
           f"{tag_reps} {tag_value}")

def read_metadata(metadata_pos):
    fd.seek (metadata_pos)
    num_metadata = int.from_bytes(fd.read(2), endianess)
    for _ in range(num_metadata):
        decode_metadata(fd.read(12))

def read_exif():
    global endianess, tiff_header_pos
    sec_len = fd.read(2)
    fd.seek(6, 1)   # pula o EXIF Header
    tiff_header_pos = fd.tell()
    tiff_header = fd.read(8)
    if tiff_header[:2] == b"\x4D\x4D":
        endianess = "big"
    elif tiff_header[:2] == b"\x49\x49":
        endianess = "little"
    else:
        raise ValueError ("Endianess inválida!!!")
    
    metadata_begin = int.from_bytes(tiff_header[4:], endianess)
    read_metadata(metadata_begin + tiff_header_pos)
    
def exif_show(file_name):
    global fd
    
    fd = open (file_name, "rb")
    if not (fd.read(2) == b"\xFF\xD8"):
        raise Exception("Não é imagem JPG!")
    
    sectionHeader = fd.read(2)
    if sectionHeader == b"\xFF\xE1":
        read_exif()
    else:
        raise Exception("Não tem EXIF!")
    fd.close()

if __name__ == '__main__':
    try:
        exif_show("Tania.jpg")
    except Exception as e:
        print (f"Erro: ", e)