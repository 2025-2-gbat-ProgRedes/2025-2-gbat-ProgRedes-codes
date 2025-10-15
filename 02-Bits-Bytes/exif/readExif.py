def decode_metadata(metadata):
    id_metadata = int.from_bytes(metadata[:2], endianess)
    tipo_metadata = int.from_bytes(metadata[2:4], endianess)
    repeats = int.from_bytes(metadata[4:8], endianess)
    value_metadata = metadata[8:]
    print (f"0x{id_metadata:x} {tipo_metadata}" +
           f"{repeats} {value_metadata}")

def read_metadata(metadata_pos):
    fd.seek (metadata_pos)
    num_metadata = int.from_bytes(fd.read(2), endianess)
    for _ in range(num_metadata):
        decode_metadata(fd.read(12))

def readExif():
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
    
def main(file_name):
    global fd
    
    fd = open (file_name, "rb")
    if not (fd.read(2) == b"\xFF\xD8"):
        raise Exception("Não é imagem JPG!")
    
    sectionHeader = fd.read(2)
    if sectionHeader == b"\xFF\xE1":
        readExif()
    else:
        raise Exception("Não tem EXIF!")
    fd.close()

if __name__ == '__main__':
    try:
        main("Tania.jpg")
    except Exception as e:
        print (f"Erro: ", e)