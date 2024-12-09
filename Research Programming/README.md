These are scripts made by David.

## p_generator.py

### Usage
When run, generates and prints a list of all p values between 1 and 10,000.

### findPValues(upper, lower=1)
Returns a list of p values between `lower` and `upper`. If generating very large values of p, I recommend using a very small range so it doesn't take forever.

### is2PrimitiveRootOfP(p)
Returns whether p is a prime number and 2 is a primitive root of p.
If 2 is a primitive root, then, for k = 1...p-1, the first time 2^k % p = 1 is when k = p-1.

## param_generator.py

### Usage
Generates sets of valid parameters and saves them to a csv. If a count is specified, parameters lists are removed randomly to the count before being saved.

#### Parameters
| Name      | Usage                     | Default       |
| --------- | ------------------------- | ------------- |
| -ppmin    | Min p value               | 1000          |
| -pmax     | Max p value               | 2000          |
| -dvmin    | Min dv value              | 11            |
| -dvmax    | Max dv value              | 15            |
| -mmin     | Min m value               | 11            |
| -mmax     | Max m value               | 17            |
| -n0       | # of m values generated   | 2             |
| -count    | # of parameters to return | -1 (no limit) |
| -fileName | File name of output       | params.csv    |


### generateParams(pmin, pmax, dvmin, dvmax, mmin, mmax, n0)
Returns an array of lists of parameters, each in the form \[p, dv, m1, ...mn, n0\], with the number of m values being equal to n0.

p loops through every odd value between pmin and pmax (inclusive). 

If 2 is a primitive root of p, then dv loops through every odd value between dvmin and dvmax (also inclusive).

For each pair of p and dv, two sets of m values are generated. Each is generated randomly between mmin and mmax (inclusive). According to the specification, the square sum of the set of m's must be an odd number. To meet this, if the square sum is an even number, the first m value is incremented by one (and subtracted by two if above mmax). Theoretically, the evenness of the square sum of a set is determined only by the number of odd numbers in the set, which is why changing the evenness of one value fixes it.

