import './App.css';
import axios from 'axios';
import React, {useState, useEffect} from 'react'
import './Additem.js'
import Additem from './Additem.js'


function App(){

  const [item, setItem] = useState([])
  const [umsg, setUmsg] = useState([])
  const [itemmsg, setItemmsg] = useState([])
  const [UiId, setiId] = useState([])
  const [Iname, setIname] = useState([])
  const [Sprice, setSprice] = useState([])

function updateSetup(e, i, n, p){
     
  setiId(i)
  setIname(n)
  setSprice(p)
}

function getitemiId(iId) {
  axios.get(`http://127.0.0.1:5000/getitemiId/${iId}`)
    .then(response => {
      if (response.status === 200 && JSON.stringify(response.data.data)!=="[]") {
        console.log(JSON.stringify(response.data.data))
        setItemmsg(`Item Found: ${JSON.stringify(response.data.data)}`);
      } else {
        setItemmsg('Item not found');
      }
    })
    .catch(error => {
      console.error(error);
      setUmsg('Something went wrong while getting item');
    });
}

function updateitem(e) {
        
  const X = {
    "iId" : UiId,
    "Iname" : Iname,
    "Sprice" : Sprice 
  }

  axios.put('http://127.0.0.1:5000/update_item', X)
      .then (response => {
            if (response.status === 200) {
                setUmsg('Item Updated')
            }
            else {
                setUmsg('Update - something is wrong')
            }
        })

  }

function deleteitem(e, iId) {
  console.log('delete '+iId)
  axios.delete('http://127.0.0.1:5000/delete_item'+iId)
      .then(response => {
            if (response.status === 200) {
                setUmsg('Item Deleted')
                getAll()
            }  
            else {
                setUmsg('Delete - something is wrong')
            } 
        })
    }

function getAll(){

    axios.get('http://127.0.0.1:5000/getitem')
    .then(response => {
        console.log(response)
        if (response.status === 200){
            console.log(response.data)
            setItem(response.data.data)
        }
        else {
            console.log('Something is wrong')

         }
      })
    } 


    useEffect(() => {
        getAll()
    }, []);


    return (
      <div className=''>
        <div>ITEM</div>

        <table>
          <thead>
            <tr>
              <th>iId</th>
              <th>Iname</th>
              <th>Sprice</th>
              <th>Update</th>
              <th>Delete</th>
            </tr>
          </thead>
        <tbody>
        { item.map(item =>
        <tr key={item[0]}>
          <td>{item[0]}</td>
          <td>{item[1]}</td>
          <td>{item[2]}</td>
          <td><button className='btn btn-primary' onClick={e => updateSetup(e, item[0], item[1], item[2])}>Update</button></td>
          <td><button className='btn btn-primary' onClick={e => deleteitem(e, item[0])}>Delete</button></td>
        </tr> )
        }
      </tbody>
    </table>

    <div>
      <div><h1>Search Item</h1></div>
      <form onSubmit={e => { e.preventDefault(); getitemiId(UiId)}}>
        <input value={UiId} onChange={e => setiId(e.target.value)} type='text' name='iId' required />
        <button className='btn btn-info' type='submit'>Search</button>
        <div>{itemmsg ? <p>{itemmsg}</p> : null}</div>
      </form>
    </div>
    <div>
    <h1>Search Results</h1>
           <p></p>
        
    </div>

    <Additem>


    </Additem>
            
      <div>
        <div>Update item</div>
        <form onSubmit={updateitem}>
                <input value={Iname}
                onChange={e=>setIname(e.target.value)}
                type= 'text' name='Iname'
                required />

                <input value={Sprice}
                onChange={e=>setSprice(e.target.value)}
                type='text' name='Sprice'
                required />

                <input value={UiId}
                onChange={e=>setSprice(e.target.value)}
                type='text' name='iId'
                required />
                <button className='btn btn-success' type='submit'>Update</button>
    
                <div>{umsg ? <p>{umsg}</p> : null}</div>
                </form>
      </div>
      {umsg}
    </div>

    
    
    );
}


export default App