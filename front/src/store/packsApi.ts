import { createApi, fetchBaseQuery } from '@reduxjs/toolkit/query/react'

import { FilterState } from './filterSlice'

export const packsApi = createApi({
	reducerPath: 'packsApi',
	baseQuery: fetchBaseQuery({
		baseUrl: 'http://127.0.0.1:8000/api/',
	}),
	endpoints: (build) => ({
		getAllPacks: build.query({
			query: (filter: FilterState) => {
				console.log(filter.search)
				const params: any = {}
				console.log(params)
				if (filter.search) params.search = filter.search
				if (filter.downloads) params.downloads = filter.downloads
				if (filter.likes) params.likes = filter.likes
				if (filter.weight) params.weight = filter.weight
				return {
					method: 'GET',
					url: 'packs',
					contentType: 'application/json',
					params,
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
