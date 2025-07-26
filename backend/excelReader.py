import pandas as pd

def excelReader(filepath):
    df = pd.read_excel(filepath) if filepath.endswith(".xlsx") else pd.read_csv(filepath)

    # Normalize column headers
    df.columns = df.columns.str.strip()

    # Map columns based on uploaded format
    Document_Date = pd.to_datetime(df['Document Date']).dt.strftime('%d.%m.%Y').tolist()
    Sales_Document_Type = df['Sales Document Type'].tolist()
    Sales_Document = df['Sales Document'].tolist()
    Quantity = df['Order Quantity (Item)'].tolist()
    Vehicle_Number = df['Vehicle Number'].tolist()
    LR_Number = df['LR Number'].tolist()
    Number_of_Package = df['Number of Package'].tolist()
    Partner_ID = df['Partner ID'].tolist()
    Plant = df['Plant'].tolist()

    return (
        Sales_Document,
        Sales_Document_Type,
        Quantity,
        Vehicle_Number,
        LR_Number,
        Number_of_Package,
        Partner_ID,
        Plant,
        Document_Date
    )
