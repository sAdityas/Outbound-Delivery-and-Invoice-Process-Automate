import pandas as pd
import os 
def excelReader(filepath):
    df = pd.read_excel(filepath) if filepath.endswith(".xlsx") else pd.read_csv(filepath)

    # Normalize column headers
    df.columns = df.columns.str.strip()

    # Map columns based on uploaded format
    Document_Date = pd.to_datetime(df['Document Date'], dayfirst=True).dt.strftime('%d.%m.%Y').tolist()
    Sales_Document_Type = df['Sales Document Type'].tolist()
    Sales_Document = df['Sales Document'].tolist()
    Quantity = df['Order Quantity (Item)'].tolist()
    Vehicle_Number = df['Vehicle Number'].tolist()
    LR_Number = df['LR Number'].tolist()
    Number_of_Package = df['Number of Package'].tolist()
    Partner_ID = df['Partner ID'].tolist()
    Plant = df['Plant'].tolist()
    pincode = df['pincode'].tolist()
    return (
        Sales_Document,
        Sales_Document_Type,
        Quantity,
        Vehicle_Number,
        LR_Number,
        Number_of_Package,
        Partner_ID,
        Plant,
        Document_Date,
        pincode
    )


def save_csv(csv_rows):
    csv_rows = csv_rows[0]
    print(csv_rows)
    folder_path = r"D:/"
    file_name = "DoNotDelete.csv"

    full_path = os.path.join(folder_path, file_name)

    df = pd.DataFrame({
        "Invoice_Number": csv_rows['invoice_number'],
        "Flag": csv_rows['Flag'],
        "Date": csv_rows['LR_Date'],
        "Plant": csv_rows['Plant'],
        'BillType': csv_rows['BillType']
    })

    df.to_csv(full_path, index=False)

    return full_path
  
def read_csv(filepath):
    df = pd.read_csv(filepath)
    df.columns = df.columns.str.strip()

    return (
        df['Invoice_Number'].tolist(),
        df['Flag'].tolist(),
        df['Date'].tolist(),
        df['Plant'].tolist(),
        df['BillType'].tolist()
    )


