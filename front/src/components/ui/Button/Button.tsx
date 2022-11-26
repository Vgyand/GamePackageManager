import styles from './Button.module.scss'

export interface IButton {
	text: string
	handler: () => void
}

const Button = ({ text, handler }: IButton) => {
	return (
		<button className={styles.btn} onClick={handler}>
			{text}
		</button>
	)
}

export default Button
