import sys
import pprint
try:
    from urlparse import parse_qs
except ImportError:
    from urllib.parse import parse_qs


def main(args):
    # Make sure we have only one arg, the URL
    if len(args) != 1:
        sys.exit("This script requires exactly one argument")

    # Make sure the argument have a : symbol
    if args[0].find(":") < 0:
        sys.exit("The argument is a url and requires the symbol ':'")

    # Parse the URL
    protocol, fullPath = args[0].split(":", 1)

    # If there is a querystring, parse it
    if fullPath.find("?") >= 0:
        path, fullArgs = fullPath.split("?", 1)
        action = path.strip("/")
        params = parse_qs(fullArgs)
    else:
        action = fullPath.strip("/")
        params = ""

    # This is where you can do something productive based on the params and the
    # action value in the URL. For now we'll just print out the contents of the
    # parsed URL.
    fh = open('output.txt', 'w')
    fh.write(pprint.pformat((protocol, action, params)))
    fh.close()


# if __name__ == '__main__':
#     # sys.exit(main(sys.argv[1:]))
#     main()