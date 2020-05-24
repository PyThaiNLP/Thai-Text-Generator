# TTG : Thai Text Generator
Thai Text Generator

## Install

```sh
pip install -e .
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