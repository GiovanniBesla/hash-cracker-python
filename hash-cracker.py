import argparse
import hashlib

def parse_args():
    parser = argparse.ArgumentParser(description='')
    parser.add_argument('-w', '--wordlist', type=str, help='Path to wordlist file', metavar='[wordlist.txt]')
    parser.add_argument('-H', '--hash', type=str, help='Hash string to crack', metavar='[hash]')
    parser.add_argument('-a', '--algorithm', type=int, help='Algorithm to use', metavar='[algorithm_number]')
    parser.add_argument('-l', '--list', required=False, help='List available algorithms', action='store_true')
    args = parser.parse_args()
    return args

def main():
    args = parse_args()

    if(args.list):
        print_algorithm_list()
        exit(0)

    if args.wordlist is None or args.hash is None or args.algorithm is None:
        print('Missing arguments, use -h for usage.')
        exit(1)

    hash_algorithm = get_algorithm_name(args.algorithm)    
    words = get_words_from_file(args.wordlist)

    animation_counter = 0
    animation = ['|', '/', '-', '\\']

    for word in words:
        animation_counter += 1
        print("Cracking Hash...", animation[animation_counter % len(animation)], end="\r")
        hashed_word = hash_algorithm(word.encode('utf-8')).hexdigest()
        if hashed_word == args.hash:
            print(f'Hash cracked succesfully: {word}')
            exit(0)
    
    print('Could not crack hash')

def get_words_from_file(path):
    words = []
    with open(path, 'r') as f:
        for line in f:
            words.append(line.strip())
    return words

def get_algorithm_name(algorithm_number):
    algroithms = {
        1: hashlib.md5,
        2: hashlib.sha1,
        3: hashlib.sha224,
        4: hashlib.sha256,
        5: hashlib.sha384,
        6: hashlib.sha512,
        7: hashlib.blake2b,
        8: hashlib.blake2s,
        9: hashlib.sha3_224,
        10: hashlib.sha3_256,
        11: hashlib.sha3_384,
        12: hashlib.sha3_512,
        13: hashlib.shake_128,
        14: hashlib.shake_256
    }

    return algroithms[algorithm_number]

def print_algorithm_list():
        print('Available algorithms:')
        print(' 1. md5')
        print(' 2. sha1')
        print(' 3. sha224')
        print(' 4. sha256')
        print(' 5. sha384')
        print(' 6. sha512')
        print(' 7. blake2b')
        print(' 8. blake2s')
        print(' 9. sha3_224')
        print('10. sha3_256')
        print('11. sha3_384')
        print('12. sha3_512')
        print('13. shake_128')
        print('14. shake_256')
        exit(0)


main()
