import json
from nostr.key import PrivateKey
from mnemonic import Mnemonic


def mnemonic_to_public_key(mnemonic_phrase):
    # Convert the mnemonic phrase back to a byte array
    mnemo = Mnemonic("english")
    byte_value = mnemo.to_seed(mnemonic_phrase, passphrase="")[:32]  # Take the first 32 bytes as the private key
    private_key = PrivateKey(byte_value)
    public_key = private_key.public_key
    
    # Get the public key in bech32 format
    npub = public_key.bech32()
    
    return npub, public_key



def mnemonic_to_private_key(mnemonic_phrase):
    # Convert the mnemonic phrase back to a byte array
    mnemo = Mnemonic("english")
    byte_value = mnemo.to_seed(mnemonic_phrase, passphrase="")[:32]
    private_key = PrivateKey(byte_value)
    
    # Get the private key in bech32 format
    nsec = private_key.bech32()
    
    return nsec, private_key


def get_mnemonic(key):
    # Convert the private key to a hex string
    hx = key.hex()

    # Generate the BIP39 mnemonic phrase from the private key hex
    byte_value = bytes.fromhex(hx)
    mnemo = Mnemonic("english")
    mnemonic_phrase = mnemo.to_mnemonic(byte_value)
    return mnemonic_phrase


def generate_keypair_and_mnemonic():
    # Generate a new private key
    pk = PrivateKey()

    # Get the public key in bech32 format
    npub = pk.public_key.bech32()

    # Get the private key in bech32 format
    nsec = pk.bech32()

    # Create the output dictionary
    output = {
        "npub": npub,
        "nsec": nsec,
        # "bip39_npub": get_mnemonic(pk.public_key),
        "bip39_nsec": get_mnemonic(pk),
        # "new_npub": mnemonic_to_public_key(get_mnemonic(pk.public_key))[0],
        "new_nsec": mnemonic_to_private_key(get_mnemonic(pk))[0]
    }

    return output

if __name__ == "__main__":
    # Generate the key pair and mnemonic
    keypair_and_mnemonic = generate_keypair_and_mnemonic()

    # Print the output as JSON
    print(json.dumps(keypair_and_mnemonic, indent=4))

