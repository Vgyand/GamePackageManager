import { createApi, fetchBaseQuery } from '@reduxjs/toolkit/query/react'

export const packsApi = createApi({
	reducerPath: 'packsApi',
	baseQuery: fetchBaseQuery({
		baseUrl: 'http://127.0.0.1:8000/api/',
	}),
	endpoints: (build) => ({
		getAllPacks: build.query({
			query: () => {
				return {
					method: 'GET',
					url: 'packs',
					contentType: 'application/json',
				}
			},
		}),

		getMainPage: build.query({
			query: () => {
				return {
					method: 'GET',
					url: 'main_page',
					contentType: 'application/json',
				}
			},
		}),
	}),
})

export const { useGetAllPacksQuery, useGetMainPageQuery } = packsApi
