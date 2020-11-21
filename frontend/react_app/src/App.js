import React from 'react';
import Urls from './routes/urls';
import Layout from './components/Layout';
import {connect} from 'react-redux';
import * as actions from './store/authActions';
import { StyleSheet } from 'react-native';

function App(props) {

  React.useEffect(() => {
    props.setAuthenticatedIfRequired();
  }, []);

  return (
    <div className="App">
      <Layout {...props}>
         <Urls {...props}/>
      </Layout>
    </div>
  );
}

//This means that one or more of the redux states in the store are available as props
const mapStateToProps = (state) => {
  return {
    isAuthenticated: state.auth.token !== null && typeof state.auth.token !== 'undefined',
    token: state.auth.token
  }
}

//This means that one or more of the redux actions in the form of dispatch(action) combinations are available as props
const mapDispatchToProps = (dispatch) => {
  return {
    setAuthenticatedIfRequired: () => dispatch(actions.authCheckState()),
    logout: () => dispatch(actions.authLogout())
  }
}

const styles = StyleSheet.create({
  container: {
    flex: 1,
    backgroundColor: '#fff',
  },
  engine: {
    position: 'absolute',
    right: 0,
  },
  sectionContainer: {
    marginTop: 32,
    paddingHorizontal: 24,
  },
  sectionTitle: {
    fontSize: 24,
    fontWeight: '600',
  },
  sectionDescription: {
    marginTop: 8,
    fontSize: 18,
    fontWeight: '400',
  },
  highlight: {
    fontWeight: '700',
  },
  footer: {
    fontSize: 12,
    fontWeight: '600',
    padding: 4,
    paddingRight: 12,
    textAlign: 'right',
  },
  chips: {
    display: 'flex',
    justifyContent: 'center',
    flexWrap: 'wrap',
    margin: 2,
  },
});

export default connect(mapStateToProps, mapDispatchToProps)(App);