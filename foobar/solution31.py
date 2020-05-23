import functools
totals = 0

def memoize(func):
    cache = func.cache = {}
    @functools.wraps(func)
    def memoized_func(*args, **kwargs):
        key = str(args) + str(kwargs)
        if key not in cache:
            cache[key] = func(*args, **kwargs)
        return cache[key]
    return memoized_func

@memoize
def findsteps(level, stepsleft, current):
    global totals
    debug=0

    savecurrent = current

    donottake=0

    if debug:
        print("at level %i with %i steps left with path %s" % (level,stepsleft, current))
    if level==stepsleft:
        # ok, must be at least two steps so this is good
        totals =totals +1
        current = current + str(level)
        if debug:
            print('               ********  ', current, ' was answer')
        donottake=1
    elif level <=1 or stepsleft <0:
        return
    elif level > stepsleft:
        if debug:
            print('keep going, but do not take the step because level %i > steps %i, so the step would overshoot' % (level, stepsleft))
        #return
        donottake=1

    # ok I think let's do some math to skip maths, like if level = x, and (x^2+x/2) < stepsleft, obviously don't bother
    quickcheck = (level*level + level) / 2
    if quickcheck < stepsleft:
        # impossible, give up
        return

    # ok now we have two options
    # take a step, first not take a step
    # so we should return the sum of these two options
 
    if level==1:
        return
    if not donottake:
        takeastep = findsteps(level-1, stepsleft-level, savecurrent + str(level))
    #notake =    findsteps(level-1, stepsleft,       current )
    notake =    findsteps(level-1, stepsleft,       savecurrent )

    return



def solution(n):
    global totals 
    totals=0
    print("\n")
    print "solving for ", n
    # ok let's phrase the problem
    # at 1 = 0: impossible
    # at 2 = 0: impossible
    # at 3 = 1: one way: 2, 1
    # at 4 = 1: one way: 3, 1
    # at 5 = 2: 41, or 32
    # at 6 = 3: 51, 42, 321
    # at 7 = 4: 61, 52, 43, 421,  
    # at 8 = 5: 71, 62, 53, 521, 431
    # at 9 = 7: 81, 72, 63, 621, 54, 531, 432
    # at 200 = 487067745
    # n will be between 3 and 200 
  
    # Params
    #  level
    #  number of steps left
    #  tracking of current solution
    #foo = findsteps(n-1, n) 
    foo = findsteps(n-1, n, '') 
    return totals 

