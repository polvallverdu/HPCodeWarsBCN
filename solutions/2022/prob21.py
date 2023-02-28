
def transform_int_to_roman(num: int) -> str:
        val = [
            1000, 900, 500, 400,
            100, 90, 50, 40,
            10, 9, 5, 4,
            1
        ]
        syb = [
            "M", "CM", "D", "CD",
            "C", "XC", "L", "XL",
            "X", "IX", "V", "IV",
            "I"
        ]
        roman_num = ''
        i = 0
        while num > 0:
            for _ in range(num // val[i]):
                roman_num += syb[i]
                num -= val[i]
            i += 1
        return roman_num

roman_decimal = {
  '0': '',
  '083':'.',
  '166':':',
  '25':':.',
  '333':'::',
  '416':'::.',
  '5':'S',
  '583':'S.',
  '666':'S:',
  '75':'S:.',
  '833':'S::',
  '916':'S::.',
}


number  = str(float(input()))


integer, decimal = number.split('.')
if decimal not in roman_decimal:
  print('ERROR')
else:
  
  roman_dec_number = roman_decimal[decimal]
  roman_int_number = transform_int_to_roman(int(integer))
  print(roman_int_number + roman_dec_number)


