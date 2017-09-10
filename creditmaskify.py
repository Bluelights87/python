# return masked string
def maskify(cc):
  numChar = len(str(cc))
  maskVal = numChar - 4
  creditVal = [int(d) for d in str(cc)]
  print(creditVal)
  maskedCard = '#' * maskVal + str(creditVal[numChar - 4]) + str(creditVal[numChar - 3]) + str(creditVal[numChar - 2]) + str(creditVal[numChar - 1])
  print(maskedCard)
##  print('#' * maskVal + str(creditVal[numChar - 4]) + str(creditVal[numChar - 3]) + str(creditVal[numChar - 2]) + str(creditVal[numChar]))
maskify(2344581820391875)