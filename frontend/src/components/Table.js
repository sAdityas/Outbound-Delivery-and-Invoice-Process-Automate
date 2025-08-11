import React from 'react'


function Table( {results, selectedIndexes, setSelectedIndexes}) {

    const handleRowClick = (index) => {
        setSelectedIndexes((prev) =>
          prev.includes(index)
            ? prev.filter((i) => i !== index) // remove if already selected
            : [...prev, index]                // add if not selected
        );
      };
  return (
    <div> 
         <table className="results-table">
              <thead>
                <tr>
                  <th>Sales Order</th>
                  <th>Quantity</th>
                  <th>Invoice Number</th>
                  <th>Status</th>
                  <th>Error</th>
                </tr>
              </thead>
              <tbody>
                {results.map((res, idx) => (
                  <tr key={idx}
                  onClick={() => handleRowClick(idx)}
                  className={selectedIndexes.includes(idx) ? 'selected' : ''}>
                    <td>{res.sales_order}</td>
                    <td>{res.quantity}</td>
                    <td>{res.invoice_number || '-'}</td>
                    <td className={res.status === 'Success' ? 'status-success' : 'status-failure'}>
                      {res.status}
                    </td>
                    <td className="error-cell">{res.error || '-'}</td>
                  </tr>
                ))}
              </tbody>
            </table>
    </div>
  )
}

export default Table