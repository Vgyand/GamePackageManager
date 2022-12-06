import close from 'assets/icons/close.png'

import { useDeletePackMutation } from 'store/packsApi'

import styles from './AdminTableItem.module.scss'

const AdminTableItem = ({ id, name, downloadCount, likeCount, index }: any) => {
	const [deletePost, response] = useDeletePackMutation()
	console.log(id)
	return (
		<tr
			key={id}
			style={{
				backgroundColor: `${index % 2 == 0 ? 'grey' : 'white'}`,
			}}
		>
			<td> {id}</td>
			<td> {name}</td>
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
