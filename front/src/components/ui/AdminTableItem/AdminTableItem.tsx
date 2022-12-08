import { useState } from 'react'

import close from 'assets/icons/close.png'

import {
	useDeletePackMutation,
	useUpdatePacksNameMutation,
} from 'store/packsApi'

import styles from './AdminTableItem.module.scss'

const AdminTableItem = ({
	id,
	name,
	downloadCount,
	likeCount,
	index,
	refetch,
}: any) => {
	const [openName, setOpenName] = useState(false)
	const [deletePost] = useDeletePackMutation()
	const [updatePack] = useUpdatePacksNameMutation()

	const deleteHandler = () => {
		deletePost({ id })
		refetch()
	}
	const updateName = (event: any) => {
		console.log(event.target.value)
		const result = confirm(`Change name ${name} to ${event.target.value}`)
		console.log(result)
		if (result) updatePack({ id, name: event.target.value })
		refetch()
		setOpenName(!openName)
	}

	return (
		<tr
			key={id}
			style={{
				backgroundColor: `${index % 2 == 0 ? 'grey' : 'white'}`,
			}}
		>
			<td>{id}</td>
			<td onDoubleClick={() => setOpenName(!openName)}>
				{openName ? (
					<input onBlur={updateName} placeholder={name} type="text" autoFocus />
				) : (
					name
				)}
			</td>
			<td> {downloadCount}</td>
			<td> {likeCount}</td>
			<button>
				<img
					src={close}
					alt="delete"
					onClick={deleteHandler}
					className={styles.pack_table__img}
				/>
			</button>
		</tr>
	)
}

export default AdminTableItem
