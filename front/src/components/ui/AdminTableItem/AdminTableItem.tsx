import close from 'assets/icons/close.png'

import styles from './AdminTableItem.module.scss'

const AdminTableItem = ({ id, name, downloadCount, likeCount, index }: any) => {
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
				<img src={close} alt="delete" className={styles.pack_table__img} />
			</button>
		</tr>
	)
}

export default AdminTableItem
