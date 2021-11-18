import Banner from './Banner';
import React from 'react';
class Home extends React.Component {
  componentWillMount() {
  }

  componentWillUnmount() {
  }

  render() {
    return (
      <div className="home-page">
        <h3>Testssetst </h3>
        <Banner token={this.props.token} appName={this.props.appName} />

        <div className="container page">
          <div className="row">
            <Banner />

            <div className="col-md-3">
              <div className="sidebar">

                <p>Popular Tags</p>

              </div>
            </div>
          </div>
        </div>

      </div>
    );
  }
}

export default Home // connect(mapStateToProps, mapDispatchToProps)(Home);
