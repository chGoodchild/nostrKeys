# Interesting Other Stuff

# Environment

Make sure you set up your virtual environment first

```
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

# Useful scripts

The `generate_npub.py` script can either generate a new keypair and mnemonic or take an existing mnemonic as an input and return the corresponding keypair.

## Example usage

To generate a new keypair and mnemonic:
```
python scripts/generate_npub.py
```

The resulting output will look like this:
```
{
    "npub": "npub1dycs3djwma96kpaf68s8047k0z2fe2rnm5p6eecwtgsadhqf5xrqkzqug9",
    "nsec": "nsec16qy5a9egwe28wduv975rcgvfnzswnk4pvs2v0dq7x5qyemqkrzysvw64d5",
    "bip39_nsec": "source engine place extend grab describe taste magnet popular three give course attend unhappy machine little sibling path minute above solution arch giraffe call"
}
```

To use an existing mnemonic to get the corresponding keypair:
```
python scripts/generate_npub.py "source engine place extend grab describe taste magnet popular three give course attend unhappy machine little sibling path minute above solution arch giraffe call"
```

The resulting output will look like this:
```
{
    "npub": "npub1dycs3djwma96kpaf68s8047k0z2fe2rnm5p6eecwtgsadhqf5xrqkzqug9",
    "nsec": "nsec16qy5a9egwe28wduv975rcgvfnzswnk4pvs2v0dq7x5qyemqkrzysvw64d5",
    "bip39_nsec": "source engine place extend grab describe taste magnet popular three give course attend unhappy machine little sibling path minute above solution arch giraffe call"
}
```
