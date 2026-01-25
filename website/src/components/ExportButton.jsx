import React from 'react'
import * as XLSX from 'xlsx'

function ExportButton({ selectedIndexes, results }) {

    const handleExportToExcel = () => {
        if (selectedIndexes.length === 0) {
          alert("No rows selected to export.");
          return;
        }
      
        const selectedData = selectedIndexes.map((i) => results[i]);
        
        // Prepare data for the sheet
        const dataForExport = selectedData.map((res) => ({
          Sales_Order: res.sales_order,
          Material: res.material,
          Quantity: res.quantity,
          Invoice_Number: res.invoice_number || '-',
          Status: res.status,
          Error: res.error || '-',
        }));
        
      // Create workbook and sheet
      const workbook = XLSX.utils.book_new();
      const sheet = XLSX.utils.json_to_sheet(dataForExport);
      XLSX.utils.book_append_sheet(workbook, sheet, 'Results');
    
      // Export
      XLSX.writeFile(workbook, 'GeneratedInvoices.xlsx');
    }
  return (
    <div>
    <button
    className='export-button'
    onClick={handleExportToExcel}
    type='button'
    disabled={selectedIndexes.length === 0}>
      Export to Excel
    </button></div>
  )
}

export default ExportButton 
 
