<div align="center">
<h1>🇧🇷 Brazilian Utils</h1>

<p>Utils library for Brazilian-specific businesses.</p>

[![codecov](https://codecov.io/gh/brazilian-utils/brutils-python/branch/main/graph/badge.svg?token=5KNECS8JYF)](https://codecov.io/gh/brazilian-utils/brutils-python)
[![Downloads per Month](https://shields.io/pypi/dm/brutils)](https://pypistats.org/packages/brutils)
[![Package version](https://shields.io/pypi/v/brutils)](https://pypi.org/project/brutils/)
### [Procurando pela versão em português?](README.md)

</div>

# Getting Started

Brazilian Utils is a library focused on solving problems that we face daily in
the development of applications for the Brazilian business.

- [Installation](#installation)
- [Usage](#usage)
- [Utilities](#utilities)
- [Contributing with Source Code](#contributing-with-source-code)
- [Feature Request and Bug Report](#feature-request-and-bug-report)
- [Questions? Ideas?](#questions-ideas)
- [Code Contribution](#code-contribution)


# Installation

```
pip install brutils
```

# Usage

To use one of our utilities you just need to import the required function as in the example below:

```python
>>> from brutils import is_valid_cpf
>>> is_valid_cpf('00011122233')
False
```

# Utilities

- [CPF](#cpf)
  - [is_valid_cpf](#is_valid_cpf)
  - [format_cpf](#format_cpf)
  - [remove_symbols_cpf](#remove_symbols_cpf)
  - [generate_cpf](#generate_cpf)
- [CNPJ](#cnpj)
  - [is_valid_cnpj](#is_valid_cnpj)
  - [format_cnpj](#format_cnpj)
  - [remove_symbols_cnpj](#remove_symbols_cnpj)
  - [generate_cnpj](#generate_cnpj)
- [CEP](#cep)
  - [is_valid_cep](#is_valid_cep)
  - [format_cep](#format_cep)
  - [remove_symbols_cep](#remove_symbols_cep)
  - [generate_cep](#generate_cep)
- [Phone](#phone)
  - [is_valid_phone](#is_valid_phone)
  - [is_valid_mobile_phone](#is_valid_mobile_phone)
  - [is_valid_landline_phone](#is_valid_landline_phone)
  - [remove_symbols_phone](#remove_symbols_phone)
- [Email](#email)
  - [is_valid_email](#is_valid_email)
- [License Plate](#license_plate)
  - [is_valid_license_plate_old_format](#is_valid_license_plate_old_format)
  - [is_valid_license_plate_mercosul](#is_valid_license_plate_mercosul)
  - [convert_license_plate_to_mercosul](#convert_license_plate_to_mercosul)
- [PIS](#pis)
  - [is_valid_pis](#is_valid_pis)
  - [generate_pis](#generate_pis)
- [Legal Process](#legal-process)
  - [remove\_symbols\_processo\_juridico](#remove_symbols_processo_juridico)

## CPF

### is_valid_cpf

Check if CPF is valid. Numbers only, formatted as strings. Does not check if CPF exists.

```python
>>> from brutils import is_valid_cpf
>>> is_valid_cpf('00011122233')
False
```

### format_cpf

Format CPF. Returns None if CPF is invalid.

```python
>>> from brutils import format_cpf
>>> format_cpf('11144477735')
'111.444.777-35'
```

### remove_symbols_cpf

Remove formatting symbols from CPF and return only digits.
It only filters out the symbols used for CPF validation.
It purposefully doesn't remove other symbols.

```python
>>> from brutils import remove_symbols_cpf
>>> remove_symbols_cpf('000.111.222-33')
'00011122233'
```

### generate_cpf

Generate a valid random CPF.

```python
>>> from brutils import generate_cpf
>>> generate_cpf()
'17433964657'
```

## CNPJ

### is_valid_cnpj

Check if CNPJ is valid. Numbers only, formatted as strings. Does not check if CNPJ exists.

```python
>>> from brutils import is_valid_cnpj
>>> is_valid_cnpj('00111222000133')
False
```

### format_cnpj

Format CNPJ.

```python
>>> from brutils import format_cnpj
>>> format_cnpj('00111222000100')
'00.111.222/0001-00'
```

### remove_symbols_cnpj

Remove formatting symbols from CNPJ and return only digits.
It only filters out the symbols used for CNPJ validation.
It purposefully doesn't remove other symbols.

```python
>>> from brutils import remove_symbols_cnpj
>>> remove_symbols_cnpj('00.111.222/0001-00')
'00111222000100'
```

### generate_cnpj

Generate a valid random CNPJ.

```python
>>> from brutils import generate_cnpj
>>> generate_cnpj()
'34665388000161'
```

## CEP

### is_valid_cep

Check if CEP is valid. Numbers only, formatted as strings. Does not check if CEP exists.

```python
>>> from brutils import is_valid_cep
>>> is_valid_cep('01310200')
True
```

### format_cep

Format CEP. Returns None if CEP is invalid.

```python
>>> from brutils import format_cep
>>> format_cpf('01310200')
'01310-200'
```

### remove_symbols_cep

Remove formatting symbols from CEP and return only digits.
It only filters out the symbols used for CEP validation.
It purposefully doesn't remove other symbols.

```python
>>> from brutils import remove_symbols_cep
>>> remove_symbols_cep('01310-200')
'01310200'
```

### generate_cep

Generate a valid random CEP.

```python
>>> from brutils import generate_cep
>>> generate_cep()
'77520503'
```

## Phone

### is_valid_phone

Check if phone number is valid, can be landline or mobile phone. Numbers only, with area code (DDD) and without the international prefix, formatted as a string. ***For example: +55 48 9999 9999 would become '4899999999'*** This function validates only Brazilian phone numbers and does not verify if the number actually exists.

```python
>>> from brutils import is_valid_phone
>>> is_valid_phone('11994029275')
True
```

### is_valid_mobile_phone

Check if mobile phone number is valid. Numbers only, with area code (DDD) and without the international prefix, formatted as a string. ***For example: +55 48 9999 9999 would become '4899999999'*** This function validates only Brazilian phone numbers and does not verify if the number actually exists.

```python
>>> from brutils import is_valid_mobile_phone
>>> is_valid_mobile_phone('11994029275')
True
```

### is_valid_landline_phone

Check if landline phone number is valid. Numbers only, with area code (DDD) and without the international prefix, formatted as a string. ***For example: +55 48 3333 3333 would become '4833333333'.*** This function validates only Brazilian phone numbers and does not verify if the number actually exists.

```python
>>> from brutils import is_valid_landline_phone
>>> is_valid_landline_phone('1938814933')
True
```

### remove_symbols_phone

Remove symbols from phone number. ***Example: +55 (21) 2569-6969 will return '552125696969'.***

```python
>>> from brutils import remove_symbols_phone
>>> remove_symbols_phone('+55 (21) 2569-6969')
'552125696969'
```
## Email

### is_valid_email

Check if a string corresponds to a valid email. The rules for validating an email address generally follow the specifications defined by RFC 5322 (updated by RFC 5322bis), which is the widely accepted standard for email address formats.

```python
from brutils import is_valid_email

>>> is_valid_email("joao.ninguem@gmail.com")
True
>>> is_valid_email(".joao.ninguem@gmail.com")
False
>>> is_valid_email("joao.ninguem@gmail.")
False
>>> is_valid_email("joao ninguem@gmail.com")
False
```

## License_Plate

### is_valid_license_plate_old_format

Checks if it is a License Plate in the old format used in Brazil. Receives as a parameter a string that should contain only alphanumeric characters (letters and numbers) and returns a boolean value. ***Example: 'abc1234' results in True.***
This function only validates plates in the old format and does not verify if it actually exists.

```python
>>> from brutils import is_valid_license_plate_old_format
>>> is_valid_license_plate_old_format('ABC1234')
True
>>> is_valid_license_plate_old_format('def5678')
True
>>> is_valid_license_plate_old_format('GHI-4567')
False
```

### is_valid_license_plate_mercosul

Checks if the provided string representing a license place is valid, according to the new
Mercosul standards, in other words, if it follows the pattern LLLNLNN.
***Example: ABC4E67.***

```python
>>> from brutils import is_valid_license_plate_mercosul
>>> is_valid_license_plate_mercosul('ABC4E67')
True
```

### convert_license_plate_to_mercosul

Converts the provided string representing a license plate in the old format to the new
format, according to the new Mercosul standards (following the pattern LLLNLNN). In case
the provided license plate is invalid it will return the value `None`.
***Example: ABC4567 -> ABC4F67.***

```python
>>> from brutils import convert_license_plate_to_mercosul
>>> convert_license_plate_to_mercosul("ABC123")
"ABC1C34"
>>> convert_license_plate_to_mercosul("abc123")
"ABC1C34"
>>> convert_license_plate_to_mercosul("ABC1D23")
None
```

## PIS

### is_valid_pis

Check if PIS/PASEP number is valid. Numbers only, formatted as strings. Does not check if PIS/PASEP exists.
More details about the validation can be found here: https://www.macoratti.net/alg_pis.htm.

```python
from brutils import is_valid_pis

>>> is_valid_pis("12038619494")
True
>>> is_valid_pis("11111111111")
False
>>> is_valid_pis("123456")
False
```

### generate_pis

Generates a valid random PIS/PASEP number.

```python
from brutils import generate_pis

>>> generate_pis()
'12038619494'
>>> generate_pis()
'57817700092'
>>> generate_pis()
'49850211630'
```

## Legal Process

### remove_symbols_processo_juridico

Removes common symbols from a legal process number string.
The standard symbols removed are "." and "-". It purposefully doesn't remove other symbols.

```python
from brutils import remove_symbols_processo_juridico

>>> remove_symbols_processo_juridico("6439067-89.2023.4.04.5902")
"64390678920234045902"
>>> remove_symbols_processo_juridico("4976023-82.2012.7.00.2263")
"49760238220127002263"
>>> remove_symbols_processo_juridico("4976023-82.2012.7.00.2263*!*&#")
"49760238220127002263*!*&#"
```

# Feature Request and Bug Report

If you want to suggest new features or report bugs, simply create
a new [issue][github-issues], and we will respond to you there!

(To learn more about GitHub issues, check out the [official GitHub documentation][github-issues-doc]).

# Questions? Ideas?

Questions on how to use the library? New ideas for the project?
Want to share something with us? Feel free to start a thread in our
[Discussions][github-discussions], and we'll interact with you there!

(To learn more about GitHub discussions, refer to the
[official GitHub documentation][github-discussions-doc]).

# Code Contribution

Your collaboration is always very welcome! We've prepared the [CONTRIBUTING.md][contributing] file
to assist you in getting started. There, you'll find all the information you need to contribute to
the project. Please, don't hesitate to ask us using [GitHub Discussions][github-discussions] if
you encounter any difficulties or have any questions. Every bit of help counts!

Let's build it together 🚀🚀

[contributing]: CONTRIBUTING_EN.md
[github-discussions-doc]: https://docs.github.com/en/discussions
[github-discussions]: https://github.com/brazilian-utils/brutils-python/discussions
[github-issues-doc]: https://docs.github.com/en/issues/tracking-your-work-with-issues/creating-an-issue
[github-issues]: https://github.com/brazilian-utils/brutils-python/issues
