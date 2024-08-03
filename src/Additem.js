
import React, {useState} from 'react'
import axios from 'axios';

function Additem() {

    const [UiId, setiId] = useState([])
    const [Iname, setIname] = useState([])
    const [Sprice, setSprice] = useState([])
    const [umsg, setUMsg] = useState([])


    function Additem(e) {
        
        const payload = {
            "iId" : UiId,
            "Iname" : Iname,
            "Sprice" : Sprice
        }
        axios.post('http://127.0.0.1:5000/insert_item', payload)
         .then(respose => {
            if (respose.status === 200) {
                setiId('')
                setIname('')
                setSprice('')
                setUMsg('Item Added')
            }
            else {
                setUMsg('something is wrong')
            }

         })
    }
    return (
        <div>
            Additem
            <form onSubmit={Additem}>
                <input value = {UiId}
                onChange={e=>setiId(e.target.value)}
                placeholder='iId'
                type='text' name='iId'
                required />

                <input values={Iname}
                onChange={e=>setIname(e.target.value)}
                placeholder='Iname'
                type='text' name='Iname'
                required />

                <input values={Sprice}
                onChange={e=>setSprice(e.target.value)}
                placeholder='Sprice'
                type='text' name='Sprice'
                required />

                <button className='btn btn-sucess' type='submit'>Add</button>
                <div>{umsg ? <p>{umsg}</p> : null} </div>
            </form>

        </div>
    );
}

export default Additem;