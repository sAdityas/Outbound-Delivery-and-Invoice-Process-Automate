def dicttolist(salecode):
    invoice_arrays = []
    Flag = []
    for key, value in salecode.items():
        invoice_arrays.append(key)
        Flag.append(value)
    return invoice_arrays, Flag