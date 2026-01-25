import { useState } from "react";
import axios from "axios";
import "../style/zdsc.css";

export default function App() {
  const [firstInvoice, setFirstInvoice] = useState("");
  const [lastInvoice, setLastInvoice] = useState("");
  const [firstDate, setFirstDate] = useState("");
  const [lastDate, setLastDate] = useState("");
  const [plant, setPlant] = useState("");
  const [loading, setLoading] = useState(false);
  const [typeofinvoice, setTypeofinvoice] = useState("1");

  const handlenavigate = () => {
    window.location.replace("/");
  };

  const formatDate = (dateStr) => {
    if (!dateStr) return "";
    const [year, month, day] = dateStr.split("-");
    return `${day}.${month}.${year}`;
  };

  const genirn = async (e) => {
    e.preventDefault();
    setLoading(true);

    try {
      await axios.post("http://localhost:5050/irn", {
        data: {
          firstInvoice,
          lastInvoice,
          firstDate: formatDate(firstDate),
          lastDate: formatDate(lastDate),
          plant,
        },
      });

      alert("Process Complete");
    } catch (err) {
      alert("Process Failed");
      console.log(err)
    } finally {
      setLoading(false);
    }
  };

  const sendData = async (e) => {
    e.preventDefault();
    setLoading(true);

    try {
      await axios.post("http://localhost:5050/zdsc", {
        data: {
          firstInvoice,
          lastInvoice,
          firstDate: formatDate(firstDate),
          lastDate: formatDate(lastDate),
          plant,
          typeofinvoice,
        },
      });

      alert("Process Complete");
    } catch (err) {
      alert("Process Failed");
      console.log(err)
    } finally {
      setLoading(false);
    }
  };

  return (
    <div className="page">

      {/* Form */}
      <div className="form-wrapper">
        <form onSubmit={sendData} className="form-box">
          <h2 className="form-title">Invoice Selection</h2>

          <div className="field">
            <label className="label">From Invoice</label>
            <input className="input" value={firstInvoice} onChange={(e) => setFirstInvoice(e.target.value)} />
          </div>

          <div className="field">
            <label className="label">To Invoice</label>
            <input className="input" value={lastInvoice} onChange={(e) => setLastInvoice(e.target.value)} />
          </div>

          <div className="field">
            <label className="label">From Date</label>
            <input type="date" className="input" value={firstDate} onChange={(e) => setFirstDate(e.target.value)} />
          </div>

          <div className="field">
            <label className="label">To Date</label>
            <input type="date" className="input" value={lastDate} onChange={(e) => setLastDate(e.target.value)} />
          </div>

          <div className="field">
            <label className="label">Plant</label>
            <input className="input" value={plant} onChange={(e) => setPlant(e.target.value)} />
          </div>

          {/* Radio */}
          <div className="radio-group">
            <label className="label">Type of Invoice</label>
            <div className="radio-options">
              <label className="radio-option">
                <input type="radio" value="1" checked={typeofinvoice === "1"} onChange={(e) => setTypeofinvoice(e.target.value)} />
                Tax Invoice
              </label>
              <label className="radio-option">
                <input type="radio" value="2" checked={typeofinvoice === "2"} onChange={(e) => setTypeofinvoice(e.target.value)} />
                Credit/Debit Note
              </label>
            </div>
          </div>

          {loading ? (
            <div className="loader-wrapper">
              <span className="loader"></span>
            </div>
          ) : (
            <div className="button-row">
              <button type="submit" className="action-btn">Generate DSC</button>
              <button type="button" onClick={genirn} className="action-btn">Generate IRN</button>
            </div>
          )}        
          <button className="back-btn" onClick={handlenavigate} type="button">
          Back
        </button>
        </form>
        

      </div>
    </div>
  );
}
