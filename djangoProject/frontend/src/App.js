import React from 'react'
import Footer from './components/Footer'
import Header from './components/Header'
import {Container} from 'react-bootstrap'
import { BrowserRouter, Route } from 'react-router-dom'
import HomeScreen from './screens/HomeScreen'
import ProductScreen from './screens/ProductScreen'

const App = () => {
  return (
    <BrowserRouter>
      <Header />
      <main>
        <Container>
          <Route path='/' component={HomeScreen} exact />
          <Route path='/products' component={ProductScreen} exact />
        </Container>
      </main>
      <Footer />
    </BrowserRouter>
  )
}

export default App
