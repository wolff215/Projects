#!/usr/bin/env python2.7
from datetime import date
from itertools import permutations
import argparse
import math

def problem1():
    """Sum of all natural numbers that are multiples of 3 or 5 and less than 1000"""
    print sum([i for i in range(1000) if 0 in (i % 3, i % 5)])

def problem2():
    """Sum of even Fibonacci numbers less than 4 million"""
    def fib_gen():
        a, b = 0, 1
        while 1:
            yield b
            a, b = b, a+b

    fib_set = fib_gen()
    fib = next(fib_set)
    fib_list = [fib]

    while fib < 4000000:
        fib_list.append(fib)
        fib = next(fib_set)

    print sum([fib for fib in fib_list if not fib & 1])

def problem6():
    """Difference between sum of squares and square of sums for natural numbers less then 100"""
    sums = sum([num**2 for num in range(101)])
    square = sum([num for num in range(101)])**2
    print square - sums

def problem5():
    """Least common multiple of natrual numbers up to 20"""
    def gcd(num_f, num_s):
        if num_s == 0:
            return num_f
        else:
            return gcd(num_s, num_f % num_s)

    def lcm(a, b):
        return (a / gcd(a, b)) * b

    def lcm_list(num):
        if num ==  1:
            return 1
        else:
            return lcm(num, lcm_list(num - 1))

    print lcm_list(20)

def problem3():
    """Largest prime factor of a number"""
    number  = 600851475143
    currentNumber = 2
    number_temp = number
    primes = []
    while currentNumber <= number**.5:
        if number_temp % currentNumber == 0:
            number_temp = number_temp / currentNumber
            primes.append(currentNumber)
        currentNumber = currentNumber + 1

    print primes

def problem4():
    """Largest palindrome made from product of two 3-digit numbers"""
    print max([x*y for x in range(100,1000) for y in range(100,1000) if str(x*y)==str(x*y)[::-1]])

def problem7():
    "Find the 1001st prime number"""
    find = 1001
    found = 1
    num = 3
    primes = [2]

    while found < find:
        for divisor in range(2, find):
            if num % divisor == 0:
                num = num + 2
                break

            if divisor**2 > num:
                primes.append(num)
                num = num + 2
                found = found + 1
                break

    print primes[find - 1]

def problem8():
    """Largest product of 5 consecutive numbers in 1000 digit number"""
    big_ass_number = '7316717653133062491922511967442657474235534919493496983520312774506326239578318016984801869478851843858615607891129494954595017379583319528532088055111254069874715852386305071569329096329522744304355766896648950445244523161731856403098711121722383113622298934233803081353362766142828064444866452387493035890729629049156044077239071381051585930796086670172427121883998797908792274921901699720888093776657273330010533678812202354218097512545405947522435258490771167055601360483958644670632441572215539753697817977846174064955149290862569321978468622482839722413756570560574902614079729686524145351004748216637048440319989000889524345065854122758866688116427171479924442928230863465674813919123162824586178664583591245665294765456828489128831426076900422421902267105562632111110937054421750694165896040807198403850962455444362981230987879927244284909188845801561660979191338754992005240636899125607176060588611646710940507754100225698315520005593572972571636269561882670428252483600823257530420752963450'
    number = list(big_ass_number)
    start = 0
    end = 5
    largest = 0
    temp = 1
    for part in number:
        for mult in range(start, end):
            if end < 1000:
                temp = temp * int(number[mult])
        start += 1
        end +=1
        if temp > largest:
            largest = temp
        temp = 1
    print largest

def problem10():
    """Find the sum of all primes below 2000000"""
    max_num = 2000000
    primes = []
    candidates = range(max_num + 1)
    final = int(max_num**0.5)
    for i in xrange(2, final + 1):
        if not candidates[i]:
            continue

        candidates[2*i::i] = [None] * (max_num//i - 1)

    primes = [item for item in candidates[2:] if item]
    print sum([total for total in primes])

def problem13():
    """Find first 10 digits of sum of 100 50-digit numbers"""
    numbers = [37107287533902102798797998220837590246510135740250,
            46376937677490009712648124896970078050417018260538,
            74324986199524741059474233309513058123726617309629,
            91942213363574161572522430563301811072406154908250,
            23067588207539346171171980310421047513778063246676,
            89261670696623633820136378418383684178734361726757,
            28112879812849979408065481931592621691275889832738,
            44274228917432520321923589422876796487670272189318,
            47451445736001306439091167216856844588711603153276,
            70386486105843025439939619828917593665686757934951,
            62176457141856560629502157223196586755079324193331,
            64906352462741904929101432445813822663347944758178,
            92575867718337217661963751590579239728245598838407,
            58203565325359399008402633568948830189458628227828,
            80181199384826282014278194139940567587151170094390,
            35398664372827112653829987240784473053190104293586,
            86515506006295864861532075273371959191420517255829,
            71693888707715466499115593487603532921714970056938,
            54370070576826684624621495650076471787294438377604,
            53282654108756828443191190634694037855217779295145,
            36123272525000296071075082563815656710885258350721,
            45876576172410976447339110607218265236877223636045,
            17423706905851860660448207621209813287860733969412,
            81142660418086830619328460811191061556940512689692,
            51934325451728388641918047049293215058642563049483,
            62467221648435076201727918039944693004732956340691,
            15732444386908125794514089057706229429197107928209,
            55037687525678773091862540744969844508330393682126,
            18336384825330154686196124348767681297534375946515,
            80386287592878490201521685554828717201219257766954,
            78182833757993103614740356856449095527097864797581,
            16726320100436897842553539920931837441497806860984,
            48403098129077791799088218795327364475675590848030,
            87086987551392711854517078544161852424320693150332,
            59959406895756536782107074926966537676326235447210,
            69793950679652694742597709739166693763042633987085,
            41052684708299085211399427365734116182760315001271,
            65378607361501080857009149939512557028198746004375,
            35829035317434717326932123578154982629742552737307,
            94953759765105305946966067683156574377167401875275,
            88902802571733229619176668713819931811048770190271,
            25267680276078003013678680992525463401061632866526,
            36270218540497705585629946580636237993140746255962,
            24074486908231174977792365466257246923322810917141,
            91430288197103288597806669760892938638285025333403,
            34413065578016127815921815005561868836468420090470,
            23053081172816430487623791969842487255036638784583,
            11487696932154902810424020138335124462181441773470,
            63783299490636259666498587618221225225512486764533,
            67720186971698544312419572409913959008952310058822,
            95548255300263520781532296796249481641953868218774,
            76085327132285723110424803456124867697064507995236,
            37774242535411291684276865538926205024910326572967,
            23701913275725675285653248258265463092207058596522,
            29798860272258331913126375147341994889534765745501,
            18495701454879288984856827726077713721403798879715,
            38298203783031473527721580348144513491373226651381,
            34829543829199918180278916522431027392251122869539,
            40957953066405232632538044100059654939159879593635,
            29746152185502371307642255121183693803580388584903,
            41698116222072977186158236678424689157993532961922,
            62467957194401269043877107275048102390895523597457,
            23189706772547915061505504953922979530901129967519,
            86188088225875314529584099251203829009407770775672,
            11306739708304724483816533873502340845647058077308,
            82959174767140363198008187129011875491310547126581,
            97623331044818386269515456334926366572897563400500,
            42846280183517070527831839425882145521227251250327,
            55121603546981200581762165212827652751691296897789,
            32238195734329339946437501907836945765883352399886,
            75506164965184775180738168837861091527357929701337,
            62177842752192623401942399639168044983993173312731,
            32924185707147349566916674687634660915035914677504,
            99518671430235219628894890102423325116913619626622,
            73267460800591547471830798392868535206946944540724,
            76841822524674417161514036427982273348055556214818,
            97142617910342598647204516893989422179826088076852,
            87783646182799346313767754307809363333018982642090,
            10848802521674670883215120185883543223812876952786,
            71329612474782464538636993009049310363619763878039,
            62184073572399794223406235393808339651327408011116,
            66627891981488087797941876876144230030984490851411,
            60661826293682836764744779239180335110989069790714,
            85786944089552990653640447425576083659976645795096,
            66024396409905389607120198219976047599490197230297,
            64913982680032973156037120041377903785566085089252,
            16730939319872750275468906903707539413042652315011,
            94809377245048795150954100921645863754710598436791,
            78639167021187492431995700641917969777599028300699,
            15368713711936614952811305876380278410754449733078,
            40789923115535562561142322423255033685442488917353,
            44889911501440648020369068063960672322193204149535,
            41503128880339536053299340368006977710650566631954,
            81234880673210146739058568557934581403627822703280,
            82616570773948327592232845941706525094512325230608,
            22918802058777319719839450180888072429661980811197,
            77158542502016545090413245809786882778948721859617,
            72107838435069186155435662884062257473692284509516,
            20849603980134001723930671666823555245252804609722,
            53503534226472524250874054075591789781264330331690]

    print sum(numbers)

def problem14():
    """Starting number under 1000000 that produces longest chain"""
    max = 0
    for num in range(1, 1000001):
        chain = 1
        cnt = long(num)
        while cnt > 1:
            if cnt % 2 == 0:
                cnt /= 2
            else:
                cnt = (3 * cnt) + 1
            chain += 1
        if chain > max:
            max = chain
            start_num = num
    print start_num

def problem20():
    """Sum of the digits of 100!"""
    fact = str(math.factorial(100))
    list_fact = list(fact)
    print sum([int(i) for i in list_fact])

def problem48():
    """Last ten digits of the series 1^1 + 2^2 + 3^3 + ... + 1000^1000"""
    answer = 0
    for num in range(1, 1001):
        answer += num ** num
    print str(answer)[-10:]

def problem16():
    """What is sum of the digits in 2^1000"""
    print sum([int(i) for i in list(str(2**1000))])

def problem12():
    """First triangle number to have over 500 divisors"""
    count = 1
    number = 2
    def triangles(number):
        tri = (number * (number + 1)) / 2
        return tri
    def divisors(number):
        divs = []
        for i in range(1, int(number ** 0.5) + 1):
            if number % i is 0:
                divs.append(i)
                if i is not number / i:
                    divs.append(number / i)
        return len(divs)
    while count <= 500:
        temp = triangles(number)
        hold = divisors(temp)
        if hold > count:
            count = hold
        number += 1
    print triangles(number - 1)

def problem25():
    """Find first Fibonacci number with 1000 digits"""
    fib = 13
    fib_next = 21
    term = 8
    while len(str(fib_next)) < 1000:
        temp = fib_next
        fib_next = fib + fib_next
        fib = temp
        term += 1
    print term

def problem15():
    """How many routes possible from top-left to bottom-right in 20X20 grid"""
    print math.factorial(40) / (math.factorial(20) * math.factorial(20))

def problem18():
    """Largest total from top of triangle to bottom"""
    table = [[int(n) for n in s.split()] for s in open('p18.txt').readlines()]
    for row in range(len(table)-1, 0, -1):
            for col in range(0, row):
                table[row-1][col] += max(table[row][col], table[row][col+1])

    print table[0][0]

def problem67():
    """Largest total from top of triangle to bottom"""
    table = [[int(n) for n in s.split()] for s in open('triangle.txt').readlines()]
    for row in range(len(table)-1, 0, -1):
            for col in range(0, row):
                table[row-1][col] += max(table[row][col], table[row][col+1])

    print table[0][0]

def problem21():
    """Find sum of all amicable numbers under 10000"""
    div_sums = [0]
    total = 0
    num = 1
    def divisors(number):
        divs = []
        for i in range(1, int(number ** 0.5) + 1):
            if number % i is 0:
                divs.append(i)
                if i is not number / i:
                    divs.append(number / i)
        return sum(divs) - number
    while num < 10001:
        nums = divisors(num)
        if num > nums and divisors(nums) == num:
            total += num + nums
        num += 1
    print total

def problem28():
    """Sum of diagonals in 1001 by 1001 spiral"""
    rows = 500
    print (16 * math.pow(rows, 3) + 26 * rows) / 3 + 10 * math.pow(rows, 2) + 1

def problem22():
    """Total of names in a file"""
    letters = open('letters.txt').readlines()
    letters = letters[0].strip().split(',')
    name_list = open('names.txt').readlines()
    names = name_list[0].strip('"').split('","')
    names.sort()
    names.insert(0, 0)
    letters.insert(0, 0)
    spot = 1
    total = 0
    while spot < len(names):
        let = 1
        subtotal = 0
        for letter in letters:
            if letter is not 0:
                subtotal += names[spot].count(letter) * let
                let += 1
        subtotal *= spot
        total += subtotal
        spot += 1
    print total

def problem97():
    """Last 10 digits of a really big prime number"""
    print (28433 * pow(2, 7830457, 10**10) + 1) % 10**10

def problem19():

    def next_first_of_month_in_20th():
        """Generator to list every first of the month during the 20th century."""
        first = date(1901, 1, 1)
        yield first
        while first.year < 2001:
            if first.month == 12:
                first = first.replace(year=first.year + 1)
                first = first.replace(month=1)
            else:
                first = first.replace(month=first.month + 1)
            yield first

    print len([first for first in next_first_of_month_in_20th() if first.weekday() == 6])

def problem23():
    nums = open('nonabundant.txt', 'r')
    numlist = []
    for line in nums:
        temp = line.split()
        numlist.append(int(temp[1]))
    print sum(numlist)

def problem24():
    nums = permutations('0123456789')
    i = 0
    while i < 1000000:
        perm = next(nums)
        i += 1
    print ''.join(perm)

def problem26():
    def recurring_cycle(n, d):
        for t in range(1, d):
            if 1 == 10**t % d:
                return t
        return 0

    longest = max(recurring_cycle(1, i) for i in range(2, 1001))
    print [i for i in range(2, 1001) if recurring_cycle(1, i) == longest][0]

def problem30():
    nums = []

    for i in range(4000, 200000):
        str_i = str(i)
        sum_5s = 0

        for char in str_i:
            sum_5s += int(char)**5

        if sum_5s == i:
            nums.append(i)

    print sum(nums)

def problem29():
    limit = 100
    nums = set()

    for i in range(2, limit + 1):
        for t in range(2, limit + 1):
            nums.add(i**t)

    print len(nums)



parser = argparse.ArgumentParser(
        description='A command line utility to run the desired Euler problem.',
        epilog='And now you know...')

parser.add_argument('number', help='The problem number...')

args = parser.parse_args()

# Dynamically call a carefully named function based on user input...
eval('problem%s()' % (args.number, ))

# Dynamically build a dictionary to call from...
#problem_set = {
#               '%s' % (args.number, ): eval('problem%s' % (args.number, ))
#              }['%s' % (args.number, )]()

#problem_set = {'problem1':problem1,
#               'problem2':problem2,
#               'problem6':problem6,
#               'problem5':problem5,
#              }['problem%s' % (args.number, )]()

