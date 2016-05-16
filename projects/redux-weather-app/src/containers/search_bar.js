import React, { Component } from 'react';

export default class SearchBar extends Component {
  constructor(props) {
    super(props);

    this.state = { term: '' };
    // bind this.onInputChange to the SearchBar
    this.onInputChange = this.onInputChange.bind(this);
  }

  onInputChange(event) {
      this.setState({ term: event.target.value });
  }

  onFormSubmit(event) {
    event.preventDefault();

    //here is where we want to go and fetch data
  }

  render() {
    return (
      <form onSubmit={ this.onFormSubmit } className='input-group'>
        <input
          placeholder='Get a five-day forecast in you favorite cities' className='form-control'
          value={this.state.term}
          onChange={this.onInputChange} />
        <span className="input-group-btn">
          <button type="submit" className='btn btn-secondary'>Submit</button>
        </span>
      </form>
    );
  }
}
