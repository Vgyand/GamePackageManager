import { createSlice } from '@reduxjs/toolkit'
import type { PayloadAction } from '@reduxjs/toolkit'

const initialState: IFlag[] = [{ id: 1, flag: true, value: 0 }]

interface IFlag {
	id: number
	flag: boolean
	value: number
}

const likedSlice = createSlice({
	name: 'like',
	initialState,
	reducers: {
		onLiked(state, action: PayloadAction<IFlag>) {
			state.push(action.payload)
		},
	},
})

export const { onLiked } = likedSlice.actions
export const like = likedSlice.reducer
