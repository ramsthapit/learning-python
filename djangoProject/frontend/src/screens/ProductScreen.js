import React, { useEffect } from 'react'
import { Button, Card, Col, Image, ListGroup, Row } from 'react-bootstrap'
import { useDispatch, useSelector } from 'react-redux'
import { listProductDetails } from '../actions/productActions'
import Loader from '../components/Loader'
import Message from '../components/Message'


const ProductScreen = ({match, history}) => {

  const dispatch = useDispatch()

  const productDetails = useSelector(state => state.productDetails)
  const { loading, error, product } = productDetails

  useEffect(() => {
    dispatch(listProductDetails(match.params.id))
  }, [dispatch, match])
  
  const addToCartHandler = () => {
    console.log("add to cart")
  }
  return (
    <>
      {loading ? <Loader /> : error ? <Message variant='danger' >{error} </Message> :
        (
          <div>
            <Row>
                <Col md={6}>
                    <Image src={product.image} alt={product.name} fluid />
                </Col>


                <Col md={3}>
                    <ListGroup variant="flush">
                        <ListGroup.Item>
                          <h3>{product.name}</h3>
                        </ListGroup.Item>

                        <ListGroup.Item>
                          <h3>{product.rating}</h3>
                        </ListGroup.Item>

                        <ListGroup.Item>
                          Price: ${product.price}
                        </ListGroup.Item>

                        <ListGroup.Item>
                          Description: {product.description}
                        </ListGroup.Item>
                    </ListGroup>
                </Col>


                <Col md={3}>
                  <Card>
                    <ListGroup variant='flush'>
                      <ListGroup.Item>
                          <Row>
                              <Col>Price:</Col>
                              <Col>
                                  <strong>${product.price}</strong>
                              </Col>
                          </Row>
                      </ListGroup.Item>
                      <ListGroup.Item>
                          <Row>
                              <Col>Status:</Col>
                              <Col>
                                  {product.countInStock > 0 ? 'In Stock' : 'Out of Stock'}
                              </Col>
                          </Row>
                      </ListGroup.Item>
                      
                      <ListGroup.Item>
                          <Button
                              onClick={addToCartHandler}
                              className='btn-block'
                              disabled={product.countInStock === 0}
                              type='button'>
                              Add to Cart
                          </Button>
                      </ListGroup.Item>
                    </ListGroup>
                  </Card>
                </Col>
            </Row>
        </div>
        )
      
      }
    </>
  )
}

export default ProductScreen
