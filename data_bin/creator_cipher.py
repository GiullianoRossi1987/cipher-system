# coding = utf-8
# using namespace std
import json
import os
from string import ascii_letters, whitespace
from typing import AnyStr

"""[summary]
"""

letters_array = [x for x in ascii_letters]
letters_array.append(whitespace)


class DevConfigFile(object):
    """
    This class catch all the data in the developer config file in ./data_bin/dev-config.json.
    It's used to less work, 'cause i'm pretty lazy. Also this class checks if the file have
    the verified code.
    """
    main_data = dict()

    class InvalidDataMode(BaseException):
        args: object = "This file's not verified by our system!"

    def __init__(self, file_config = "./data_bin/dev-config.json"):
        with open(file_config) as fconf:
            self.main_data = json.loads(fconf.read())
        try:
            a = self.main_data["Verified"]
            del a
        except IndexError:
            raise self.InvalidDataMode()



class CipherCreator(object):

    """CipherCreator
    The class to the tool to create the ciphers.
    :cvar inner_data : All the coding data in the file.
    :cvar file_name : The file name to the path ./lib-cipher .
    """
    inner_data = dict()
    file_name = str
    __version__ = "alpha"

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
        And to add anything in the system
        """
        # the encoding vls
        encoding  = {}
        decoding = {}
        for lt in letters_array:
            c = True
            while True:
                vl = input(f"The value to the letter [{lt}]: ")
                # encoding[lt] = vl
                confirm = int(input("Confirm the value?\n[1]Y\n[2]N\n[3]Cancel\n>>> "))
                if confirm == 3:
                    c = False
                    break
                if confirm == 1: break
            if c:
                encoding[lt] = vl
            else:
                raise KeyboardInterrupt()
        for v1, v2 in encoding:
            decoding[v2] = v1
        self.inner_data["Encoding"] = encoding
        self.inner_data["Decoding"] = decoding
        c = True
        while True:
            author = input("Type your author name: ")
            confirm = int(input("Confirm the author name?\n[1]Y\n[2]N\n[3]Cancel\n>>> "))
            if confirm == 3:
                c = False
                break
            if confirm == 1: break
        if c:
            self.inner_data["Author"] = author
        else:
            raise KeyboardInterrupt()

    def create_file(self, dire="./lib-cipher"):
        """
        Create the cipher file and add the data to the file.
        :param dire: The directory to add the file.
        """
        os.system("touch "+dire+"/"+self.file_name)
        with open(dire+"/"+self.file_name, "w") as cipher_file:
            data_dumped = json.dumps(self.inner_data)
            cipher_file.write(data_dumped)
            del data_dumped


class CipherDevManagement(object):
    """
    Alter cipher data from a file.
    """
    main_cipher_file = AnyStr
    cipher_data = dict()
    got_data = False
    auto_save = bool

    class CorruptedData(BaseException):
        args: object = "This file data's corrupted!"

    class InvalidFileType(BaseException):
        args: object = "This file's not valid to the system!"

    class EmptyDataError(BaseException):
        args: object = "The system don't have data to do this action!"

    @classmethod
    def check_got_data(cls):
        """
        Checks if the data's empty in the system.
        :raise cls.EmptyDataError : Because the data's empty.
        """
        if not cls.got_data:
            raise cls.EmptyDataError()

    def __init__(self, file_to_man: str, dir_at="./lib-cipher", auto_saves = False):
        """
        Starts the management system at one file.
        :param file_to_man: The cipher file to manage.
        :param auto_saves : If the system will save the alterations automaticly
        """
        self.main_cipher_file = dir_at+"/"+file_to_man
        with open(self.main_cipher_file, "r") as file_cipher:
            self.cipher_data = json.loads(file_cipher.read())
        self.got_data = True
        self.auto_save = auto_saves

    @classmethod
    def update_file(cls):
        """
        That updates the cipher file content, for the newest in cls.cipher_data.
        """
        with open(cls.main_cipher_file, "w") as to_update:
            vl_dumped = json.dumps(cls.cipher_data)
            to_update.write(vl_dumped)
            del vl_dumped

    @classmethod
    def check_saves(cls):
        """
        Saves the file if auto saves is true.
        """
        cls.check_got_data()
        if cls.auto_save: cls.update_file()

    def alter_encoding_data(self, letter="*"):
        """
        Alter a letter in the encoding data.
        :param letter: The letter to alter. For alter all the letters use '*'.
        :type letter: str
        """
        if letter == "*":
            for lt in letters_array:
                c = True
                while True:
                    vl = str(input(f"Type the new value to the letter '{lt}': "))
                    confirm = int(input("Confirm?\n[1]Y\n[2]N\n[3]Cancel\n>>> "))
                    if confirm == 3:
                        c = False
                        break
                    if confirm == 1: break
                if c:
                    self.cipher_data["Encoding"][lt] = vl
                else:
                    raise KeyboardInterrupt()
        else:
            c = True
            while True:
                new_vl = str(input(f"Type the new value to the letter '{letter}': "))
                confirm = int(input("Confirm?\n[1]Y\n[2]N\n[3]Cancel\n>>> "))
                if confirm == 3:
                    c = False
                    break
                if confirm == 1: break
            if c:
                self.cipher_data['Encoding'][letter] = new_vl
            else:
                raise KeyboardInterrupt()
        self.check_saves()

    def alter_decoding_data(self, letter="*"):
        """
        Works like the alter_encoding_data, but with the decoding data.
        :param letter: The letter to alter.
        :type letter : str
        """
        if letter == "*":
            for lt in letters_array:
                c = True
                while True:
                    vl = str(input(f"Type the new value to the letter '{lt}': "))
                    confirm = int(input("Confirm?\n[1]Y\n[2]N\n[3]Cancel\n>>> "))
                    if confirm == 3:
                        c = False
                        break
                    if confirm == 1: break
                if c:
                    self.cipher_data["Decoding"][lt] = vl
                else:
                    raise KeyboardInterrupt()
        else:
            c = True
            while True:
                new_vl = str(input(f"Type the new value to the letter '{letter}': "))
                confirm = int(input("Confirm?\n[1]Y\n[2]N\n[3]Cancel\n>>> "))
                if confirm == 3:
                    c = False
                    break
                if confirm == 1: break
            if c:
                self.cipher_data["Decoding"][letter] = new_vl
            else:
                raise KeyboardInterrupt()
        self.check_saves()
