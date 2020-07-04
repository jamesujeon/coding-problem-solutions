# 문제 링크: https://leetcode.com/problems/encode-and-decode-tinyurl/

import string

class Codec:
    BASE_CHARS = string.digits + string.ascii_letters
    BASE = len(BASE_CHARS)

    def __init__(self):
        self.urls = []

    def encode(self, longUrl: str) -> str:
        index = len(self.urls)
        if longUrl in self.urls:
            index = self.urls.index(longUrl)
        else:
            self.urls.append(longUrl)
        return f"http://tinyurl.com/{self.encode_base62(index + 1)}"

    def decode(self, shortUrl: str) -> str:
        index = self.decode_base62(shortUrl.split('/')[-1]) - 1
        return self.urls[index]

    def encode_base62(self, value: int) -> str:
        encoded_str = ''
        while value > 0:
            encoded_str += Codec.BASE_CHARS[int(value % Codec.BASE)]
            value //= Codec.BASE
        return encoded_str[::-1]

    def decode_base62(self, encoded_str: str) -> int:
        value = power = 0
        for ch in encoded_str[::-1]:
            value += Codec.BASE_CHARS.index(ch) * (Codec.BASE ** power)
            power += 1
        return value


# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.decode(codec.encode(url))