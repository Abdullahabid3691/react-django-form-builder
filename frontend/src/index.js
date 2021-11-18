import React from 'react';
import ReactDOM from 'react-dom';
import { Provider } from 'react-redux';
import {Switch, Route, Router} from 'react-router-dom';

import { store, history} from './store/store';
import App from './components/App';

ReactDOM.render((
  <Provider store={store}>
    <Router history={history}>
      <Switch>
        <Route path="/" component={App} />
      </Switch>
    </Router>
  </Provider>

), document.getElementById('root'));

// If you want to start measuring performance in your app, pass a function
// to log results (for example: reportWebVitals(console.log))
// or send to an analytics endpoint. Learn more: https://bit.ly/CRA-vitals
// reportWebVitals();
