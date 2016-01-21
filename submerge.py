from sys import argv
import hex_util

args = argv

prompt = '> '
count = 0

for arg in args:

    if len(args) == count + 1:
        break
    else:
        nextArg = args[count + 1]

    # Getting an unsplit hex string from file
    if str(arg) == 'hex':
        print('{}Creating Hex Values for file "{}"...'.format(prompt, nextArg))
        print(hex_util.get_file_hex(nextArg))

    # Getting split hex string from file
    if str(arg) == 'bhex':
        print('{}Creating Beautiful Hex Values for file "{}"...'.format(prompt, nextArg))

        new_hex = hex_util.beautiful_hex(nextArg)

        if new_hex:
            print(new_hex)

    if str(arg) == 'uhex':
        print('{}Creating string from hex data...'.format(prompt))
        print(hex_util.hex_to_string(nextArg))

    count += 1
