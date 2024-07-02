import json
from nostr.key import PrivateKey
from mnemonic import Mnemonic


def generate_private_key():
    # Generate a new private key
    pk = PrivateKey()
    entropy = pk.raw_secret  # Get the raw entropy used to generate the private key
    return pk, entropy

def mnemonic_from_entropy(entropy):
    mnemo = Mnemonic("english")
    mnemonic_phrase = mnemo.to_mnemonic(entropy)
    return mnemonic_phrase

def entropy_from_mnemonic(mnemonic_phrase):
    mnemo = Mnemonic("english")
    entropy = mnemo.to_entropy(mnemonic_phrase)
    return entropy


def nsec_from_mnemonic(mnemonic):
    pass

def generate_keypair_and_mnemonic():
    # Generate a new private key
    pk, entropy = generate_private_key()

    # Get the public key in bech32 format
    npub = pk.public_key.bech32()

    # Get the private key in bech32 format
    nsec = pk.bech32()

    output = {
        "npub": npub,
        "nsec": nsec,
        "entropy": str(entropy),
        "bip39_nsec": mnemonic_from_entropy(entropy),
        "entropy_from_mnemonic": str(entropy_from_mnemonic(mnemonic_from_entropy(entropy))),
        "nsec_from_mnemonic": nsec_from_mnemonic(mnemonic_from_entropy(entropy))
    }

    return output

if __name__ == "__main__":
    # Generate the key pair and mnemonic
    keypair_and_mnemonic = generate_keypair_and_mnemonic()

    # Print the output as JSON
    print(json.dumps(keypair_and_mnemonic, indent=4))

