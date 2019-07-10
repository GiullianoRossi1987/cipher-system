# coding = utf-8
# using namespace std
import json
from typing import AnyStr

"""
"""


class Decoder(object):
    """

    """
    all_alphabet = dict
    cipher_using = AnyStr
    got_data = False

    class EmptyDataError(BaseException):
        args: object = "The system can't do this action without the main data!"

    def __init__(self, cipher_:AnyStr):
        self.cipher_using = "./lib-cipher/"+cipher_
        with open(self.cipher_using, "r") as cipher:
            self.all_alphabet = json.loads(cipher.read())
        self.got_data = True

    def decode(self, text_coded: AnyStr) -> str:
        """
        Decode a text data.
        :param text_coded: The text to decode.
        :return: The text decoded .
        :type text_coded: basestring.
        :rtype: str.
        """
        if not self.got_data:
            raise self.EmptyDataError()
        result = ""
        for lt in text_coded:
            result += self.all_alphabet["Decoding"][lt]
        return result


class Encoder(object):
    """

    """
    all_alphabet = dict()
    cipher_string = AnyStr
    got_data = False

    class EmptyDataError(BaseException):
        args: object = "The system can't do this action without the main data!"

    def __init__(self, cipher: AnyStr):
        """
        Get the cipher data from a file in the lib.
        :param cipher: The cipher to get data
        """
        self.cipher_string = "./lib-cipher/"+cipher
        with open(self.cipher_string, "r") as cipher_file:
            self.all_alphabet = json.loads(cipher_file.read())
        self.got_data = True
















