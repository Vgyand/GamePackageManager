import { useState } from 'react'

import close from 'assets/icons/close.png'

import { useDeletePackMutation } from 'store/packsApi'

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
	console.log(id)

	const deleteHandler = () => {
		deletePost({ id })
		refetch()
	}
	return (
		<tr
			key={id}
			style={{
				backgroundColor: `${index % 2 == 0 ? 'grey' : 'white'}`,
			}}
		>
			<td> {id}</td>
			<td onDoubleClick={() => setOpenName(!openName)}>
				{openName ? (
					<input
						onBlur={() => setOpenName(!openName)}
						placeholder={name}
						type="text"
						autoFocus
					/>
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
