def ppc(invoice, postalcodearray, pincode):
    result = {}
    for i in range(min(len(invoice), len(postalcodearray), len(pincode))):
        result[invoice[i]] = int(postalcodearray[i]) == int(pincode[i])

    return result