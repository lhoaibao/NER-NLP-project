import React from 'react';
import 'bootstrap/dist/css/bootstrap.min.css';

class App extends React.Component {
  render() {
    return (
      <html>
        <link
          rel="stylesheet"
          href="https://maxcdn.bootstrapcdn.com/bootstrap/4.3.1/css/bootstrap.min.css"
          integrity="sha384-ggOyR0iXCbMQv3Xipma34MD+dH/1fQ784/j6cY/iJTQUOhcWr7x9JvoRxT2MZw1T"
          crossorigin="anonymous"
        />
        <form id='form1'>
            <h2 style={{color:'blue', marginLeft:200}}>Try my Demo (Named Entity Recognition)</h2>
            <div style={{marginLeft:250}}>
              <p>Enter A Text:</p>
              <textarea rows="10" cols="100" name="comment" form="usrform" placeholder="Enter text here..."/>
            </div>
        </form>
        <br/>
        <button style={{marginLeft:250}} type="button" class="btn btn-primary" form='form1'>Extract</button>
      </html>
    );
  }
}

export default App;
