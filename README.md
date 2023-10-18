# Rainbow Table Generator and MD5 Hash Decryptor

This Python project is designed to generate rainbow tables for the MD5 hashing algorithm. It prompts the user to input a character set and the desired length of the passphrase, then proceeds to generate a rainbow table based on these specifications.

Additionally, the project includes a feature to decrypt MD5 hashes using the generated rainbow table.

## Prerequisites

- Python 3.x
- Required libraries (hashlib, itertools)

## How to Use

1. Run the `Generate_MD5_Rainbow_Table.py` script.
2. Follow the prompts to input the character set and the length of the passphrase.
3. The rainbow table will be generated and stored in the specified directory.

## Files

- `Generate_MD5_Rainbow_Table.py`: Contains the Python script for generating rainbow tables.
- `hashes.txt`: Database file containing the generated rainbow table.
- `Decrypt_MD5_Hash_Using_Rainbow_Table.py`: Script for decrypting MD5 hashes using the rainbow table.

## Usage

### Rainbow Table Generation:

```bash
python Generate_MD5_Rainbow_Table.py
```

Follow the prompts to provide the character set and the desired length of the passphrase.

### MD5 Hash Decryption:

```bash
python Decrypt_MD5_Hash_Using_Rainbow_Table.py
```

Input the MD5 hash you wish to decrypt, and the program will attempt to find a match in the rainbow table.

## Note

- Ensure that you have the necessary permissions to write to the specified directory for rainbow table generation.
- The larger the character set and the longer the passphrase, the larger the generated rainbow table will be.

## Disclaimer

This project is for educational purposes only. It is essential to respect privacy and legality when using these tools. The developers are not responsible for any misuse or illegal activities performed with this software.

