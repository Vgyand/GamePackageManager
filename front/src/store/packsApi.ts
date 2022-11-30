import { createApi, fetchBaseQuery } from '@reduxjs/toolkit/query/react'

export const packsApi = createApi({
	reducerPath: 'packsApi',
	baseQuery: fetchBaseQuery({
		baseUrl: 'https://localhost:3001/api',
	}),
	endpoints: (build) => ({
		getAllPacks: build.query({
			query: () => {
				return {
					method: 'GET',
					url: '/',
					contentType: 'application/json',
				}
			},
			transformResponse(response: any) {
				return response.filter((el: any) => el)
			},
		}),
	}),
})

export const { useGetAllPacksQuery } = packsApi
