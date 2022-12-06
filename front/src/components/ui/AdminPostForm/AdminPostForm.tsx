import { useForm } from 'react-hook-form'

import { useCreateNewPackMutation } from 'store/packsApi'

import styles from './AdminPostForm.module.scss'

const AdminPostForm = () => {
	const [addNewPost, result] = useCreateNewPackMutation()
	const {
		register,
		handleSubmit,
		watch,
		formState: { errors },
	} = useForm()

	const onSubmit = (data: any, e: any) => {
		e.preventDefault()
		addNewPost(data)
			.unwrap()
			.then(() => {
				console.log('s')
			})
			.then((error: any) => {
				console.log(error)
			})
		console.log(data)
	}

	return (
		<form className={styles.adminPostForm} onClick={handleSubmit(onSubmit)}>
			<input
				placeholder="Введите имя пака"
				{...register('name', { required: true })}
			/>
			{errors.name && <span>This field is required</span>}
			<input
				placeholder="Введите описание пака"
				{...register('description', { required: true })}
			/>
			{errors.description && <span>This field is required</span>}
			<input
				placeholder="Введите ссылку на скачивание"
				{...register('download_link', { required: true })}
			/>
			{errors.download_link && <span>This field is required</span>}
			<input
				placeholder="Введите вес пака"
				{...register('size', { required: true })}
			/>
			{errors.exampleRequired && <span>This field is required</span>}

			<button type="submit" className={styles.btn}>
				post
			</button>
		</form>
	)
}

export default AdminPostForm
