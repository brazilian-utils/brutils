<div align="center">
<h1>🇧🇷 Brazilian Utils</h1>

<p>Utils library for Brazilian-specific businesses.</p>
</div>

[![codecov](https://codecov.io/gh/brazilian-utils/brutils-python/branch/main/graph/badge.svg?token=5KNECS8JYF)](https://codecov.io/gh/brazilian-utils/brutils-python)
[![Downloads per Month](https://shields.io/pypi/dm/brutils)](https://pypi.org/project/brutils/)
[![Package version](https://shields.io/pypi/v/brutils)](https://pypi.org/project/brutils/)

### [Procurando pela versão em português?](README_PT_BR.md)

`brutils` is a library for validating brazilian document numbers, and might
eventually evolve to deal with other validations related to brazilian bureaucracy.

It's main functionality is the validation of CPF and CNPJ numbers, but suggestions
for other (preferably deterministic) things to validate are welcome.


## Installation

```
pip install brutils
```


## Usage

### How do I validate a CPF or CNPJ?
```
# numbers only, formatted as strings

>>> from brutils.cnpj import is_valid_cnpj
>>> from brutils.cpf import is_valid_cpf
>>> is_valid_cpf('00011122233')
False
>>> is_valid_cnpj('00111222000133')
False
```

### What if my string has formatting symbols in it?
```
>>> cpf.sieve('000.111.222-33')
'00011122233'
>>> cnpj.sieve('00.111.222/0001-00')
'00111222000100'

# The `sieve` function only filters out the symbols used for CPF or CNPJ validation.
# It purposefully doesn't remove other symbols, as those may be indicators of data
# corruption, or a possible lack of input filters.
```

### What if I want to format a numbers only string?
```
>>> cpf.display('00011122233')
'000.111.222-33'
>>> cnpj.display('00111222000100')
'00.111.222/0001-00'
```

### What if I want to generate random, but numerically valid CPF or CNPJ numbers?
```
>>> cpf.generate()
'17433964657'
>>> cnpj.generate()
'34665388000161'
```


## Testing

```
python3 -m unittest discover tests/
```
