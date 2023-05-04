import "./Root.css";

import { useLocation, useParams } from "react-router-dom";
import { validate as uuidValidate } from "uuid";

function CheckIfQrCodeExists() {
  const location = useLocation();
  const params = useParams();
  const qrCode = params.qrcode;
  if (uuidValidate(qrCode as string)) {
    return (
      <img
        src={`/static/pmb/qr-codes/${location.state.qrCodeFilename}.${location.state.qrCodeFilenameExt}`}
        className="d-block mx-auto"
        alt="QR code not found"
      />
    );
  } else {
    return <p>QR code does not exist.</p>;
  }
}

function QrCode() {
  return (
    <div className="center-text container">
      <CheckIfQrCodeExists />
    </div>
  );
}

export default QrCode;
