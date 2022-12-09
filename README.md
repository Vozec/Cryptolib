<p align="center">
  <img alt="GitHub release (latest by date)" src="https://img.shields.io/badge/Version-1.0-blue.svg">
</p>

#  Cryptolib

## Description:

This python library gathers all the cryptographic attacks that I present on my website [vozec.fr](https://vozec.fr/crypto-rsa/)
Most of the scripts are taken from my articles, so it is advisable to read them to better understand how they work!

## Installation:

```bash
git clone https://github.com/Vozec/Cryptolib.git
cd Cryptolib
nano first_test.py
... enjoy !
```

## Examples / test
You can retrieve test for all attacks in the **examples** folder.  
The file ``test.py`` runs all tests in this folder.


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

- Show info on known variables
  ```python
  sys.info()
  ```

  *output*:
  ```bash
  --- Status ---
    E: known
    P: unknown
    Q: unknown
    N: known
    D: unknown
  PHI: unknown
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

- Add a value:
  ```python
  sys.add('n',7617...7187)
  ```

- Get Public Key (.pub)
  ```python
  sys.public_key()
  ```

- Get Private Key (.pem)
  ```python
  sys.private_key()
  ```

## Attacks
- `FactorDb Factorization`
  ```python
  sys.factordb()
  m = sys.decrypt(c)
  ```

- `Fermat Factorization`
  ```python
  sys.fermat()
  m = sys.decrypt(c)
  ```

- `Wiener Factorization`
  ```python
  sys.wiener()
  m = sys.decrypt(c)
  ```

- `Common Prime Factorization`
  ```python
  sys.common_prime()
  m = sys.decrypt(c)
  ```

- `Small m decoder`
  ```python
  m = sys.small_m()
  ```

- `Common Modulus decoder`
  ```python
  m = sys.common_modulus()
  ```

- `Hastad Broadcast attack`
  ```python
  m = sys.hastad()
  ```

- `MultiPrimes decoder`
  ```python
  primes = [..,..,..]
  sys.multi_primes()
  m = sys.decrypt(c)
  ```

- `Franklin Reiter attack`
  ```python
  sys.add('c',c1)
	sys.add('c',c2)
	m2 = sys.franklin_reiter(a=a,b=b)
  #m2 = a*m1+b
  ```
