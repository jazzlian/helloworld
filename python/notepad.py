import sys
import time

def usage():
    print("""
    Usage
    ======
    python3 %s -v : View Memo
    python3 %s -a : Add Meno
    """ % (sys.argv[0], sys.argv[0]))

if __name__ == '__main__':
    if not sys.argv[1:] or sys.argv[1] not in ['-v','-a']:
        usage()
    elif sys.argv[1] == '-v':
        try:
            print(open("memo.txt").read())
        except IOError:
            print("memo does not exists")
    elif sys.argv[1] == '-a':
        word = input("Enter memo: ")
        f = open("memo.txt", 'a')
        f.write(time.ctime() + ': ' + word + '\n')
        f.close()
        
        print("Addddded")