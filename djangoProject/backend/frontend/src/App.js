import React from 'react'
import Footer from './components/Footer'
import Header from './components/Header'

import {BrowserRouter} from 'react-router-dom'

const App = () => {
  return (
    <BrowserRouter>
      <Header />
      <main className='py-3'>
        <h1>ram sthapit</h1>
      </main>
      <Footer />
    </BrowserRouter>
  )
}

export default App
