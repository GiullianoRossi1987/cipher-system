# coding = utf-8
# using namespace std
import json
import os
from string import ascii_letters, whitespace

"""[summary]
"""

letters_array = [x for x in ascii_letters]
letters_array.append(whitespace)


class CipherCreator(object):

    """CipherCreator
    :cvar inner_data : All the coding data in the file.
    :cvar file_name : The file name to the path ./lib-cipher .
    """
    inner_data = dict()
    file_name = str

    class CipherExistsError(BaseException):
        args : object = "This Cipher already exists in the system!"

    class InvalidData(TypeError):
        args : object = "This's a not valid data!"

    @staticmethod
    def check_cipher_exists(cipher: str) -> bool:
        """
        Checks if the file exists in the lib dir.
        :param cipher: The cipher name to verify.
        :return: If the file's in the dir.
        """
        if ".json" not in cipher: cipher += ".json"
        return cipher in os.listdir("./lib-cipher")

    def __init__(self, cipher_name: str):
        """
        Starts the creator setting the cipher name.
        :param cipher_name:  The name of the cipher.
        """
        if self.check_cipher_exists(cipher_name):
            raise self.CipherExistsError()
        self.file_name = cipher_name + ".json"

    def add_values(self):
        """
        It add the values to the inner_data.

        """
        # the encoding vls
        encoding  = {}
        decoding = {}
        for lt in letters_array:
            vl = input(f"The value to the letter [{lt}]: ")
            encoding[lt] = vl
        for v1, v2 in encoding:
            decoding[v2] = v1
        self.inner_data["Encoding"] = encoding
        self.inner_data["Decoding"] = decoding
        self.inner_data["Author"] = str(input("Your author name to the cipher: "))
    











