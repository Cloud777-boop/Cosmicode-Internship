import hashlib
import itertools
import string

# === CONFIGURABLE ===
charset = string.ascii_lowercase + string.digits  # you can expand to include symbols or uppercase
max_length = 5  # longer length = more time

# Load hashes from file
with open("hashes.txt", "r") as file:
    target_hashes = [line.strip().lower() for line in file]

print(f"Loaded {len(target_hashes)} hashes.")

# Store cracked passwords
cracked = {}

# Start brute-forcing
for length in range(1, max_length + 1):
    print(f"[*] Trying length: {length}")
    for combo in itertools.product(charset, repeat=length):
        candidate = ''.join(combo)
        hashed_candidate = hashlib.sha256(candidate.encode()).hexdigest()

        if hashed_candidate in target_hashes and hashed_candidate not in cracked:
            print(f"[+] Cracked: {candidate} -> {hashed_candidate}")
            cracked[hashed_candidate] = candidate

        if len(cracked) == len(target_hashes):
            print("[+] All hashes cracked.")
            break
    else:
        continue
    break

# Print summary
print("\n==== Summary ====")
for h in target_hashes:
    if h in cracked:
        print(f"{h} -> {cracked[h]}")
    else:
        print(f"{h} -> Not cracked")
