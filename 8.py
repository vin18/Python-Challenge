import gzip, io
import zlib, base64

un = b'BZh91AY&SYA\xaf\x82\r\x00\x00\x01\x01\x80\x02\xc0\x02\x00 \x00!\x9ah3M\x07<]\xc9\x14\xe1BA\x06\xbe\x084'

unS = base64.b64decode(un).decode('utf-8')
#unS = un.decode('base64')
#unS = gzip.GzipFile(fileobj=io.BytesIO(un)).read()

print (unS)
