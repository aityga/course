import hashlib
import json
import os
from pprint import pprint as pp


class Block:

    def __init__(self):
        self.blockchain_dir = os.curdir + '/blockchain/'

    def get_hash(self, filename):
        file = open(blockchain_dir + filename, 'rb').read()
        return hashlib.md5(file).hexdigest()

    def get_files(self):
        files = os.listdir(blockchain_dir)
        return sorted([int(i) for i in files])

    def check_integrity(self):
        files = get_files()
        results = []
        for file in files[1:]:
            f = open(blockchain_dir + str(file))
            h = json.load(f)['hash']
            prev_file = str(file - 1)
            actual_hash = get_hash(prev_file)
            if h == actual_hash:
                res = 'ok'
            else:
                res = 'changed'
            results.append({'block': prev_file, 'result': res})
        # print(f'Block {prev_file} is {res}')
        return results

    def write_block(name, amount, to_who, prev_hash=''):
        files = get_files()
        prev_file = files[-1]
        filename = str(prev_file + 1)
        prev_hash = get_hash(str(prev_file))
        data = {
            'name': name,
            'amount': amount,
            'to_who': to_who,
            'hash': prev_hash
        }
        with open(blockchain_dir + filename, 'w') as file:
            json.dump(data, file, indent=4, ensure_ascii=False)

    def main(self):
        pp(check_integrity())

    # write_block(name='ait', amount=200, to_who='myr')

    if __name__ == "__main__":
        main()
