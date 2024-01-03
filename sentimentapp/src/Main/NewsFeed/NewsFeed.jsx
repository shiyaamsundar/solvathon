import React from 'react'
import './newsfeed.css';
import TextField from '@mui/material/TextField';
import Autocomplete from '@mui/material/Autocomplete';
import Box from '@mui/material/Box';
import InputLabel from '@mui/material/InputLabel';
import MenuItem from '@mui/material/MenuItem';
import FormControl from '@mui/material/FormControl';
import Select from '@mui/material/Select';
import Button from '@mui/material/Button';
import SearchIcon from '@material-ui/icons/Search';
import Stack from '@mui/joy/Stack';
import LinearProgress from '@mui/joy/LinearProgress';


const NewsFeed = () => {
    const [age, setAge] = React.useState('');

    const handleChange = (event) => {
        setAge(event.target.value);
      };
    const top100Films = [
        { label: 'The Shawshank Redemption', year: 1994 },
        { label: 'The Godfather', year: 1972 },
        { label: 'The Godfather: Part II', year: 1974 },
        { label: 'The Dark Knight', year: 2008 },
        { label: '12 Angry Men', year: 1957 },
        { label: "Schindler's List", year: 1993 },
        { label: 'Pulp Fiction', year: 1994 },
    ]
  return (
    <div className='news-card-container'>
        <div className="news-card-header">
        
      <FormControl sx={{ m: 1, minWidth: 120 }}>
        <InputLabel id="demo-simple-select-label">Age</InputLabel>
        <Select
          labelId="demo-simple-select-label"
          id="demo-simple-select"
          value={age}
          label="Age"
          onChange={handleChange}
        >
          <MenuItem value={10}>Ten</MenuItem>
          <MenuItem value={20}>Twenty</MenuItem>
          <MenuItem value={30}>Thirty</MenuItem>
        </Select>
      </FormControl>
   
    <Box sx={{ maxWidth: 150 }}>
        <Autocomplete
  disablePortal
  id="combo-box-demo"
  options={top100Films}
  sx={{ width: 150 }}
  renderInput={(params) => <TextField {...params} label="Movie" />}
/>
</Box>
<Button variant="outlined" endIcon={<SearchIcon />}>
  Delete
</Button>
        </div>
        <div className="news-card">
            <div className="news-card-title">
                Lorem ipsum dolor sit amet consectetur adipisicing elit. Nobis, eum.
            </div>
            <p>Lorem ipsum dolor sit amet consectetur adipisicing elit. Maxime blanditiis saepe totam cumque ipsum omnis voluptatum molestias et facilis suscipit, dolorem similique necessitatibus doloremque modi corporis consequuntur debitis praesentium. Magni nulla tempore sed eos? Expedita voluptatum dolores impedit voluptates itaque. Quo quidem aut ipsa! Incidunt facere perferendis corporis praesentium est.</p>
            <p className='news-sentiment'>Positive</p>
            <Stack spacing={2} sx={{ flex: 1 }}>
      <LinearProgress determinate value={25} variant="solid" color="primary"/>
    </Stack>
            <div className="news-p">see more...</div>
        </div>
        <div className="news-card">
            <div className="news-card-title">
                Lorem ipsum dolor sit amet consectetur adipisicing elit. Nobis, eum.
            </div>
            <p>Lorem ipsum dolor sit amet consectetur adipisicing elit. Maxime blanditiis saepe totam cumque ipsum omnis voluptatum molestias et facilis suscipit, dolorem similique necessitatibus doloremque modi corporis consequuntur debitis praesentium. Magni nulla tempore sed eos? Expedita voluptatum dolores impedit voluptates itaque. Quo quidem aut ipsa! Incidunt facere perferendis corporis praesentium est.</p>
            <p className='news-sentiment'>Positive</p>
            <Stack spacing={2} sx={{ flex: 1 }}>
            <LinearProgress determinate value={50} color="success"  variant="solid"/>
    </Stack>
            <div className="news-p">see more...</div>
        </div>
        <div className="news-card">
            <div className="news-card-title">
                Lorem ipsum dolor sit amet consectetur adipisicing elit. Nobis, eum.
            </div>
            <p>Lorem ipsum dolor sit amet consectetur adipisicing elit. Maxime blanditiis saepe totam cumque ipsum omnis voluptatum molestias et facilis suscipit, dolorem similique necessitatibus doloremque modi corporis consequuntur debitis praesentium. Magni nulla tempore sed eos? Expedita voluptatum dolores impedit voluptates itaque. Quo quidem aut ipsa! Incidunt facere perferendis corporis praesentium est.</p>
            <p className='news-sentiment'>Positive</p>
            <Stack spacing={2} sx={{ flex: 1 }}>
            <LinearProgress determinate value={100} color="warning"  variant="solid"/>
    </Stack>
            <div className="news-p">see more...</div>
        </div>




    </div>
  )
}

export default NewsFeed



{/* <LinearProgress determinate value={50} color="success"  variant="solid"/>
<LinearProgress determinate value={75}  color="danger" variant="solid"/>
<LinearProgress determinate value={100} color="warning"  variant="solid"/> */}