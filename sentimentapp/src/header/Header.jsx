import React from 'react'
import './header.css'

const Header = () => {
  return (
    <div className='header-main'>

<div className="header-left">
    <span className='left-t1'>header 1</span> 
    <h3 className='left-t2'>Lorem ipsum dolor sit amet consectetur adipisicing elit. Doloribus, harum.</h3>
    <p className='left-t3'>Lorem ipsum dolor sit amet consectetur adipisicing elit. Velit ea laudantium nisi, a ipsum nulla, reiciendis, dolores dignissimos beatae cumque laboriosam delectus sint voluptas eligendi!</p>
    <p className='left-t4'>Lorem ipsum dolor sit, amet consectetur adipisicing elit. Nostrum sequi consectetur libero deleniti beatae optio.</p>
    <button> Start Now</button>
    <div className="left-icons">
    <i class='bx bxl-instagram'></i>
    <i class='bx bxs-bank' ></i>
    <i class='bx bx-comment-dots' ></i>
    </div>
</div>
<div className="header-right">
</div>

    </div>
  )
}

export default Header