import React from 'react'
import { Route, Routes } from 'react-router-dom'

import AdminPanel from './AdminPanel/AdminPanel'
import MainPage from './MainPage/MainPage'

const App = () => {
	return (
		<Routes>
			<Route path="/" index element={<MainPage />} />
			<Route path="/admin" index element={<AdminPanel />} />
		</Routes>
	)
}

export default App
