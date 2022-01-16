lengthDict = {
    "m": 1.0,
    "ft": 3.2808399,
    "in": 39.37007874,
}
weightDict = {
    "kg": 1.0,
    "oz": 35.27396195,
    "lb": 2.20462262,
}
areaDict = {
    "m2": 1.0,
    "ha": 0.0001,
    "sy": 1.19599005,
}

unit = [lengthDict, weightDict, areaDict]


def convertUnitMath(inputUnitType, inputUnit, inputNumber, outputUnit):
    if 0 > inputUnitType > len(unit) or isinstance(inputUnitType, int) == False:
        return "unsupported kind of unit"
    if inputUnit not in unit[inputUnitType]:
        return "unsupported input unit"
    if outputUnit not in unit[inputUnitType]:
        return "unsupported output unit"

    if isinstance(inputNumber, float) or isinstance(inputNumber, int):
        unitPer = 1.0
        if unit[inputUnitType][inputUnit] != 1.0:
            unitPer = 1.0/unit[inputUnitType][inputUnit]
        output = unitPer * unit[inputUnitType][outputUnit] * inputNumber
        return "%s %s = %s %s" % (inputNumber, inputUnit, output, outputUnit)
    else:
        return "please enter a number"


def addCustomUnit(unitType, unitName, unitPer):
    unit[unitType].update({unitName: unitPer})


print(convertUnitMath(1, 'bb', 10, 'oz'))
print(convertUnitMath(1, 'oz', 16, 'lb'))
addCustomUnit(1, "hulahula", 3.14)
print(convertUnitMath(1, 'oz', 73.941, 'hulahula'))
print('=======================================================================================')
