import string
def generate_alphanum():
    count = 1;
    while True:
        for c in string.ascii_lowercase:
            yield ''.join((c,str(count)))
        count += 1


def main(script, n='6', *args):
    c = 0
    for t in generate_alphanum():
        c += 1
        print(t)
        if(c > 100):
            break


if __name__ == '__main__':
    import sys
    main(*sys.argv)

