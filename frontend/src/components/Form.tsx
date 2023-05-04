import { useNavigate } from "react-router-dom";

function Form() {
  const navigate = useNavigate();

  function generateQrCode() {
    const ids = [
      "iban",
      "amount",
      "due_date",
      "payment_note",
      "beneficiary_name",
      "beneficiary_address1",
      "beneficiary_address2",
      "variable_symbol",
      "specific_symbol",
      "constant_symbol",
    ];
    const inputData: { [key: string]: string } = {};
    for (let id of ids) {
      let idValue = (document.getElementById(id) as HTMLInputElement).value;
      if (idValue) {
        inputData[id] = idValue;
      }
    }

    return fetch("/api/qrcode", {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify(inputData),
    })
      .then((res) => {
        return res.json();
      })
      .then((data) => {
        return data;
      });
  }

  function handleClick(event: React.FormEvent<HTMLButtonElement>) {
    event.preventDefault();
    generateQrCode().then((res) =>
      navigate(`/${res.filename}`, {
        state: {
          qrCodeFilename: res.filename,
          qrCodeFilenameExt: res.filename_ext,
        },
      })
    );
  }

  return (
    <form>
      <div className="g-2 mt-0 row">
        <div className="col">
          <input
            className="form-control"
            id="iban"
            placeholder="IBAN"
            type="text"
          />
        </div>
      </div>
      <div className="g-2 mt-0 row">
        <div className="col">
          <input
            className="form-control"
            id="amount"
            placeholder="Amount"
            step="0.01"
            type="number"
          />
        </div>
        <div className="col">
          <input
            className="form-control"
            id="due_date"
            placeholder="Due Date"
            type="date"
          />
        </div>
      </div>
      <div className="g-2 mt-0 row">
        <div className="col">
          <input
            className="form-control"
            id="payment_note"
            placeholder="Payment Note"
            type="text"
          />
        </div>
      </div>
      <div className="g-2 mt-4 row">
        <div className="col">
          <input
            className="form-control"
            id="beneficiary_name"
            placeholder="Beneficiary Name"
            type="text"
          />
        </div>
      </div>
      <div className="g-2 mt-0 row">
        <div className="col">
          <input
            className="form-control"
            id="beneficiary_address1"
            placeholder="Beneficiary Address 1"
            type="text"
          />
        </div>
      </div>
      <div className="g-2 mt-0 row">
        <div className="col">
          <input
            className="form-control"
            id="beneficiary_address2"
            placeholder="Beneficiary Address 2"
            type="text"
          />
        </div>
      </div>
      <div className="g-2 mt-4 row">
        <div className="col">
          <input
            className="form-control"
            id="variable_symbol"
            placeholder="VS"
            type="text"
          />
        </div>
        <div className="col">
          <input
            className="form-control"
            id="specific_symbol"
            placeholder="SS"
            type="text"
          />
        </div>
        <div className="col">
          <input
            className="form-control"
            id="constant_symbol"
            placeholder="CS"
            type="text"
          />
        </div>
      </div>
      <div className="g-2 justify-content-md-center mt-4 row">
        <div className="col-md-auto">
          <button
            className="btn btn-primary"
            onClick={handleClick}
            type="button"
          >
            Generate QR Code
          </button>
        </div>
      </div>
    </form>
  );
}

export default Form;
