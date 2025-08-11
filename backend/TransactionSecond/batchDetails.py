from connectionSAP import connection
import time

def batchInputVL01N(session, Quantity):
    """Input batch quantity for SAP VL01N based on user-specified quantity."""

    # 1️⃣ Collect original batch quantities
    bQty = []
    for row in range(0,100):
        try:
            qty_path = f"wnd[0]/usr/tabsTAXI_TABSTRIP_ITEM/tabpT\\03/ssubSUBSCREEN_BODY:SAPMV50A:3112/tblSAPMV50ATC_LIPS_CHND/txtLIPS-LFIMG[4,{row}]"
            qty_field = session.findById(qty_path)
            qty_text = qty_field.text.replace(',', '').strip()
            if qty_text == '':
                break
            batch_quantity = int(qty_text)
            bQty.append(batch_quantity)
        except Exception as e:
            return  # Exit function if any error occurs

    # At the top of batchInputVL01N
    if not bQty or sum(bQty) < Quantity:
        raise ValueError(f"Total available Material {sum(bQty)} is less than required {Quantity}.")
    

    # 3 Otherwise, scale across batch lines
    scaled = []
    remaining = Quantity
    for batch_quantity in bQty:
        if remaining <= 0:
            scaled.append(0)
        elif batch_quantity <= remaining:
            scaled.append(batch_quantity)
            remaining -= batch_quantity
        else:
            scaled.append(remaining)
            remaining = 0

    # 4️⃣ Apply updated quantities and collect rows with quantity == 0
    delete_rows = []
    for row, quantity_to_set in enumerate(scaled):
        try:
            batch_path = f"wnd[0]/usr/tabsTAXI_TABSTRIP_ITEM/tabpT\\03/ssubSUBSCREEN_BODY:SAPMV50A:3112/tblSAPMV50ATC_LIPS_CHND/ctxtLIPS-CHARG[1,{row}]"
            qty_path = f"wnd[0]/usr/tabsTAXI_TABSTRIP_ITEM/tabpT\\03/ssubSUBSCREEN_BODY:SAPMV50A:3112/tblSAPMV50ATC_LIPS_CHND/txtLIPS-LFIMG[4,{row}]"

            batch_field = session.findById(batch_path)
            if not batch_field.text.strip():
                break

            qty_field = session.findById(qty_path)
            qty_field.text = str(quantity_to_set)

            if quantity_to_set == 0 and len(scaled) > 1:
                delete_rows.append(row)

        except Exception as e:
            break

    # 5️⃣ Delete surplus batch lines
    for row in reversed(delete_rows):
        try:
            batch_path = f"wnd[0]/usr/tabsTAXI_TABSTRIP_ITEM/tabpT\\03/ssubSUBSCREEN_BODY:SAPMV50A:3112/tblSAPMV50ATC_LIPS_CHND/ctxtLIPS-CHARG[1,{row}]"
            batch_field = session.findById(batch_path)
            batch_field.setFocus()
            session.findById("wnd[0]/usr/tabsTAXI_TABSTRIP_ITEM/tabpT\\03/ssubSUBSCREEN_BODY:SAPMV50A:3112/subSUBSCREEN_ICONBAR:SAPMV50A:3702/btnBT_POLO_T").press()
            time.sleep(0.5)

            try:
                session.findById("wnd[1]/usr/btnSPOP-OPTION1").press()
                time.sleep(0.5)
            except:
                pass
        except Exception as e:
            raise (e)