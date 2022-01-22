import React, { Component } from 'react';
import './App.css';
import AppBar from '@material-ui/core/AppBar';
import Toolbar from '@material-ui/core/Toolbar';
import Typography from '@material-ui/core/Typography';
import { withStyles } from '@material-ui/core/styles';
import InputLabel from '@material-ui/core/InputLabel';
import MenuItem from '@material-ui/core/MenuItem';
import FormControl from '@material-ui/core/FormControl';
import Select from '@material-ui/core/Select';
import TextField from '@material-ui/core/TextField';
import List from '@material-ui/core/List';
import ListItem from '@material-ui/core/ListItem';
import ListItemText from '@material-ui/core/ListItemText';
import ListSubheader from '@material-ui/core/ListSubheader';
import Paper from '@material-ui/core/Paper';
import Grid from '@material-ui/core/Grid';
import Button from '@material-ui/core/Button';

const styles = {
  list: {
    width: '100%',
    maxWidth: 360,
    position: 'relative',
    overflow: 'auto',
    maxHeight: 300,
  },
  text: {
    width: 400,
    
  },
  select: {
    width: 400
  },
  grid: {
    paddingBottom: 10
  },
  paper: {
    width: 700
  }
}

class App extends Component {
  state = {
    text: '',
    size: 1,
    results: [],
    error: null
  }

  handleTextChange = (event) => {
    this.setState({ text: event.target.value });
  }

  handleSelectChange = (event) => {
    this.setState({ size: event.target.value });
  }

  handleSubmit = () => {
    fetch("http://localhost:5000/bruteforce/", {
      method: 'post',
      body: JSON.stringify({
        text: this.state.text,
        size: this.state.size
      })
    })
    .then(res => res.json())
    .then(
      (result) => {
        this.setState({
          results: result
        });
      },
      // Note: it's important to handle errors here
      // instead of a catch() block so that we don't swallow
      // exceptions from actual bugs in components.
      (error) => {
        this.setState({
          error
        });
      }
    )
  }

  render() {
    return (
      <div className="App">
        <AppBar position="absolute" color="default">
          <Toolbar>
            <Typography variant="h6" color="inherit" noWrap>
              Vantage Test - Decrypt it!
            </Typography>
          </Toolbar>
        </AppBar>
        <link rel="stylesheet" href="https://fonts.googleapis.com/css?family=Roboto:300,400,500" />
        <Grid className="App-header" styles={{width:'100%'}} container>
          <Grid item xs={12} className={this.props.classes.grid}>
            <TextField
              id="text"
              label="Encrypted text"
              value={this.state.text}
              className={this.props.classes.text}
              onChange={this.handleTextChange}
            />
          </Grid>
          <Grid item xs={12} className={this.props.classes.grid}>
            <FormControl>
              <InputLabel htmlFor="key-size">Key size</InputLabel>
              <Select
                onChange={this.handleSelectChange}
                className={this.props.classes.select}
                value={this.state.size}
                inputProps={{
                  name: 'size',
                  id: 'key-size',
                }}
              >
                <MenuItem value={1}>1</MenuItem>
                <MenuItem value={2}>2</MenuItem>
                <MenuItem value={3}>3</MenuItem>
                <MenuItem value={4}>4</MenuItem>
                <MenuItem value={5}>5</MenuItem>
                <MenuItem value={6}>6</MenuItem>
                <MenuItem value={7}>7</MenuItem>
              </Select>
            </FormControl>
          </Grid>

          <Grid item xs={12} className={this.props.classes.grid}>
            <Button fullWidth onClick={this.handleSubmit}>Submit</Button>
          </Grid>

          <Paper className={this.props.classes.paper}>
            <List>
            <ListSubheader>Suggested decryptions</ListSubheader>
            {
              this.state.results.map((item, index) => (
                <ListItem key={index}>
                  <ListItemText>{item[0]} - {item[1]}</ListItemText>
                </ListItem>
              ))
            }
          </List>
        </Paper>
        </Grid>
      </div>
    );
  }
}

export default withStyles(styles)(App);
