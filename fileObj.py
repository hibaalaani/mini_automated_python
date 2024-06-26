# f = open("test.txt", "r")
# print(f.name)
# f.close()
#  other best way


# with open("test.txt", "r") as f:
# print(f.readline()) one way not efficient
# for line in f:
# print(line, end=''), """ no memory issue """
with open("test2.txt", "r") as rf:

    # f.write("size_to_read")
    # f.seek(0) # to move the cursor to the start of the file
    # f.write("size_to_read")
    with open("test_copy.txt", 'w') as wf:
        for line in rf:
            wf.write(line)
# to copy image file , we need to add b for binary mode

with open("dfdf.jpg", "rb") as rfb:
    with open("dewcx.jpg", "wb") as wfb:
        chunk_size = 4096
        rfb_chunk = rfb.read(chunk_size)
        while len(rfb_chunk) > 0:
            wfb.write(rfb_chunk)
            rfb_chunk = rfb.read(chunk_size)
        # for line in rfb:
        #     wfb.write(line)
