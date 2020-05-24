# TTG : Thai Text Generator
Thai Text Generator

## Install

```sh
pip install ttg
```

if you want used thai2fit, you can install :
```sh
pip install ttg[thai2fit]
```

## Example

```python
from thaitextgenerator import *
a=Unigram()
print(a.gen_sentence(N=10))
b=Bigram()
print(b.gen_sentence(start_seq="คน", N=10))
c=Tigram()
c.gen_sentence(N=10, start_seq=("คน","ดี"))
# Thai2Fit
from thaitextgenerator.thai2fit import gen_sentence
gen_sentence()
```

## Docs

### N-Gram
**import**
```python
from thaitextgenerator import *
```
#### Unigram

we support corpus

- TNC : Thai National Corpus (Default)
- TCC : Thai Textbook Corpus
- oscar : Open Super-large Crawled ALMAnaCH coRpus

```python
Unigram(name = "tnc or tcc or oscar")

Unigram().gen_sentence(N:int=3,prob:float=0.001, start_seq:str=None ,output_str:bool = True, duplicate:bool=False)
```

#### Bigram

we support corpus

- TNC : Thai National Corpus (Default)

```python
Bigram(name = "tnc")

Bigram().gen_sentence(N:int=4,prob:float=0.001, start_seq:str=None, output_str:bool = True, duplicate:bool=False)
```

#### Tigram

we support corpus

- TNC : Thai National Corpus (Default)

```python
Tigram(name = "tnc")

Bigram().gen_sentence(N:int=4,prob:float=0.001, start_seq:tuple=None, output_str:bool = True, duplicate:bool=False)
```

### Thai2Fit
```python
# Thai2Fit
from thaitextgenerator.thai2fit import gen_sentence
en_sentence(N:int=4,prob:float=0.001, start_seq:str=None, output_str:bool = True)
```

## License
```
   Copyright 2020 Wannaphong Phatthiyaphaibun

   Licensed under the Apache License, Version 2.0 (the "License");
   you may not use this file except in compliance with the License.
   You may obtain a copy of the License at

       http://www.apache.org/licenses/LICENSE-2.0

   Unless required by applicable law or agreed to in writing, software
   distributed under the License is distributed on an "AS IS" BASIS,
   WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
   See the License for the specific language governing permissions and
   limitations under the License.
```