import { createStore } from 'redux';
import reducer from './reducer';import { createHashHistory } from 'history'

// import createHistory from 'history/createBrowserHistory';

// export const history = createHistory();
// Create an enhanced history that syncs navigation events with the store
export const history = createHashHistory()


export const store = createStore(reducer);