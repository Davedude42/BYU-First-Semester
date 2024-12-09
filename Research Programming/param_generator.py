from p_generator import is2PrimitiveRootOfP
import random
import sys
import functools

def paramsToCSV(params, fileName):
    with open(fileName, 'w') as file:
        header = 'p,dv,' + (','.join(['m' + str(n) for n in range(len(params[0])-3)])) + ',n0\n'
        file.write(header)
        for lst in params:
            file.write(','.join([str(n) for n in lst]) + '\n')

def generateParams(pmin, pmax, dvmin, dvmax, mmin, mmax, n0):
    """
    Returns matrix of valid p, dv, m1, ...mn, n0 values
    """
    ret = []

    if pmin % 2 == 0:
        pmin = pmin+1
    if dvmin % 2 == 0:
        dvmin = dvmin+1

    for p in range(pmin, pmax+1, 2):
        if is2PrimitiveRootOfP(p):
            for dv in range(dvmin, dvmax+1, 2):

                # Arbitrary number of m_values to generate for each p and dv
                for i in range(2):
                    m_values = []
                    # Theoretically, an even number squared plus an odd number squared is always odd
                    for n in range(n0):
                        m_values.append(random.randint(mmin, mmax))

                    sqr_sum = functools.reduce(lambda a, b: a + b**2, m_values)

                    if sqr_sum % 2 == 0:
                        m_values[0] += 1
                        if m_values[0] > mmax:
                            m_values[0] -= 2
                        
                    ret.append([p, dv] + m_values + [n0])
    
    return ret
                



if __name__ == '__main__':
    pmin = 1000
    pmax = 2000
    dvmin = 11
    dvmax = 15
    mmin = 11
    mmax = 17
    n0 = 2
    count = -1
    fileName = 'params.csv'
    for i in range(len(sys.argv)):
        if sys.argv[i] == '-pmin':
            pmin = int(sys.argv[i+1])
            i += 1
        if sys.argv[i] == '-pmax':
            pmax = int(sys.argv[i+1])
            i += 1
        if sys.argv[i] == '-dvmin':
            dvmin = int(sys.argv[i+1])
            i += 1
        if sys.argv[i] == '-dvmax':
            dvmax = int(sys.argv[i+1])
            i += 1
        if sys.argv[i] == '-mmin':
            mmin = int(sys.argv[i+1])
            i += 1
        if sys.argv[i] == '-mmax':
            mmax = int(sys.argv[i+1])
            i += 1
        if sys.argv[i] == '-n0':
            n0 = int(sys.argv[i+1])
            i += 1
        if sys.argv[i] == '-count':
            count = int(sys.argv[i+1])
            i += 1
        if sys.argv[i] == '-fileName':
            fileName = sys.argv[i+1]
            i += 1

    print(f'Generating with ranges:\npmin = {pmin}, pmax = {pmax}, dvmin = {dvmin}, dvmax = {dvmax}, mmin = {mmin}, mmax = {mmax}, n0 = {n0}')

    params = generateParams(pmin, pmax, dvmin, dvmax, mmin, mmax, n0)

    print(f'Generated {len(params)} parameter sets')

    # Removes random paramter sets until count specified
    if count != -1 and count > 0:
        while len(params) > count:
            params.pop(random.randint(0, len(params)-1))
        print(f'Trimmed to {len(params)} parameter sets')

    paramsToCSV(params, fileName)

    print(f'Saved to {fileName}')