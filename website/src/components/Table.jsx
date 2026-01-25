import React , {useMemo} from 'react'
const COLUMN_LABELS = {
  sales_order: 'Sales Order',
  quantity: 'Quantity',
  invoice_number: 'Invoice Number',
  Invoice_Number: 'Invoice Number',
  Flag: 'Flag',
  Date: 'Date',
  Plant: 'Plant',
  BillType: 'Bill Type',
  status: 'Status',
  error: 'Error',
  final_status: 'Final Status'
};

function Table({ results, selectedIndexes, setSelectedIndexes}) {

  const handleRowClick = (index) => {
    setSelectedIndexes((prev) =>
      prev.includes(index)
        ? prev.filter((i) => i !== index)
        : [...prev, index]
    );
  };

  // 🔹 Build columns dynamically from data
  const columns = useMemo(() => {
    if (!results || results.length === 0) return [];

    const keys = new Set();
    results.forEach(row => {
      Object.keys(row).forEach(key => keys.add(key));
    });

    return Array.from(keys);
  }, [results]);

  if (!results || results.length === 0) return null;

  return (
    <table className="results-table">
      <thead>
        <tr>
          {columns.map((col) => (
            <th key={col}>
              {COLUMN_LABELS[col] || col.replace(/_/g, ' ').toUpperCase()}
            </th>
          ))}
        </tr>
      </thead>

      <tbody>
        {results.map((row, idx) => (
          <tr
            key={idx}
            onClick={() => handleRowClick(idx)}
            className={selectedIndexes.includes(idx) ? 'selected' : ''}
          >
            {columns.map((col) => (
              <td
                key={col}
                className={
                  col === 'status'
                    ? row[col] === 'Success'
                      ? 'status-success'
                      : 'status-failure'
                    : col === 'error'
                    ? 'error-cell'
                    : ''
                }
              >
                {row[col] ?? '-'}
              </td>
            ))}
          </tr>
        ))}
      </tbody>
    </table>
  );
}

export default Table;
