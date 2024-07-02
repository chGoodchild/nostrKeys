import json
from nostr.key import PrivateKey
from mnemonic import Mnemonic


def generate_keypair_and_mnemonic():
    # Generate a new private key
    pk = PrivateKey()

    # Get the public key in bech32 format
    npub = pk.public_key.bech32()

    # Get the private key in bech32 format
    nsec = pk.bech32()

    # Convert the private key to a hex string
    private_key_hex = pk.hex()

    # Generate the BIP39 mnemonic phrase from the private key hex
    byte_value = bytes.fromhex(private_key_hex)
    mnemo = Mnemonic("english")
    mnemonic_phrase = mnemo.to_mnemonic(byte_value)

    # Create the output dictionary
    output = {
        "npub": npub,
        "nsec": nsec,
        "bip39_mnemonic": mnemonic_phrase
    }

    return output

if __name__ == "__main__":
    # Generate the key pair and mnemonic
    keypair_and_mnemonic = generate_keypair_and_mnemonic()

    # Print the output as JSON
    print(json.dumps(keypair_and_mnemonic, indent=4))

