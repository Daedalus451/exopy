# exopy #

[![Language](https://img.shields.io/badge/C%2B%2B-17-blue.svg)](https://en.wikipedia.org/wiki/C%2B%2B#Standardization)
[![License](https://img.shields.io/github/license/Daedalus451/exopy)](https://www.mozilla.org/en-US/MPL/2.0/)

**exopy** is a Python module for modeling the growth of planetesimals in a disk over time. It is built as a .pyd from a C++ project using pybind11.

The [Smoluchowski coagulation equation](https://en.wikipedia.org/wiki/Smoluchowski_coagulation_equation), as shown below, is used to compute the number of planetesimals.

![coagulation_equation.svg](/assets/coagulation_equation.svg "Coagulation Equation")

## Requirements ##

+ C++ 17 compiler
  + tested on:
    + msvc 1924 (Windows 10 1909)
    + gcc 8.3.0 (Ubuntu 18.04.4)
    + clang 9.0.0 (Ubuntu 18.04.4)
+ [CMake 3.14](https://cmake.org/) or newer
+ [pybind11](https://github.com/pybind/pybind11)
+ [span-lite](https://github.com/martinmoene/span-lite)
+ [Python 3](https://www.python.org/)
+ [numpy](https://numpy.org/)

## Example ##

### Input ###

```
import exopy
import numpy as np

t = np.linspace(start=0.0, stop=3.0, num=4)
nk = exopy.compute_nk_approx(steps=t, k_max=8, initial=200.0, A=0.001)
with np.printoptions(precision=5, suppress=True, linewidth=100):
  print(nk)
```

### Output ###

```
[[200.        0.        0.        0.        0.        0.        0.        0.     ]
 [160.       20.        0.        0.        0.        0.        0.        0.     ]
 [131.2      29.2       3.2       0.2       0.        0.        0.        0.     ]
 [109.70944  33.02376   6.50688   1.0134    0.11968   0.01096   0.00064   0.00002]]
```

## License ##

Copyright &copy; 2020 Jared Duffey - All Rights Reserved

*exopy* is distributed under the [Mozilla Public License, v. 2.0](https://www.mozilla.org/en-US/MPL/2.0/). A copy of this license is included in LICENSE.txt.
