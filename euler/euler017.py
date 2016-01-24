# Enter your code here. Read input from STDIN. Print output to STDOUT

words = {
    '0' : "",
    '1' : "One",
    '2' : "Two",
    '3' : "Three",
    '4' : "Four",
    '5' : "Five",
    '6' : "Six",
    '7' : "Seven",
    '8' : "Eight",
    '9' : "Nine",
    '10' : "Ten",
    '11' : "Eleven",
    '12' : "Twelve",
    '13' : "Thirteen",
    '14' : "Fourteen",
    '15' : "Fifteen",
    '16' : "Sixteen",
    '17' : "Seventeen",
    '18' : "Eighteen",
    '19' : "Nineteen",
    '20' : "Twenty",
    '30' : "Thirty",
    '40' : "Forty",
    '50' : "Fifty",
    '60' : "Sixty",
    '70' : "Seventy",
    '80' : "Eighty",
    '90' : "Ninety",
}


def translate(number):
    returnval = ''
    if number >= 100:
        (quotient, remainder) = divmod(number, 100)    
        #print quotient
        hundreds = words[str(quotient)]
        returnval = hundreds + ' Hundred '
        number = remainder
    
    if number <=20:
        if number > 0:
            lows = words[str(number)]
            returnval = returnval + ' ' + lows
    else:
        (tens, leftover) = divmod(number, 10)
        tens = str(int(tens) * 10)
        tens = words[tens]
        returnval = returnval + ' ' + tens
        if leftover > 0:
            returnval = returnval + ' ' + words[str(leftover)]
    
    return returnval
        

def convert(number):
    if number == 0:
        return 'Zero'
    returnval = ''
    if number > 999999999:
        (quotient, remainder) = divmod(number, 1000000000)
        billions = translate(quotient)
        number = remainder
        returnval = billions + ' Billion '
    
    if number > 999999:
        (quotient, remainder) = divmod(number, 1000000)
        millions = translate(quotient)
        number = remainder
        returnval = returnval + millions + ' Million '
    
    if number > 999:
        (quotient, remainder) = divmod(number, 1000)
        thousands = translate(quotient)
        number = remainder
        #print thousands, 'was thousands'
        returnval = returnval + thousands + ' Thousand '
    
    if number > 0:
        lows = translate(number)
        returnval = returnval + lows
        
    return returnval






samples = input()
for i in xrange(samples):
    number = input()
    # collapse multiple space with the join/split
    # remove leading/trailing with strip
    print ' '.join(convert(number).split()).strip()
    

