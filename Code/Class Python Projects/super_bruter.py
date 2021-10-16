import hashlib

with open("shadow.txt", "r") as fShadow:
    for line in fShadow:
        with open("pass_list.txt", "r") as wordlist:
            for password in wordlist:
                hashed = hashlib.md5(password[:-1].encode("UTF-8")).hexdigest()
                print(f"{hashed}    {password[:-1]}")
                if hashed == line[:-1]:
                    print(f"\n\n\t\t\t\tCRACKED\n\n{hashed}    {password[:-1]}\n\nThe password is {password}")
                    quit()

