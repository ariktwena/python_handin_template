from modules import webget
import requests
from concurrent.futures import ThreadPoolExecutor
import io
from concurrent.futures import ProcessPoolExecutor
import multiprocessing

class NotFoundException(Exception):
    """Base class for other exceptions"""
    pass


class TextComparer():

    def __init__(self, url_list = []):
        self.url_list = url_list

    def get_list(self):
        return self.url_list

    def create_filename(self, url):
        url_tokens = url.split('//')
        url_words = url_tokens[1].split("/")
        filename = ''
        if len(url_words) == 1:
            filename = str(url_words[0])
        else:
            filename = str(url_words[0]) + '-' + str(url_words[len(url_words) - 1])
        filename = filename.replace('.', '-')
        return filename

    def download(self, url, filename = 'default'):
        filename_to_save = ''

        if filename == 'default':
            filename_to_save = self.create_filename(url)
        else:
            filename_to_save = filename


        filename_to_save = filename_to_save + ".txt"
        r = requests.get(url)
        try:
            if r.status_code == 404:
                raise NotFoundException
            else:
                webget.download(url, to=filename_to_save)
                return filename_to_save
        except NotFoundException:
            print('Exception occurred with status code: ' + str(r.status_code))

    def multithreading(self, func, args=[], workers=5):

        if len(args) == 0:
            args = self.url_list

        if len(args) > 5:
            workers = len(args)

        with ThreadPoolExecutor(workers) as ex:
            res = ex.map(func, args)
        return list(res)

    def read_files_from_list(self, list):

        read_list = {}

        for filename in list:
            file = io.open(filename, mode="r", encoding="utf-8")
            read_list[filename] = file.read()

        return read_list

    def __iter__(self):
        self.current = 0
        return self

    def __next__(self):
        try:
            if self.current < len(self.url_list):
                self.current += 1
                return self.url_list[self.current - 1]
            else:
                raise StopIteration
        except StopIteration:
            print("No more url's in the list")

    def urllist_generator(self):
        current = 0
        try:
            while (current < len(self.url_list)):
                yield self.url_list[current]
                current += 1
            raise StopIteration
        except StopIteration:
            print("No more url's in the list")



    def read_vowel(self, dict):

        read_vowel_list = {}

        for key, value in dict.items():
            file = io.open(key, mode="r", encoding="utf-8")
            content = file.read()
            content = content.replace('\n', '')
            words = content.split(' ')
            vowel = 0
            for word in words:
                for letter in word:
                    if letter in ['a', 'e', 'i', 'o', 'u', 'y', 'æ', 'ø', 'å']:
                        vowel += 1

            avg_vowel = vowel/len(words)

            read_vowel_list[key] = avg_vowel

        return read_vowel_list

    def multiprocess(self, func, args, workers=multiprocessing.cpu_count()):
        with ProcessPoolExecutor(workers) as ex:
            res = ex.map(func, args)
        return list(res)

    def hardest_read(self, list_element):

        key = list_element[0]
        value = list_element[1]

        content = value.replace('\n', '')
        words = content.split(' ')
        vowel = 0
        for word in words:
            for letter in word:
                if letter in ['a', 'e', 'i', 'o', 'u', 'y', 'æ', 'ø', 'å']:
                    vowel += 1

        avg_vowel = vowel / len(words)

        return {key:avg_vowel}