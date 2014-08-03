# index, value lenghth
# returns roman str for the specivied tens slot (i)
def rom(i, x, len):
    tens = 1
    for each in range(0, i):
        tens*=10
    
    roms = { 1 : 'I',
             2 : 'II',
             3 : 'III',
             4 : 'IV',
             5 : 'V',
             6 : 'VI',
             7 : 'VII',
             8 : 'VIII',
             9 : 'IX' }
    # should pull the number form the dictionary
    roman = roms[x]
    
    # prints to verify digit spot for manual validation
    # print str(tens) + ": " + roman
    
    # conditionals to replace for the right tens spot
    # range 10 - 99
    if (x*tens) >= 10 and (x*tens) < 100:
        roman = roman.replace('X', 'C')
        roman = roman.replace('I', 'X')
        roman = roman.replace('V', 'L')
    # range 100 - 999
    elif (x*tens) >= 100 and (x*tens) < 1000:
        roman = roman.replace('X', 'M')
        roman = roman.replace('I', 'C')
        roman = roman.replace('V', 'D')
    # range 1000+
    elif (x*tens) >= 1000:
        roman = roman.replace('I', 'M')
    
    return roman
# main call
def main():    
    x = 2016
    str_x = str(x)[::-1]
    roman = ''
    roman_list = []
    for i in range(0, len(str_x)):
        if str_x[i] != '0':
            roman_list.append(rom(i, int(str_x[i]), len(str_x)))
    for each in roman_list[::-1]:
        roman += each
    print roman
if __name__ == "__main__":
    main()