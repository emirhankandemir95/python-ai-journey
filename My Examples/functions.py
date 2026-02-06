def sayHello(name = 'User'):
    return 'Hello '+ name

msg = sayHello('Çınar')
msg = sayHello('Ada')
print(msg)

def total(num1, num2):
    return num1 + num2

result = total(10,20)
result = total(15,20)
print(result)

def ageCalc(birthYear):
    return 2019 - birthYear

ageCinar =ageCalc(2017)
ageAda =ageCalc(2010)
ageSena =ageCalc(1999)

print(ageCinar, ageAda, ageSena)


def retirementYear(birthYear, name):
    '''
    DOCSTRING: Dogum yiliniza gore emekliliginize kac yil kaldi
    INPUT: Dogum Yili
    OUTPUT: Hesaplanan yil bilgisi
    '''
    age = ageCalc(birthYear)
    retirement = 65 - age

    if retirement > 0:
        print(f'Emekliliğinize {retirement} yıl kaldı' )
    else:
        print('Zaten emekli oldunuz')

retirementYear(1983, 'Ali')
retirementYear(1950, 'Ahmet')
retirementYear(1974, 'Yağmur')

print(help(retirementYear))

list = [1,2,3]

print(help(list.append))