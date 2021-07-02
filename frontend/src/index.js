import React from "react";
import ReactDom from 'react-dom';

import Root from './Root';

ReactDom.render(
  <React.StrictMode>
    <Root />
  </React.StrictMode>,
  document.getElementById('root')
);