import subprocess


def crack():
    # hashidentifier
    # john
    # etc.
    # input(hash)
    # demo hash 1e6681065a0ddfa80714a3df70438f12 md5
    # demo hash 0400774cdcab43bc634ae6e5d737e9b6c7c8e5e3 sha1
    hash = input("please add hash to crack: ")
    # demo
    hash = "1e6681065a0ddfa80714a3df70438f12"
    # hash-identifier
    print("For debugging it uses this hash: " + hash)

    # result = subprocess.run(["ls"], shell=True, capture_output=True, text=True)
    # print("XXXXXXXXX")
    # print(result)
    # print(result.stdout)

    p = subprocess.Popen(
        ["hash-identifier", hash],
        shell=True,
        text=True,
        stderr=subprocess.PIPE,
        stdout=subprocess.PIPE,
    )
    stdout, stderr = p.communicate()

    print(stdout)
