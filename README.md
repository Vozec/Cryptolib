<p align="center">
  <img alt="GitHub release (latest by date)" src="https://img.shields.io/badge/Version-1.0-blue.svg">
</p>

#  Cryptolib

## Description:
This python library gathers all the cryptographic attacks that I present on my website [vozec.fr](https://vozec.fr/crypto-rsa/)
Most of the scripts are taken from my articles , so it is advisable to read them to better understand how they work

## Installation:
git clone https://github.com/Vozec/Cryptolib.git
cd Cryptolib
nano first_test.py
... enjoy !

## Documentation:

- Create a RSA-Object with secure parameters
  ```python
  sys = rsa_init()
  ```
- Create a RSA-Object with custom parameters
  ```python
  sys = rsa_init(
    e=65537,
    n=...
  )
  ```
- Show info on know variables 
  ```python
  sys.info()
  ```
  *output*:
  ```bash
  --- Status ---
    E: know
    P: unknow
    Q: unknow
    N: know
    D: unknow
  PHI: unknow
  --------------
  ```

- Encrypt Message:  
  *(e,n) have to be set*
  ```python
  c = sys.encrypt(b'Hello Vozec')
  ```

- Decrypt Message:  
  *(e,n,d) have to be set*
  ```python
  m = sys.decrypt(c)
  ```

- Remove a value:
  ```python
  sys.pop('p')
  ```

- Get Publique Key (.pub)
  ```python
  sys.public_key()
  ```

- Get Private Key (.pem)
  ```python
  sys.private_key()
  ```

## Attacks


- ``FactorDb Factorization``
  ```python
  sys.factordb()
  ```

- ``Fermat Factorization``
  ```python
  sys.fermat()
  ```

- ``Wiener Factorization``
  ```python
  sys.wiener()
  ```

- ``Common Prime Factorization``
  ```python
  sys.wiener(n_2)
  ```

- ``Small m``
  ```python
  m = sys.small_m(c)
  ```
