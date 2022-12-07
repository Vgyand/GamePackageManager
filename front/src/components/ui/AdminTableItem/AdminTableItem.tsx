import { useState } from 'react'

import close from 'assets/icons/close.png'

import { useDeletePackMutation } from 'store/packsApi'

import styles from './AdminTableItem.module.scss'

const AdminTableItem = ({ id, name, downloadCount, likeCount, index }: any) => {
	const [openName, setOpenName] = useState(false)
	const [deletePost] = useDeletePackMutation()
	console.log(id)
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
					onClick={() => deletePost({ id })}
					className={styles.pack_table__img}
				/>
			</button>
		</tr>
	)
}

export default AdminTableItem
