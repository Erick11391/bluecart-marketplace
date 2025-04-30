import { useState, useEffect } from 'react'
import './App.css'
import Navbar from './component/Navbar'
import {BrowserRouter, Routes, Route} from 'react-router-dom'
import Product from './page/Product'
import Profile from './page/Profile'
import History from './page/History'
import LandingPage from './store/LandingPage'
import { AuthProvider, RequireAuth } from 'react-auth-kit'


function App() {
  const [count, setCount] = useState(0)
  return (
    <>
    <AuthProvider authType = {'cookie'}
      authName={'_auth'}
      cookieDomain={window.location.hostname}
      cookieSecure= {false}>
      <BrowserRouter>
        <Navbar />
        <Routes>
          <Route exact path='/' element={<LandingPage />} />
          <Route exact path='/history' element={
             <RequireAuth loginPath={'/'}>
             <History/>
           </RequireAuth>
          }/>
          <Route exact path='/product' element={<Product/>}/>
          <Route exact path='/profile' element={
             <RequireAuth loginPath={'/'}>
             <Profile/>
           </RequireAuth>
          }/>
        </Routes>
      </BrowserRouter></AuthProvider>
    </>
  )
}

export default App;
