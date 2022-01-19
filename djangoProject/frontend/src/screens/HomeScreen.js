import React, { useEffect } from 'react'
import { useDispatch, useSelector } from 'react-redux'
import Loader from '../components/Loader'
import Message from '../components/Message'
import { listProducts } from '../actions/productActions'
import { Row } from 'react-bootstrap'

const HomeScreen = () => {
  const dispatch = useDispatch()

  const productList = useSelector(state=>state.productList)
  const { loading, error, products } = productList

  useEffect(() => {
    dispatch(listProducts())
  }, [dispatch])
  console.log(products);
  return (
    <>
      <h1>Latest Products</h1>
      {loading ? <Loader /> : error ? <Message variant='danger' >{error} </Message> :
        <Row>
          {/* {products.map(product => (
            console.log(product.name)
          ))} */}
        </Row>
      }
    </>
  )
}

export default HomeScreen
