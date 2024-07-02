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

def nsec_from_entropy(entropy):
    # Ensure the entropy is 32 bytes and a bytes object
    if isinstance(entropy, bytearray):
        entropy = bytes(entropy)
    if len(entropy) < 32:
        entropy = entropy.ljust(32, b'\x00')
    elif len(entropy) > 32:
        entropy = entropy[:32]

    pk = PrivateKey(entropy)
    return pk.bech32(), pk

def generate_keypair_and_mnemonic():
    # Generate a new private key and entropy
    pk, original_entropy = generate_private_key()

    # Get the public key in bech32 format
    npub = pk.public_key.bech32()

    # Get the private key in bech32 format
    nsec = pk.bech32()

    # Generate mnemonic from original entropy
    mnemonic = mnemonic_from_entropy(original_entropy)

    # Verify that the mnemonic can be converted back to the same entropy
    derived_entropy = entropy_from_mnemonic(mnemonic)
    assert original_entropy == derived_entropy, "Entropy mismatch!"

    derrived_nsec = nsec_from_entropy(derived_entropy)[0]
    assert nsec == derrived_nsec, "nsec mismatch!"

    # Create the output dictionary
    output = {
        "npub": npub,
        "nsec": nsec,
        "entropy": original_entropy.hex(),
        "bip39_nsec": mnemonic,
        "nsec_from_mnemonic": derrived_nsec
    }

    return output

def get_keypair_from_mnemonic(mnemonic):
    # Assume input is a seed phrase (mnemonic)
    original_entropy = entropy_from_mnemonic(mnemonic)

    # Get the private key and public key
    pk = nsec_from_entropy(original_entropy)[1]
    npub = pk.public_key.bech32()
    nsec = pk.bech32()

    # Generate mnemonic from original entropy
    derived_mnemonic = mnemonic_from_entropy(original_entropy)

    # Verify that the mnemonic can be converted back to the same entropy
    derived_entropy = entropy_from_mnemonic(derived_mnemonic)
    assert original_entropy == derived_entropy, "Entropy mismatch!"

    derrived_nsec = nsec_from_entropy(derived_entropy)[0]
    assert nsec == derrived_nsec, "nsec mismatch!"
    # Create the output dictionary
    output = {
        "npub": npub,
        "nsec": nsec,
        "entropy": original_entropy.hex(),
        "bip39_nsec": mnemonic,
        "nsec_from_mnemonic": derrived_nsec
    }
    
    return output

if __name__ == "__main__":
    import sys
    # Example usage
    input_value = sys.argv[1] if len(sys.argv) > 1 else "quiz brain company puzzle nut address country play fringe mansion torch critic clarify figure history two general blur fancy various check claim panther coffee"

    # keypair_and_mnemonic = generate_keypair_and_mnemonic()
    mnemonic = "oval stay develop alley embrace erase hill cabin alley deliver purpose light play renew begin thought heavy pact peace year sail lunch liar zero"
    keypair_and_mnemonic = get_keypair_from_mnemonic(mnemonic)

    # Print the output as JSON
    print(json.dumps(keypair_and_mnemonic, indent=4))

