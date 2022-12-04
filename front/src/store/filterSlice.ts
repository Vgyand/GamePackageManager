import { createSlice } from '@reduxjs/toolkit'
import type { PayloadAction } from '@reduxjs/toolkit'

export interface FilterState {
	search: string
	downloads: null | 'dec' | 'inc'
	likes: null | 'inc' | 'dec'
	weight: null | 'inc' | 'dec'
}
const initialState = {
	search: '',
	downloads: null,
	likes: null,
	weight: null,
} as FilterState

const filterSlice = createSlice({
	name: 'filter',
	initialState,
	reducers: {
		onFilterSearchChange(state, action: PayloadAction<string>) {
			console.log(action.payload.search)
			state.search = action.payload
		},
		onFilterSelectChange(state, action: any) {
			if (action.payload.val == 'likes') {
				state.downloads = null
				state.weight = null
				state.likes = action.payload.mod
			}
			if (action.payload.val == 'downloads') {
				state.likes = null
				state.weight = null
				state.downloads = action.payload.mod
			}
			if (action.payload.val == 'weight') {
				state.downloads = null
				state.likes = null
				state.weight = action.payload.mod
			}
			state
		},
	},
})

export const { onFilterSearchChange, onFilterSelectChange } =
	filterSlice.actions
export const filter = filterSlice.reducer
