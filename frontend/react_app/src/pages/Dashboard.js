import React, { useState, useEffect } from 'react';
import { withStyles, makeStyles } from '@material-ui/core/styles';
import Table from '@material-ui/core/Table';
import TableBody from '@material-ui/core/TableBody';
import TableCell from '@material-ui/core/TableCell';
import TableContainer from '@material-ui/core/TableContainer';
import TableHead from '@material-ui/core/TableHead';
import TableRow from '@material-ui/core/TableRow';
import Paper from '@material-ui/core/Paper';

import { API_SERVER } from '../settings.js';

const StyledTableCell = withStyles((theme) => ({
  head: {
    backgroundColor: "#2196f3",
    color: theme.palette.common.white,
  },
  body: {
    fontSize: 14,
  },
}))(TableCell);

const useStyles = makeStyles({
  table: {
    minWidth: 700,
  },
});

export default function Dashboard(props) {
    const  [ hasError, setErrors ] =  useState(false);
    const  [ trips, setTrips ]= useState([]);
    const [ loading, setLoading ] = useState(false)
    const classes = useStyles();

    const header = new Headers({'Authorization': `Token ${props.token}`});
    const request = new Request(`${API_SERVER}/api/trips/`, {
      method: 'GET',
      headers: header
    })
    async function fetchData() {
        const res = await fetch(request);
        res.json()
        .then(res => {
            setTrips(res)
        })
        .catch(err => setErrors(err));
    }
    useEffect(() => {
        fetchData();
    }, [])

    return (
        <TableContainer component={Paper}>
        <Table className={classes.table} aria-label="customized table">
            <TableHead>
            <TableRow>
                <StyledTableCell>Trips</StyledTableCell>
                <StyledTableCell align="right">Start&nbsp;Date</StyledTableCell>
                <StyledTableCell align="right">Location</StyledTableCell>
                <StyledTableCell align="right">Budget</StyledTableCell>
                <StyledTableCell align="right">Classification</StyledTableCell>
            </TableRow>
            </TableHead>
            <TableBody>
            {trips.map((row) => (
                <TableRow 
                    key={row.id}
                    onClick={() => { alert('navigate to trip details') }}
                    hover
                >
                    <TableCell component="th" scope="row">{row.name}</TableCell>
                    <TableCell align="right">{row.startdate}</TableCell>
                    <TableCell align="right">{row.start_location}</TableCell>
                    <TableCell align="right">{row.budget}</TableCell>
                    <TableCell align="right">{row.classification ? row.classification : '--'}</TableCell>
                </TableRow>
            ))}
            </TableBody>
        </Table>
        </TableContainer>
    );
}
