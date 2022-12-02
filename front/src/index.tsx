import App from 'pages/App'
import React from 'react'
import { createRoot } from 'react-dom/client'
import { Provider } from 'react-redux'
import ReduxToastr from 'react-redux-toastr'
import { BrowserRouter } from 'react-router-dom'
import { PersistGate } from 'redux-persist/integration/react'

import ErrorBoundary from 'components/ErrorBoundary/ErrorBoundary'

import { persistor, store } from 'store/store'

import './index.scss'
import Meta from './services/Meta'

const container = document.getElementById('root')!
const root = createRoot(container)

root.render(
	<React.StrictMode>
		<BrowserRouter>
			<ErrorBoundary>
				<PersistGate loading={<p>loading...</p>} persistor={persistor}>
					<Provider store={store}>
						<ReduxToastr />
						<Meta title="Cringe Svoyak" desc="Downloable packs">
							<App />
						</Meta>
					</Provider>
				</PersistGate>
			</ErrorBoundary>
		</BrowserRouter>
	</React.StrictMode>
)
