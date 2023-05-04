import "./Root.css";

import Form from "../components/Form";

function Root() {
  return (
    <div className="container">
      <div className="center-text">
        <img src="/static/pmb/logo.png" className="d-block mx-auto" alt="Pay Me Back" />
      </div>
      <div>
        <Form />
      </div>
    </div>
  );
}

export default Root;
