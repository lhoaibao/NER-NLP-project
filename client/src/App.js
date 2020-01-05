import React from 'react';
import 'bootstrap/dist/css/bootstrap.min.css';
class App extends React.Component {
  render() {
    return (
      <html>
        <body>
          <link
            rel="stylesheet"
            href="https://maxcdn.bootstrapcdn.com/bootstrap/4.3.1/css/bootstrap.min.css"
            integrity="sha384-ggOyR0iXCbMQv3Xipma34MD+dH/1fQ784/j6cY/iJTQUOhcWr7x9JvoRxT2MZw1T"
            crossorigin="anonymous"
          />
          <form action="http://localhost:8888/ner/predict" method="get" id='form1'>
              <h2 style={{color:'blue', marginLeft:200}}>Try my Demo (Named Entity Recognition)</h2>
              <div style={{marginLeft:250}}>
                <p>Enter A Text:</p>
                <textarea rows="5" cols="80" name="comment" form="form1" placeholder="Enter text here..."/>
                <br/>
                <input type = "submit" class="btn btn-primary" value = "Extract" />
              </div>
          </form>
        </body>
      </html>
    );
  }
}

export default App;
