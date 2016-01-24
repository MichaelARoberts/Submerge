from sys import argv
import utility.hex_util as hex_util
import utility.hash_util as hash_util

args = argv

prompt = '> '
count = 1

for arg in args[1:]:
    nextArg = args[count+1]

    # Getting an unsplit hex string from file
    if str(arg) == 'hex':
        print('{}Creating Hex Values for file "{}"'.format(prompt, nextArg))
        print(hex_util.get_file_hex(nextArg))

    # Getting split hex string from file
    if str(arg) == 'bhex':
        print('{}Creating Beautiful Hex Values for file "{}"'.format(prompt, nextArg))

        new_hex = hex_util.beautiful_hex(nextArg)

        if new_hex:
            print(new_hex)

    if str(arg) == 'uhex':
        print('{}Creating string from hex data...'.format(prompt))
        print(hex_util.hex_to_string(nextArg))

    count += 1

    if (len(args)) == count + 1:
        break
