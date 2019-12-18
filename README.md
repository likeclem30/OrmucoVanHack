#### Ormuco and VanHack Code Challenge

- Question A

  Your goal for this question is to write a program that accepts two lines (x1,x2) and (x3,x4) on the
  x-axis and returns whether they overlap. As an example, (1,5) and (2,6) overlaps but not (1,5)
  and (6,8).

#### My Solution Question A---See Directory

> The Question B
> The goal of this question is to write a software library that accepts 2 version string as input and returns whether one is greater than, equal, or less than the other. As an example: “1.2” is greater than “1.1”. Please provide all test cases you could think of.

#### My Solution Question B

Get Started:

- Clone this repository:
```sh
$ git@github.com:likeclem30/CompareVersionString.git
```
- Change into the `CompareVersionString` directory:
```sh
$ cd likeclem30/CompareVersionString
```
- Install all dependencies:
```sh
$ pip install -r requirements.txt
```
Run Test:
```sh
$ python3 -m unittest -v test.test_compareversion
```

Run as Packaged Library:
- Install:
```sh
$ pip install CompareVersionString
```

- Usage:

````
from CompareVersionString.comparevs import padStringZero,compareVersion,compareVersionDriver



version1 = '2.1.1' = version1.split('.')

padded_result = padStringZero(('2.1.1', 6, '0')
""" version1 is 2.1.1 and version2 is 2.1.1.1.0.1 it makes the length of both version same by padding it with '0' """

# It will return:
#     ['2', '1', '1', '0', '0', '0']  


comparison_result = compareVersion('2.1.1', '2.0.1')

# It will return:
#     A positive number: If the first version is greater than the second  
#     A negative number: If the first version is smaller than the second
#     Zero: If the versions are equals

outcome = compareVersionDriver('1.0.1', '1.0.3')

# It will return:

#     '{version1}' is smaller than '{version2}': If the comparison returns -1
#     '{version2}' is smaller than '{version2}': If the comparison returns 1
#     '{version1}' is same version as '{version2}': If the comparison returns 0
````


#### Author(s)
>- [William Aaron](https://github.com/likeclem30)
