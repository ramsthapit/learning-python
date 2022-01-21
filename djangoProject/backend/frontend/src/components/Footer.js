import React from 'react'
import { Col, Container, Row } from 'react-bootstrap'

const Footers = () => {
  return (
    <footer>
      <Container>
        <Row>
          <Col className='text-center py-3'>
            Copyright &copy; ecommerce
          </Col>
        </Row>
      </Container>
    </footer>
  )
}

export default Footers
