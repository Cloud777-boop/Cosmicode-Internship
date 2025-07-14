import hashlib

def hash_password(password):
    return hashlib.sha256(password.encode()).hexdigest()

def dictionary_attack(hashes_file, wordlist_file):
    # Read all known hashes from file
    with open(hashes_file, 'r') as f:
        hash_list = [line.strip() for line in f]

    # Read all passwords from the wordlist
    with open(wordlist_file, 'r') as f:
        passwords = [line.strip() for line in f]

    # Try each password against each hash
    for hash_val in hash_list:
        found = False
        for password in passwords:
            if hash_password(password) == hash_val:
                print(f"[+] Hash matched! Password: '{password}' -> {hash_val}")
                found = True
                break
        if not found:
            print(f"[-] No match found for hash: {hash_val}")

# Example usage
dictionary_attack('hashes.txt', 'wordlist.txt')
