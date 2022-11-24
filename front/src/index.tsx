import MainPage from 'pages/MainPage/MainPage'
import React from 'react'
import { createRoot } from 'react-dom/client'
import { Provider } from 'react-redux'
import ReduxToastr from 'react-redux-toastr'
import { BrowserRouter } from 'react-router-dom'
import { PersistGate } from 'redux-persist/integration/react'

import { persistor, store } from 'store/store'

import './index.scss'
import Meta from './services/Meta'

const container = document.getElementById('root')!
const root = createRoot(container)

root.render(
	<React.StrictMode>
		<BrowserRouter>
			<PersistGate loading={<p>loading...</p>} persistor={persistor}>
				<Provider store={store}>
					<ReduxToastr />
					<Meta title="Cringe Svoyak" desc="Downloable packs">
						<MainPage />
					</Meta>
				</Provider>
			</PersistGate>
		</BrowserRouter>
	</React.StrictMode>
)
