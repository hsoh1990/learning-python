from Crypto.Hash import MD5, SHA512

hash_md5 = MD5.new()  # MD5를 이용한다.
hash_md5.update(b'hamegg')  # 문자열을 바이트 문자열로 전달해야 한다.
hash_md5.hexdigest()

hash_sha512 = SHA512.new()  # SHA-512를 이용한다.
hash_sha512.update(b'ham')
hash_sha512.hexdigest()

hash_md5 = MD5.new(b'hamegg')  # 인스턴스를 생성할 때 데이터도 전달할 수 있다.
hash_md5.hexdigest()
hash_md5 = MD5.new(b'ham')
hash_md5.hexdigest()

hash_md5.update(b'egg')  # update 함수는 추가로 작성한다.
hash_md5.hexdigest()  # b'ham'과 b'egg'가 연결되어 b'hamegg'가 되었다.
